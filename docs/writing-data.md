# 本文・データを書くとき

本文、`law.yaml`、`history.yaml`、`glyphs.yaml`等を書くときに確かめてほしい規則です。参加する前に、[CONTRIBUTING.md](../CONTRIBUTING.md)を読んでください。ファイルの置き場所は、[法令リポジトリを作るとき](creating-a-repository.md#ファイル構成)を参照してください。

## 各ファイルの内容と書式

各ファイルは、それぞれのschemaVersionの仕様に従って書いてください。

| ファイル | schemaVersion | 仕様 |
|---|---|---|
| `law.yaml`と本文のMarkdown | `loj/v1alpha2` | [loj/v1alpha2](https://github.com/law-of-japan/loj-spec/blob/main/spec/v1alpha2/01-overview.md) |
| `history.yaml` | `loj-history/v1alpha1` | [loj-history/v1alpha1](https://github.com/law-of-japan/loj-spec/blob/main/spec/loj-history/v1alpha1/01-history.md) |
| `glyphs.yaml` | `loj-glyphs/v1alpha1` | [loj-glyphs/v1alpha1](https://github.com/law-of-japan/loj-spec/blob/main/spec/loj-glyphs/v1alpha1/01-glyphs.md) |
| `rebuild.yaml` | `loj-rebuild/v1alpha1` | [loj-rebuild/v1alpha1](https://github.com/law-of-japan/loj-spec/blob/main/spec/loj-rebuild/v1alpha1/01-rebuild.md) |

`law.yaml`と本文のMarkdownの例は、`loj/v1alpha2`の[祝日法の制定時の版](https://github.com/law-of-japan/loj-spec/tree/main/conformance/loj-history/v1alpha1/valid/hist-001/repo/versions/98mj5vgx)を参照してください。履歴マニフェスト・字体注記・再構築報告を含む構成は、[法令リポジトリ全体の例](https://github.com/law-of-japan/loj-spec/tree/main/conformance/loj-history/v1alpha1/valid/hist-001/repo)で確認できます。

本文のMarkdownについて、注意すべきことは以下です。詳細と、以下にない事項は仕様に従ってください。

- 本文は、原典資料から起こします（[原典資料](#原典資料)）。字体の根拠は、公布された本文（官報と官報正誤）です（GLYPH-07）。[文字保存方針](../CONTRIBUTING.md#文字保存方針)に従い、旧字体や踊り字も原典どおりとします。
- すべてのファイルは改行で終了する（BASIC-02）。
- 編・章・節・款・目・条は、Headingを用いて「第一章　総則」「第一条（目的）」のように原文のラベルで記述する（HEAD-01）。Headingのレベルは表示上の深さであり、所属は見出しのラベルで決まります。
- 項・号・細分は、Ordered listやUnordered listではなく、HTMLコメントのマーカー（`<!-- loj:paragraph number=1 -->`等）で記述する（DIR-01）。
- 無番号の項、表、前文、制定文は、それぞれの構造（PARA-01、TABLE-01〜03、PRE-01〜02）で記述する。表を箇条書きで書くことはしません（BASIC-03）。
- 公布文、御名御璽、署名は、版の本文に含めない（BASIC-03）。
- 改正法の附則は、被改正法令の版に含めない。被改正法令の版には、その法令自身の本則と附則（改正で加えられた部分を含む）だけを記述する（BASIC-03）。改正法の附則のうち施行期日や経過措置は、history.yamlの関係の根拠として参照します（HIST-03）。
- 仕様で表現できない構造を含む場合は、`law.yaml`の`unsupportedFeatures`に記録する（BASIC-03）。

## 原典資料

版の本文は、公布された本文（官報と官報正誤）から起こします（GLYPH-07）。原典資料は、以下の優先順位をもって選択するものとします。

1. 官報と官報正誤
2. 御署名原本（[国立公文書館_デジタルアーカイブ](https://www.digital.archives.go.jp)）。官報を入手できない場合に限ります。この場合は、history.yamlの`text.glyphCheck`を`unverified`とし、官報を入手した時点で照合します（REB-05）。

[衆議院_制定法律](https://www.shugiin.go.jp/Internet/itdb_housei.nsf/html/housei/menu.htm)のページやe-Govの本文は、作業の手がかりとして使えますが、版の本文や字体の根拠にはしません。衆議院_制定法律ページにはOCRの都合による誤字があり、e-Govの本文は新字体に置き換えられているためです。官報も御署名原本も入手できない改正の版は、本文のない版（`text.status: absent`）として記録します（REB-05）。

従来の形式の既存のリポジトリの本文（旧本文）を下書きにするときは、[旧本文を下書きにするとき](migrating-legacy-repositories.md#旧本文を下書きにするとき)を参照してください。

それぞれのシステムに全文が記載されているかどうかは、[日本法令索引](https://hourei.ndl.go.jp/)を用いて確認することができる。

## 文字の扱い

[文字保存方針](../CONTRIBUTING.md#文字保存方針)は、仕様の文字の要件（CHAR-01〜05）と字体注記（GLYPH-01〜11）で具体化されています。両者に矛盾はありません。方針で「別途定めます」とした事項のうち、次は仕様で定めました。

- 方針の各項目は、CHAR-01（コードポイント列の保持、正規化の禁止）、CHAR-02（字体の自動変換と踊り字の展開の禁止）、CHAR-03（異体字セレクタ）、CHAR-04（決められない字と判読困難な字）、CHAR-05（派生処理の分離）に対応します。
- 判読困難な字、Unicodeで表せない字、対応を決められない字は、本文に〓（U+3013）を置くか、決めた字を置いたうえで、版ごとの`glyphs.yaml`に注記します（GLYPH-02、GLYPH-03）。私用領域の文字やU+FFFD、画像を本文に置いてはいけません。
- コードポイントの選び方は、GLYPH-06に従います。統合漢字とCJK互換漢字のどちらに当たるか決められない場合は、統合漢字を置いて`ambiguous`として注記し、互換漢字を推測で選びません。
- 本文の中のCJK互換漢字と異体字セレクタ付きの字には、すべて注記を付けます（GLYPH-11）。正規化による変化を検出できるようにするためです。
- 踊り字は原典に印刷された記号のまま転記します（GLYPH-08）。原典の中で消して書き直した箇所は、訂正後の字句を本文に置き、訂正を注記します（GLYPH-09）。
- 字体の根拠は、公布された本文（官報と官報正誤）です。官報で決められない字に限り、ほかの原典資料（御署名原本等）で確かめます（GLYPH-07）。
- 原典の字体と照合したかどうかは、history.yamlの`text.glyphCheck`（`verified`／`unverified`）で示します。注記がないことを、原典どおりであることの根拠にはしません（GLYPH-10）。
- 既存データの移行手順は、[旧リポジトリから原典による再構築への移行の手順](https://github.com/law-of-japan/loj-spec/blob/main/docs/migration-from-legacy.md)で定めました。既存の本文は取り込まず、原典から作り直します（REB-03）。

原典照合の文字単位の比較規則と、派生処理の仕様は、引き続き未決定です。

原典の表記を記録するデータ（`law.yaml`の`law.number`、登録台帳の番号主張の`raw`、時点値の`raw`等）は、原典の表記をそのまま記録します（CHAR-01、REG-03、TIME-02）。コミットメッセージ等での[法令番号の表記の統一](committing-and-merging.md#法令番号の漢数字での表記)は、これらのデータには適用しません。

## 未施行の法令がある場合の取り扱い

- 未施行の改正を、別のブランチ（従来の`not_entered_into_force`ブランチ）で表すことはやめます。未施行の改正も、mainブランチの`history.yaml`に一つの版として記録します。
- 施行日が確定している場合は、その日付を施行時点（`effective`）に`state: date`で記録します。
- 「政令で定める日」のように施行日が法令上まだ定まっていない場合は、施行時点を`state: pending`とし、定め方の原文を`raw`に、委任先・条件を`delegation`に記録します（TIME-01、TIME-04）。このような版も登録できます（REV-04）。
- 施行期日政令等で施行日が確定した場合は、施行時点を`state: date`に改め、確定前の定め方を`delegation`に残し、確定させた根拠を`determinedBy`に記録します（TIME-04）。確定前の値を消してはいけません。このとき、revision_idは変えません（REV-01）。この変更の種類は`metadata`です。
- 施行は、ブランチの進め方では表しません。`history`ブランチ等の派生ビューは、施行日が確定している版をその日の到来によって加えることができますが、期日未確定・条件付き・併存する版を自動で進めることはしません（VIEW-06）。

## 参照の書き方

### 参照の種類

法令やその版を指し示すときは、仕様の参照の形式を使います（FIXREF-01）。

| 種類 | 指すもの | 用途 |
|---|---|---|
| Record参照 | 法令そのもの | 法令を指す |
| Revision参照 | 法令のある状態（版） | 「この法令のこの状態」を指す。記録訂正等で指す内容が変わり得る |
| 固定参照 | 版の記録版（正本のコミット） | 引用・検証の対象になった本文・根拠を固定する |

- データ（history.yaml、glyphs.yaml、登録台帳等）の中では、構造化形式（RecordRef、RevisionRef、FixedRef）で書きます。版をrevision_idで指し、表示用のラベルや施行日で指してはいけません（FIXREF-01）。
- データの外（Issue、PR、文書、外部サイト等）で引用するときは、次の文字列表記を使います（FIXREF-02）。`<space>`は登録空間の識別子です。

  ```text
  loj:<space>/<record>/<revision>                 # Revision参照
  loj:<space>/<record>/<revision>@<commit>        # 固定参照
  loj:<space>/<record>/<revision>@<commit>#<node> # 固定参照とノード
  ```

- 固定参照の`<commit>`は、正本ブランチ（`main`）から到達できるコミットの完全なハッシュとします。短縮形、ブランチ名、タグ名は使えません（FIXREF-04）。作業ブランチのコミットは固定参照に使えません。
- 条などのノードを指せるのは、固定参照だけです。Revision参照にノードを付けてはいけません（FIXREF-07）。
- GitHub等のURLは、参照を解決した結果の一つにすぎません。URLを参照そのものとして案内しないでください（FIXREF-02）。
- `history`ブランチのタグはRevision参照として扱い、`history`ブランチのコミットを固定参照として案内してはいけません（VIEW-04）。

既存のリポジトリの旧コミットや`blob/master/…`へのリンクの扱いは、[従来のリンク](migrating-legacy-repositories.md#従来のリンク)を参照してください。

### 本文の中のリンク

- 従来は、本文の「第ｘ条」や「○○法」の部分にリンクを付加していましたが、これをやめます。法令の中の参照の構文（L2）は、仕様の将来の版で定められます（REF-01）。それまでは、本文に新しいリンクを付加しません。
- 原典から本文を起こすときは、旧リポジトリのリンクを含め、原典にないものを本文に持ち込みません。
