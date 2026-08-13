# エミー・ネーター数学論文全集 — 完全日本語版

[完全版のリンク付きリーダーを開く](reader/00_EMMY_NOETHER_JA_COMPLETE_LINKED_READER.pdf)

- 日本語版 Concept DOI: [10.5281/zenodo.21921484](https://doi.org/10.5281/zenodo.21921484)
- この版の DOI: [10.5281/zenodo.21921485](https://doi.org/10.5281/zenodo.21921485)
- 直接プレビュー: [00_EMMY_NOETHER_JA_COMPLETE_LINKED_READER.pdf](https://zenodo.org/records/21921485/files/00_EMMY_NOETHER_JA_COMPLETE_LINKED_READER.pdf)
- 直接ダウンロード: [PDF](https://zenodo.org/records/21921485/files/00_EMMY_NOETHER_JA_COMPLETE_LINKED_READER.pdf?download=1)
- 多言語ハブ: [10.5281/zenodo.20412587](https://doi.org/10.5281/zenodo.20412587)
- 言語: 日本語 (`ja`; Zenodo `jpn`)
- 版: `2026-08-13 r10`
- Git タグ: `ja-r10-20260813`

このリポジトリは、エミー・ネーターの維持対象数学論文コーパス全体（Post-P43 資料を含む）の独立した日本語累積版を公開する。`完全` は収録範囲を示し、無欠陥、外部承認済み、または校訂版として確定済みであることを意味しない。

基準ドイツ語本文は `NOETH-DE-AUTH-v051-20260811` / `NOETH-DE-ED-0014`、SHA-256 `EE226847656BC4D65EDDA9E9BF9BB1D25797C0C6D672D267D94A97FD88C7AD58` である。日本語 r10 の元 PDF は 421 頁、SHA-256 `1194204B23B02A302E925590DD5A8D411F7FC308A9E12F763C485674C6CB0E25`。公開リーダーは識別情報を記した表紙 1 頁を加えた 422 頁である。

## 状態

r10 の系譜、全 58 区間の被覆、ED0011→ED0014 の限定差分、および固定時刻二回ビルドの機械的再現性は記録済みである。独立 r10 監査は保管・系譜・被覆を再現したが、確定返却前に中断され、継承済みの数式・意味上の候補指摘 4 件を残した。数式フォントの ToUnicode 不足 `CJK-NOETH-EXT-SYS-001` も未解決である。正確な状態と根拠は `evidence/QA_STATE.json` と `evidence/UNRESOLVED_ITEMS.tsv` にある。

## 公開物

- `reader/`: 直ちに読める完全累積リーダー。
- `source/`: 日本語の編集可能な TeX と必要な画像資産。
- `evidence/`: 出典、DOI 関係、QA 状態、未解決事項、ハッシュ。
- Zenodo の `01_...SOURCES.zip`: 日本語ソースと凍結ドイツ語基準。
- Zenodo の `02_...EVIDENCE_AND_PROVENANCE.zip`: rebase 履歴、変更台帳、用語・反証記録、独立チェック返却、ビルド記録、統治・方法資料。

この日本語版は、同じ知的範囲の原典を収める多言語ハブ DOI の `IsTranslationOf` 対象であり、同時に同ハブの `IsPartOf` 構成要素である。現行 Zenodo 語彙が翻訳関係を公開しないため、完全な DataCite 4.7 の意図は `evidence/DATACITE_RELATIONS.json` に保存する。

## English identification

This is the standalone Japanese (`ja`) cumulative edition of the maintained complete Emmy Noether mathematical corpus. The reader is complete in coverage, while four inherited formula/meaning observations and the shared ToUnicode extraction defect remain explicitly unresolved. The exact German authority, source lineage, build evidence, checker returns, terminology decisions, adverse records, and all public-file hashes are preserved with the release. Human review is welcome but is not a publication dependency.
