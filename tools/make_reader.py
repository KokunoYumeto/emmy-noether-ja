from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
BODY = ROOT / "evidence" / "R10_ORIGINAL_READER_EXACT.pdf"
COVER = ROOT / "tmp" / "pdfs" / "publication-cover.pdf"
OUTPUT = ROOT / "reader" / "00_EMMY_NOETHER_JA_COMPLETE_LINKED_READER.pdf"
FONT = Path(r"C:\Windows\Fonts\YuGothM.ttc")

VERSION_DOI = "10.5281/zenodo.21921485"
CONCEPT_DOI = "10.5281/zenodo.21921484"
GLOBAL_DOI = "10.5281/zenodo.20412587"
REPOSITORY = "https://github.com/KokunoYumeto/emmy-noether-ja"


def draw_link(c: canvas.Canvas, text: str, url: str, x: float, y: float, size: float = 9.5):
    c.setFont("YuGothic", size)
    c.setFillColor(HexColor("#174E74"))
    c.drawString(x, y, text)
    width = pdfmetrics.stringWidth(text, "YuGothic", size)
    c.linkURL(url, (x, y - 2, x + width, y + size + 1), relative=0)


def make_cover():
    pdfmetrics.registerFont(TTFont("YuGothic", str(FONT), subfontIndex=0))
    width, height = A4
    c = canvas.Canvas(str(COVER), pagesize=A4, pageCompression=1, invariant=1)
    c.setTitle("エミー・ネーター数学論文全集 — 完全日本語版")
    c.setAuthor("Emmy Noether; Manuscript Typesetting Project; OpenAI Codex")
    c.setSubject("Complete Japanese corpus edition, cumulative release r10")

    navy = HexColor("#123A56")
    gold = HexColor("#B38A37")
    grey = HexColor("#44515B")
    pale = HexColor("#F3F7F9")

    c.setFillColor(navy)
    c.rect(0, height - 92, width, 92, stroke=0, fill=1)
    c.setFillColor(gold)
    c.rect(0, height - 98, width, 6, stroke=0, fill=1)

    c.setFillColor(HexColor("#FFFFFF"))
    c.setFont("YuGothic", 22)
    c.drawString(48, height - 53, "エミー・ネーター数学論文全集")
    c.setFont("YuGothic", 12)
    c.drawString(49, height - 76, "完全日本語版・累積版 r10")

    y = height - 142
    c.setFillColor(navy)
    c.setFont("YuGothic", 14)
    c.drawString(48, y, "Emmy Noether: Complete Japanese Corpus Edition")
    y -= 28
    c.setFillColor(grey)
    c.setFont("YuGothic", 10.2)
    lines = [
        "原著者: Emmy Noether（エミー・ネーター）",
        "翻訳・組版: Manuscript Typesetting Project / OpenAI Codex",
        "言語: 日本語 (BCP 47: ja; Zenodo: jpn)",
        "範囲: 維持対象のネーター全論文コーパス（Post-P43 資料を含む）",
        "基準: NOETH-DE-AUTH-v051-20260811 / NOETH-DE-ED-0014",
        "ドイツ語本文 SHA-256: EE226847656BC4D65EDDA9E9BF9BB1D25797C0C6D672D267D94A97FD88C7AD58",
        "日本語 r10 原 PDF SHA-256: 1194204B23B02A302E925590DD5A8D411F7FC308A9E12F763C485674C6CB0E25",
    ]
    for line in lines:
        c.drawString(48, y, line)
        y -= 18

    y -= 8
    c.setFillColor(pale)
    c.roundRect(42, y - 104, width - 84, 116, 7, stroke=0, fill=1)
    c.setFillColor(navy)
    c.setFont("YuGothic", 11)
    c.drawString(54, y - 8, "永続識別子と公開先")
    draw_link(c, f"日本語版 Concept DOI: {CONCEPT_DOI}", f"https://doi.org/{CONCEPT_DOI}", 54, y - 31)
    draw_link(c, f"この版の DOI: {VERSION_DOI}", f"https://doi.org/{VERSION_DOI}", 54, y - 51)
    draw_link(c, f"多言語ハブ DOI: {GLOBAL_DOI}", f"https://doi.org/{GLOBAL_DOI}", 54, y - 71)
    draw_link(c, f"GitHub: {REPOSITORY}", REPOSITORY, 54, y - 91)

    y -= 142
    c.setFillColor(navy)
    c.setFont("YuGothic", 11)
    c.drawString(48, y, "版の状態")
    y -= 22
    c.setFillColor(grey)
    c.setFont("YuGothic", 9.3)
    state_lines = [
        "本書は全コーパスを収録する現行日本語 r10 を一冊にまとめた独立公開版である。",
        "二回の固定時刻 XeLaTeX ビルドは同一バイトの 421 頁 PDF を生成した。",
        "独立 r10 監査で報告された継承済みの数式・意味上の指摘 4 件は、確定返却前の未解決事項として保持する。",
        "数式フォントの ToUnicode 不足 (CJK-NOETH-EXT-SYS-001) も未解決である。",
        "完全な出典、変更箇所、用語台帳、反証・失敗記録、査読返却、ビルド記録は証拠 ZIP に収録した。",
        "「完全」は収録範囲を示す。無欠陥または外部承認済みであることを意味しない。",
    ]
    for line in state_lines:
        c.drawString(48, y, line)
        y -= 17

    c.setStrokeColor(gold)
    c.line(48, 74, width - 48, 74)
    c.setFillColor(grey)
    c.setFont("YuGothic", 8.3)
    c.drawString(48, 56, "独立維持・AI 生成の日本語版 / 2026-08-13 / Version r10")
    c.drawRightString(width - 48, 56, "本文 421 頁 + 公開表紙 1 頁")
    c.save()


def merge():
    cover_reader = PdfReader(str(COVER))
    body_reader = PdfReader(str(BODY))
    writer = PdfWriter()
    writer.append(cover_reader, import_outline=True)
    writer.append(body_reader, import_outline=True)
    writer.add_metadata(
        {
            "/Title": "エミー・ネーター数学論文全集 — 完全日本語版",
            "/Author": "Emmy Noether; Manuscript Typesetting Project; OpenAI Codex",
            "/Subject": "Complete Japanese corpus edition, cumulative release r10",
            "/Keywords": "Emmy Noether, Japanese, translation, mathematics, algebra",
        }
    )
    with OUTPUT.open("wb") as stream:
        writer.write(stream)


if __name__ == "__main__":
    make_cover()
    merge()
    result = PdfReader(str(OUTPUT))
    print(f"pages={len(result.pages)}")
    print(f"encrypted={result.is_encrypted}")
