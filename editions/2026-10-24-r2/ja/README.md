# エミー・ネーター — 数学著作集・日本語版

論文1–43、M. Deuringが筆記した1929/30年の講義、KapfererとNoetherの論文および補遺、書誌と巻末一覧を収録します。

## How this was made: AI's failure modes, and what we do about them

Everything here was produced by AI. The translation was made in a first pass mostly by GPT-5.6 Sol (OpenAI Codex,
reasoning effort ultra), by the user's account (July and August 2026). Its formulas were then brought into line with the German text, which Claude Opus 5.5 at
effort max compared page by page with Noether's printed originals (785 page checks, 26 October 2026), in automatic and
hand rounds by Claude Opus 5.5 at effort max (26-27 October; 2,570 lines in the last hand round), against the known
failures of AI translation of mathematics: renamed letters, formulas changed or dropped, statements narrowed, passages
reworked or garbled, sentences and displays dropped, broken layout. Every change passes a release filter, and every PDF
is checked for lines running into the margin (Claude Opus 5.5 at effort high, 15 November). No person has reviewed the
translation. What was done in each round, the measured figures and what is still open:
[How this was made](https://github.com/KokunoYumeto/emmy-noether#how-this-was-made-ais-failure-modes-and-what-we-do-about-them).

## 底本の本文

1. [PDF](https://github.com/KokunoYumeto/emmy-noether-ja/releases/download/noether-ja-2026-11-15-r2/01-noether-ja-base.pdf)
2. [編集可能なLaTeXソース](https://github.com/KokunoYumeto/emmy-noether-ja/releases/download/noether-ja-2026-11-15-r2/02-noether-ja-base.tex)
3. [ソース一式](https://github.com/KokunoYumeto/emmy-noether-ja/releases/download/noether-ja-2026-11-15-r2/03-noether-ja-base-sources.zip)

## 校訂を含む本文

1. [PDF](https://github.com/KokunoYumeto/emmy-noether-ja/releases/download/noether-ja-2026-11-15-r2/04-noether-ja-emendations.pdf)
2. [編集可能なLaTeXソース](https://github.com/KokunoYumeto/emmy-noether-ja/releases/download/noether-ja-2026-11-15-r2/05-noether-ja-emendations.tex)
3. [ソース一式](https://github.com/KokunoYumeto/emmy-noether-ja/releases/download/noether-ja-2026-11-15-r2/06-noether-ja-emendations-sources.zip)

原著者はEmmy Noetherおよび各作品に記載する共著者である。講義録はM. Deuringの筆録による。日本語訳はAIによる翻訳。初版の制作主体はManuscript Typesetting Project / OpenAI Codexであり、当時の正確なモデルは現存する来歴資料からは確定していない。本版のAIによる訂正・組版：OpenAI Codex — GPT-6 Astra、Ultra。発行者による人間の翻訳または学術的査読を示すものではない。

底本：[日本語版2026-08-13 r10](https://github.com/KokunoYumeto/emmy-noether-ja/releases/tag/ja-r10-20260813)、ドイツ語版ED0014/v051。各作品の原刊情報、署名および引用は本文に記載する。

継承した翻訳は、ユーザーの説明によれば、主に GPT-5.6 Sol（OpenAI Codex、推論設定 ultra）が行いました。 AIによる訂正・組版：2026年10月23–24日；Claude Opus 5.5（Anthropic、推論設定 max）、2026年10月26–27日（数式は Noether の印刷ページから読んだドイツ語本文と照合）。刊行日：2026年10月27日。

直接入手できる累積LaTeXには、各本文とプリアンブルが編集可能なコードとして収録されています。付属のPythonプログラムで元のファイル構成を展開し、XeLaTeXで組版した各PDFを読む順序で結合します。画像やPDFページを翻刻の代わりには用いません。ZIPには元の構成、同じ累積LaTeX、組版プログラムを収録しています。Python 3、pypdf、および各プリアンブルに指定されたTeXパッケージとフォントが必要です。TeXとフォントの版によってPDFのバイト列は変わる場合があります。固定された内部組版日は刊行日ではありません。

[Python](build.py) · [SHA-256](07-noether-ja-SHA256SUMS.txt)

組版プログラムはAI作成：OpenAI Codex — GPT-6 Astra、Ultra、2026年10月24日。

## 著者・来歴・権利

エミー・ネーターは1935年に没したため、その著作は欧州連合および保護期間が著作者の死後70年で終わるすべての国・地域でパブリックドメインにある。米国では、1931年以降に初めて公表された論文は公表後95年まで保護される（1931年の論文は2027年1月1日に自由になる）。AIが作成した翻訳・修正・組版について発行者が権利を有する範囲で、その権利は[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.ja)によりパブリックドメインに供される。M. Deuringが記録した講義、H. Kapfererの論文、および明記された共著者の寄与はこの表示の対象外であり、その権利は著作者またはその相続人に留まる。

[権利者からの申し立て](https://github.com/KokunoYumeto/emmy-noether-ja/issues/new).

## 以前の版

[GitHub](https://github.com/KokunoYumeto/emmy-noether-ja/releases).
