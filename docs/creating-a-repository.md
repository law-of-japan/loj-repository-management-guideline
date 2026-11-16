# 法令リポジトリを作るとき

新しい法令を登録し、法令リポジトリを作るときに確かめてほしい規則です。参加する前に、[CONTRIBUTING.md](../CONTRIBUTING.md)を読んでください。従来の形式の既存のリポジトリについては、[従来の形式の既存のリポジトリを移すとき](migrating-legacy-repositories.md)を参照してください。

## リポジトリの名称

- 法令リポジトリは、一つのRecord（法令）につき一つです（HIST-01）。
- リポジトリの名称は、そのRecordのRecord IDと同じにします。仕様は、法令リポジトリの所在を登録台帳のRecordの`repository`で解決し、リポジトリの名称を参照の解決に使いません（RID-03）。このプロジェクトでは、Recordとリポジトリを見分けやすくするために、名称をRecord IDに揃えます。
- リポジトリを移転・改名したときは、登録台帳のRecordの`repository`を更新します（REG-02）。
- Record IDは、登録の管理主体が発行するランダムな文字列で、Crockford Base32の小文字（`0-9a-hjkmnp-tv-z`。`i`、`l`、`o`、`u`を除く）10文字です（RID-01、RID-02）。番号・日付・種別・題名からRecord IDを作ってはいけません。
- 発行するときは、登録台帳でこれまでに発行したすべてのID（撤回・統合・分割したIDと別名を含む）と、大小文字を区別せずに衝突しないことを確かめます（RID-01）。

以上に従えば、リポジトリの名称は以下の例のようになります。
> 3kq8vz0hmt

法令の題名と法令番号は、リポジトリのDescription、README.md、登録台帳のRecordの`label`で示します。リポジトリのDescriptionには、その法令の名称、通称、法令番号をコンマ&スペース区切りで列挙するものとします。これらは表示のためのものであり、参照の解決には使いません（RID-03）。

## リポジトリの作成

1. 登録台帳のリポジトリに、そのRecordのファイル`records/<Record ID>.yaml`を作り、`repository`に法令リポジトリの場所と正本ブランチ（`main`）を書きます（REG-01、REG-02）。番号主張や外部識別子は、原典で確かめた根拠と共に記録します（REG-03、REG-05）。
2. 法令リポジトリを、Record IDと同じ名称で作成します。初めにGitHubのリポジトリ作成機能によってREADME.mdのみを作成し、規定のブランチを`main`にします。これを起点のコミットとして、作業ブランチを切ってください（[コミットし、マージするとき](committing-and-merging.md)）。

本文を収録しない法令（改正法等）で、関係の起点になるだけのものは、登録台帳への登録だけでよく、法令リポジトリを作らなくてかまいません。

## ファイル構成

法令リポジトリは、次の構成とします（HIST-01）。

```text
<法令リポジトリ>/
  README.md                    # その法令の基礎情報（表示用）
  history.yaml                 # 履歴マニフェスト
  rebuild.yaml                 # 再構築報告（既存のリポジトリから移したRecordだけ）
  versions/
    <revision_id>/             # 版（Revision）ごとのディレクトリ
      law.yaml                 # 版パッケージのManifest（loj/v1alpha2）
      main.md                  # 本則
      supplement.md            # 附則
      glyphs.yaml              # 字体注記（注記がある場合）
```

- history.yaml
  - その法令の履歴（版の一覧、その法令を改正・廃止する関係、収録範囲、効力の終了）を記録するファイルです。
- versions/&lt;revision_id&gt;/
  - 一つの版（法令のある時点の状態）につき一つのディレクトリを作り、その版の本文を置きます。版のディレクトリは、history.yamlの版と一対一に対応させます。
  - revision_idは、版ごとにランダムに発行する、Crockford Base32の小文字8文字の識別子です（REV-01）。施行日や改正法の番号から作ってはいけません。ディレクトリ名はrevision_idとし、表示用のラベル（`label`）を直しても改名しません（REV-03）。
  - 版の単位は「一つの施行時点 × 一つの改正法令」です（REV-04）。
- law.yaml、本文のMarkdown
  - 版パッケージです。本文のファイルは`law.yaml`の`documents`に読み込む順に列挙します（MAN-01〜03）。
  - ファイルの分け方は任意ですが、本則を`main.md`に、附則を`supplement.md`（附則が複数ある場合はkeyごとのファイル）にまとめることを基本とします。従来の`chapterX.md`のような章ごとのファイル分割やディレクトリによる分類は、求めません。
- glyphs.yaml
  - 字体注記です。注記する字がある版にだけ置き、`law.yaml`の`documents`には列挙しません（GLYPH-01）。
- rebuild.yaml
  - 既存のリポジトリから原典による再構築で移したRecordにだけ置く、作業の記録です。
- README.md
  - 表示のための基礎情報です。README.mdの内容を、参照の解決や同一性の判断に使ってはいけません。

本文を収録していない法令で法令リポジトリを持つ場合は、`history.yaml`だけを置き、`versions/`を置かなくてかまいません（HIST-01）。

完全な例として、仕様の適合ケースの正例（[hist-001](https://github.com/law-of-japan/loj-spec/tree/main/conformance/loj-history/v1alpha1/valid/hist-001/repo)、国民の祝日に関する法律）を参照してください。

各ファイルの書き方は、[本文・データを書くとき](writing-data.md)を参照してください。
