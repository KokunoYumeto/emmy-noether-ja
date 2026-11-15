# エミー・ネーター — 数学著作集・日本語版

エミー・ネーター（Emmy Noether, 1882–1935）の数学著作集の日本語訳です。論文1–43、M. Deuring が筆録した1929/30年冬学期の講義「超複素量の代数」、H. Kapferer の論文と E. Noether との共著による補遺、文献目録、ならびに短報・書評・Noether が関与した書籍の一覧を収録します。不変式、イデアル、体、代数および表現論を扱います。PDF と編集可能な LaTeX で提供します。

[**基礎本文の PDF を読む（422頁）**](https://github.com/KokunoYumeto/emmy-noether-ja/releases/download/noether-ja-2026-11-15-r2/01-noether-ja-base.pdf) · [校訂本文の PDF（427頁）](https://github.com/KokunoYumeto/emmy-noether-ja/releases/download/noether-ja-2026-11-15-r2/04-noether-ja-emendations.pdf) · [2026年10月27日版のすべてのファイル](https://github.com/KokunoYumeto/emmy-noether-ja/releases/tag/noether-ja-2026-11-15-r2)

## How this was made: AI's failure modes, and what we do about them

Everything here was produced by AI. The translation was made in a first pass mostly by GPT-5.6 Sol (OpenAI Codex,
reasoning effort ultra) (July and August 2026). Its formulas were then brought into line with the German text, which Claude Opus 5.5 at
effort max compared page by page with Noether's printed originals (785 page checks, 26 October 2026), in automatic and
hand rounds by Claude Opus 5.5 at effort max (26-27 October; 2,570 lines in the last hand round), against the known
failures of AI translation of mathematics: renamed letters, formulas changed or dropped, statements narrowed, passages
reworked or garbled, sentences and displays dropped, broken layout. Every change passes a release filter, and every PDF
is checked for lines running into the margin (Claude Opus 5.5 at effort high, 15 November). No person has reviewed the
translation. What was done in each round, the measured figures and what is still open:
[How this was made](https://github.com/KokunoYumeto/emmy-noether#how-this-was-made-ais-failure-modes-and-what-we-do-about-them).

## 制作方法

日本語訳は AI による翻訳です。翻訳は OpenAI Codex のモデルが行いました（主に GPT-5.6 Sol、推論設定 ultra）。本版の底本は、2026年8月13日の日本語版 r10 とドイツ語版 ED0014/v051 です。本版の訂正と組版は、OpenAI Codex — GPT-6 Astra（推論設定 Ultra、2026年10月23–24日）と Claude Opus 5.5（Anthropic、推論設定 max、2026年10月26–27日）が行いました。Claude Opus 5.5 は、数式を Noether の印刷ページから読んだドイツ語本文と照合して合わせました。組版プログラムは OpenAI Codex — GPT-6 Astra（Ultra、2026年10月24日）が作成しました。

## 現状

上記の著作はすべて収録されていますが、次の点が残っています。論文32、34、40（および論文30、35、41、42の一部）は以前の英訳に拠っており、その数式はところどころドイツ語本文と異なります。論文40と41は約4分の3に短縮されています。論文2では、Σ₃ に関する脚注が隣の文に組み込まれており、数式中の本来の位置には記号 `*)` だけがあります。論文10、13、38には、ドイツ語本文と読みが異なる箇所があるかもしれません。PDF にはしおり（アウトライン）がありません。翻訳は人間による確認を受けていないため、誤りが残っている可能性があります。翻訳が独自の言い回しで訳した箇所では、一部の数式がまだ以前のドイツ語翻刻に従っていることがあります。誤りの報告や修正の提案は [GitHub issues](https://github.com/KokunoYumeto/emmy-noether-ja/issues) で受け付けています。

## 内容と読み方

本版は二つの本文で提供され、それぞれに PDF、LaTeX ファイル1点、組版用ソースの ZIP があります。

| 本文 | PDF | LaTeX | ソース |
|---|---|---|---|
| 基礎本文：原刊の読みを保持し、問題となる読みは編集注で論じます | [PDF、422頁](https://github.com/KokunoYumeto/emmy-noether-ja/releases/download/noether-ja-2026-11-15-r2/01-noether-ja-base.pdf) | [LaTeX](https://github.com/KokunoYumeto/emmy-noether-ja/releases/download/noether-ja-2026-11-15-r2/02-noether-ja-base.tex) | [ZIP](https://github.com/KokunoYumeto/emmy-noether-ja/releases/download/noether-ja-2026-11-15-r2/03-noether-ja-base-sources.zip) |
| 校訂本文：編集上の訂正を適用し、各訂正の理由を編集注で説明します | [PDF、427頁](https://github.com/KokunoYumeto/emmy-noether-ja/releases/download/noether-ja-2026-11-15-r2/04-noether-ja-emendations.pdf) | [LaTeX](https://github.com/KokunoYumeto/emmy-noether-ja/releases/download/noether-ja-2026-11-15-r2/05-noether-ja-emendations.tex) | [ZIP](https://github.com/KokunoYumeto/emmy-noether-ja/releases/download/noether-ja-2026-11-15-r2/06-noether-ja-emendations-sources.zip) |

[SHA-256 一覧](https://github.com/KokunoYumeto/emmy-noether-ja/releases/download/noether-ja-2026-11-15-r2/07-noether-ja-SHA256SUMS.txt)。同じファイルは [`editions/2026-10-24-r2/ja/`](editions/2026-10-24-r2/ja/) にもあります。

各 LaTeX ファイルには、その本文のすべてのソースファイルがプリアンブルとともに収録されています。Python プログラム [`build.py`](editions/2026-10-24-r2/ja/build.py) がそれらを展開し、XeLaTeX で組版して、各 PDF を読む順序で結合します。Python 3、pypdf、および各プリアンブルに指定された TeX パッケージとフォントが必要です。ZIP には同じソースが元の構成のまま、組版プログラムとともに収録されています。

2026年8月13日の日本語版 r10 は [`reader/`](reader/)（PDF）と [`source/`](source/)（LaTeX）にあり、その記録は [`evidence/`](evidence/) と [`release/`](release/) にあります。[リリース ja-r10-20260813](https://github.com/KokunoYumeto/emmy-noether-ja/releases/tag/ja-r10-20260813) からも入手できます。ドイツ語本文、他の言語の版、版の間の既知の相違は[中央ページ](https://kokunoyumeto.github.io/emmy-noether/)にまとめられています。

## 原著者と出典

- 原著者は Emmy Noether および各著作に記載された共著者です：Werner Schmeidler（論文17）、R. Brauer（論文32）、R. Brauer と H. Hasse（論文38）。1929/30年の講義は M. Deuring が筆録しました。著作45は H. Kapferer の論文で、E. Noether との共著による補遺が付いています。各著作の原刊情報、署名および引用は本文に記載されています。
- 底本：日本語版2026-08-13 r10（Manuscript Typesetting Project / OpenAI Codex、[リリース ja-r10-20260813](https://github.com/KokunoYumeto/emmy-noether-ja/releases/tag/ja-r10-20260813)）とドイツ語版 ED0014/v051。数式は、原刊と頁ごとに照合したドイツ語本文（[noether-de-2026-10-26](https://github.com/KokunoYumeto/modern-latex-manuscripts/releases/tag/noether-de-2026-10-26)）に従います。
- [旧版の権利表示](editions/2026-10-24/ja/reader-edition/NOTICE_HISTORIQUE.md)

## 権利

エミー・ネーターは1935年に没したため、その著作は欧州連合および保護期間が著作者の死後70年で終わるすべての国・地域でパブリックドメインにある。米国では、1931年以降に初めて公表された論文は公表後95年まで保護される（1931年の論文は2027年1月1日に自由になる）。AIが作成した翻訳・修正・組版について発行者が権利を有する範囲で、その権利は[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.ja)によりパブリックドメインに供される。M. Deuringが記録した講義、H. Kapfererの論文、および明記された共著者の寄与はこの表示の対象外であり、その権利は著作者またはその相続人に留まる。