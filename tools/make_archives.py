from __future__ import annotations

import hashlib
import os
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = Path(r"C:\Users\Floris\Documents\interlanguage")
REBASE = WORKSPACE / r"03_projects\language_management\cjk\03_working_translations\japanese\rebase"
CHECKER = WORKSPACE / r"03_projects\language_management\cjk\05_independent_checking\cjk_r1"
AUTH = WORKSPACE / r"03_projects\noether\07_german_canon_control"
METHOD = WORKSPACE / r"methodology\multilingual-publication-datacite-zenodo-github"
RELEASE = ROOT / "release"

SOURCE_ZIP = RELEASE / "01_EMMY_NOETHER_JA_EDITABLE_SOURCES.zip"
EVIDENCE_ZIP = RELEASE / "02_EMMY_NOETHER_JA_EVIDENCE_AND_PROVENANCE.zip"

FIXED_DT = (2026, 8, 13, 0, 0, 0)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def add_tree(entries: dict[str, Path], source: Path, prefix: str) -> None:
    for path in sorted(p for p in source.rglob("*") if p.is_file()):
        rel = path.relative_to(source).as_posix()
        entries[f"{prefix}/{rel}"] = path


def selected_method_files() -> dict[str, Path]:
    entries: dict[str, Path] = {}
    for path in sorted(p for p in METHOD.iterdir() if p.is_file()):
        entries[f"method/{path.name}"] = path
    scaffold = METHOD / "07_COPYABLE_LANGUAGE_RELEASE_SCAFFOLD"
    add_tree(entries, scaffold, "method/07_COPYABLE_LANGUAGE_RELEASE_SCAFFOLD")
    return entries


def write_zip(output: Path, entries: dict[str, Path]) -> tuple[int, str]:
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(output.suffix + ".tmp")
    if temporary.exists():
        temporary.unlink()

    rows = ["archive_path\tbytes\tsha256"]
    material: list[tuple[str, bytes]] = []
    for archive_path, source in sorted(entries.items()):
        data = source.read_bytes()
        material.append((archive_path, data))
        rows.append(f"{archive_path}\t{len(data)}\t{sha256(data)}")
    manifest = ("\n".join(rows) + "\n").encode("utf-8")
    material.append(("ARCHIVE_CONTENTS.tsv", manifest))

    with zipfile.ZipFile(
        temporary,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for archive_path, data in material:
            info = zipfile.ZipInfo(archive_path, FIXED_DT)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (0o100644 & 0xFFFF) << 16
            info.flag_bits |= 0x800
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    with zipfile.ZipFile(temporary, "r") as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise RuntimeError(f"duplicate archive paths in {temporary}")
        bad = archive.testzip()
        if bad is not None:
            raise RuntimeError(f"CRC failure in {temporary}: {bad}")
        if names[-1] != "ARCHIVE_CONTENTS.tsv":
            raise RuntimeError("archive manifest is not the final entry")

    data = temporary.read_bytes()
    digest = sha256(data)
    os.replace(temporary, output)
    return len(material), digest


def source_entries() -> dict[str, Path]:
    entries: dict[str, Path] = {
        "README.md": ROOT / "README.md",
        "CITATION.cff": ROOT / "CITATION.cff",
        ".zenodo.json": ROOT / ".zenodo.json",
        "LICENSE": ROOT / "LICENSE",
        "build/BUILD.ps1": ROOT / "build" / "BUILD.ps1",
        "tools/make_reader.py": ROOT / "tools" / "make_reader.py",
        "evidence/SOURCE_AUTHORITY.json": ROOT / "evidence" / "SOURCE_AUTHORITY.json",
        "authority/CURRENT_GERMAN_AUTHORITY_POINTER.json": AUTH / "CURRENT_GERMAN_AUTHORITY_POINTER.json",
        "authority/ED0014/noether.tex": AUTH / "candidates" / "ED0014" / "noether.tex",
        "authority/ED0014/authority_rosette_native_supported_mask.png": AUTH / "candidates" / "ED0014" / "authority_rosette_native_supported_mask.png",
    }
    add_tree(entries, ROOT / "source", "ja")
    return entries


def evidence_entries() -> dict[str, Path]:
    fixed_publication_evidence = (
        "SOURCE_AUTHORITY.json",
        "QA_STATE.json",
        "UNRESOLVED_ITEMS.tsv",
        "DATACITE_RELATIONS.json",
        "R10_CHECKER_STATUS.md",
        "PUBLICATION_STATE.md",
        "R10_ORIGINAL_READER_EXACT.pdf",
    )
    entries: dict[str, Path] = {
        f"publication/{name}": ROOT / "evidence" / name
        for name in fixed_publication_evidence
    }
    entries["publication/tools/make_reader.py"] = ROOT / "tools" / "make_reader.py"
    entries["publication/tools/make_archives.py"] = ROOT / "tools" / "make_archives.py"
    entries["publication/build/BUILD.ps1"] = ROOT / "build" / "BUILD.ps1"

    add_tree(entries, REBASE, "rebase")

    for path in sorted(CHECKER.glob("ja_r*")):
        if path.is_file() and path.suffix.lower() in {".csv", ".md"}:
            entries[f"checker/{path.name}"] = path
    for name in ("ext_sys.csv", "ext_sys.md"):
        entries[f"checker/{name}"] = CHECKER / name

    governance = {
        "governance/USER_VERBATIM_THREAD_BRIEF_20260717.md": WORKSPACE / r"00_governance\USER_VERBATIM_THREAD_BRIEF_20260717.md",
        "governance/RESET_20260804.md": WORKSPACE / r"03_projects\language_management\cjk\00_lane_control\RESET_20260804.md",
        "governance/REBASE_NOT_REWRITE.md": WORKSPACE / r"01_methodology\research_department\REBASE_NOT_REWRITE.md",
    }
    entries.update(governance)
    entries.update(selected_method_files())
    return entries


def main() -> None:
    source_count, source_hash = write_zip(SOURCE_ZIP, source_entries())
    evidence_count, evidence_hash = write_zip(EVIDENCE_ZIP, evidence_entries())
    print(f"SOURCE entries={source_count} bytes={SOURCE_ZIP.stat().st_size} sha256={source_hash}")
    print(f"EVIDENCE entries={evidence_count} bytes={EVIDENCE_ZIP.stat().st_size} sha256={evidence_hash}")


if __name__ == "__main__":
    main()
