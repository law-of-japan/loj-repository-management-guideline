# -*- coding: utf-8 -*-
from more_itertools import chunked
import numpy

def textToInt(string):
    if len(string) > 8:
        print("ERROR! chunked string length must be shorter than 8")
    elif len(string) < 8:
        string += "0"*(8-len(string))
    res_int = 0
    lis = list(string)
    for i in range(0, len(lis)):
        if lis[i] == "1":
            res_int += 2**i
        elif lis[i] == "0":
            pass
        else:
            pass
    return res_int

ordinances = [
"|0|陸軍省|甲||",
"|1|大蔵省|||",
"|2|農商務省|||",
"|3|海軍省|||",
"|4|逓信省||第一次|",
"|5|内務省|||",
"|6|陸軍省|乙||",
"|7|文部省|||",
"|8|司法省|丙||",
"|9|司法省|甲||",
"|10|外務省|||",
"|11|陸軍省|||",
"|12|司法省|||",
"|13|拓殖務省|||",
"|14|宮内省|||",
"|15|鉄道省|||",
"|16|農林省||第一次|",
"|17|拓務省|||",
"|18|商工省||第一次|",
"|19|厚生省|||",
"|20|大東亜省|||",
"|21|運輸通信省|||",
"|22|軍需省|||",
"|23|農商省|||",
"|24|運輸省|||",
"|25|農林省||第二次|",
"|26|商工省||第二次|",
"|27|第一復員省|||",
"|28|第二復員省|||",
"|29|逓信省||第二次|",
"|30|総理庁|||",
"|31|労働省|||",
"|32|法務庁|||",
"|33|建設省|||",
"|34|通商産業省|||",
"|35|総理府|||",
"|36|法務府|||",
"|37|経済安定本部|||",
"|38|電気通信省|||",
"|39|物価庁|||",
"|40|海上保安庁|||",
"|41|郵政省|||",
"|42|電波監理委員会||規則|",
"|43|法務省|||",
"|44|自治省|||",
"|45|農林水産省|||",
"|46|内閣府|||",
"|47|総務省|||",
"|48|財務省|||",
"|49|文部科学省|||",
"|50|厚生労働省|||",
"|51|経済産業省|||",
"|52|国土交通省|||",
"|53|環境省|||",
"|54|防衛省|||",
]

"""
このスクリプトは、府省令のレポジトリ名に使用される、対象機関を示すキーを作成するためのユーティリティです。

スクリプトを開始すると、以下のように表示されます。

['|0|陸軍省|甲||', '|1|大蔵省|||', '|2|農商務省|||', '|3|海軍省|||', '|4|逓信省||第一次|', '|5|内務省|||', '|6|陸軍省|乙||', '|7|文部省|||']
input binary like this: 01001010 >>>

機関の名前が並んで表示されますので、それぞれ順に、あてはまるなら1、あてはまらないなら0を入力してください。
例えば上の、'|4|逓信省||第一次|'は、第一次逓信省のときのみ有効にし、第二次逓信省のときは有効にしないよう注意してください。
例）大蔵省令の場合
01000000

例）大蔵省、農商務省令の場合
01100000

これと同じような質問が数回繰り返されますので、それぞれ答えてください。
最後に、英数字の文字列が表示されます。それがキーになりますのでリポジトリ名に含めてください。
リポジトリ名は、日付-ministerialOrdinance-キー-府省令番号のような形式です。
詳細はCONTRIBUTING.mdを参照してください。
"""
if __name__ == "__main__":
    result_int = 0
    chunked_list = list(chunked(ordinances, 8))

    for i in range(0, len(chunked_list)):
        print(chunked_list[i])
        user_input = input("input binary like this: 01001010 >>>")
        result_int += textToInt(user_input) << i*8
    print(numpy.base_repr(result_int, 36))
