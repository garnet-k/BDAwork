"""
形態素解析
"""

from natto import MeCab
import pandas as pd 

stop_word = [] # ストップワード

f = open('BDAdata/stop_words.txt', 'r')
text = f.read()
text = text.split("\n")
for tmp in text:
    stop_word.append(tmp)
f.close()


def parse2df(text, sysdic = "/usr/local/lib/mecab/dic/mecab-ipadic-neologd"):
    df = pd.DataFrame(index=[], columns=['文番号','表層', '品詞1','品詞2','品詞3','品詞4','原型','posID'])
    
    text = text.split("\n") #改行で分割して配列にする
    while '' in text: #空行は削除
        text.remove('')
    
    parser = MeCab("-d "+sysdic)

    for index,sentence in enumerate(text): 
        nodes = parser.parse(sentence,as_nodes=True)
        for node in nodes:
            if not node.is_eos():
                #品詞情報を分割
                feature = node.feature.split(',')
                #dataframeに追加
                series = pd.Series( [
                    index,          #文番号
                    node.surface,   #表層
                    feature[0],     #品詞1
                    feature[1],     #品詞2     
                    feature[2],     #品詞3
                    feature[3],     #品詞4
                    feature[6],     #原型
                    node.posid      #品詞番号
                ], index=df.columns)
                df = df.append(series, ignore_index = True)
    return df


def get_noun(df, stop_words = stop_word): # 名詞のみ取り出す
    """
    形態素解析をした結果から、名詞だけを取り出す
    　動詞を加えるなら、31,32,33
    　形容詞を加えるなら、10,11,12
    　副詞を加えるなら、34,35
    を加える
    名詞だけでいいかはよくわかっていないがよさそうに思える
    """
    text_list = []
    df2 = df[df["posID"].isin([36,37,38,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,67])] # 名詞のみ
    df2 = df2[~df2["原型"].isin(stop_words)]
    for row in df2.iterrows():
        if row[1]["原型"] == "*":
            if row[1]["posID"] != 36:
                text_list.append(row[1]["表層"])
        else:
            if row[1]["原型"] == "ドナルド・トランプ":
                text_list.append("トランプ")
            elif row[1]["原型"] == "トランプ大統領":
                text_list.append("トランプ")
                text_list.append("大統領")
            elif row[1]["原型"] == "隠れトランプ":
                text_list.append("トランプ")
                #text_list.append("隠れトランプ")
            elif row[1]["原型"] == "米国":
                text_list.append("アメリカ")
            elif row[1]["原型"] == "米" and row[1]["品詞4"] == "国":
                text_list.append("アメリカ")
            elif row[1]["原型"] == "アメリカメディア":
                text_list.append("アメリカ")
                text_list.append("メディア")
            elif row[1]["原型"] == "大統領選":
                text_list.append("大統領選挙")
            elif row[1]["原型"] == "アメリカ大統領選挙":
                text_list.append("アメリカ")
                text_list.append("大統領選挙")
            elif row[1]["原型"] == "ジョージ・ブッシュ":
                text_list.append("ブッシュ")
            elif row[1]["原型"] == "ブッシュ大統領":
                text_list.append("ブッシュ")
                text_list.append("大統領")
            else:
                text_list.append(row[1]["原型"])
                
    return text_list


def get_nva(df, stop_words = stop_word): # 名詞、動詞、形容詞を取り出す
    """
    形態素解析をした結果から、名詞、動詞、形容詞を取り出す
    """
    text_list = []
    df2 = df[df["posID"].isin([36,37,38,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,67,31,32,33,10,11,12])] 
    df2 = df2[~df2["原型"].isin(stop_words)]
    for row in df2.iterrows():
        if row[1]["原型"] == "*":
            if row[1]["posID"] != 36:
                text_list.append(row[1]["表層"])
        else:
            if row[1]["原型"] == "ドナルド・トランプ":
                text_list.append("トランプ")
            elif row[1]["原型"] == "トランプ大統領":
                text_list.append("トランプ")
                text_list.append("大統領")
            elif row[1]["原型"] == "隠れトランプ":
                text_list.append("トランプ")
                #text_list.append("隠れトランプ")
            elif row[1]["原型"] == "米国":
                text_list.append("アメリカ")
            elif row[1]["原型"] == "米" and row[1]["品詞4"] == "国":
                text_list.append("アメリカ")
            elif row[1]["原型"] == "アメリカメディア":
                text_list.append("アメリカ")
                text_list.append("メディア")
            elif row[1]["原型"] == "大統領選":
                text_list.append("大統領選挙")
            elif row[1]["原型"] == "アメリカ大統領選挙":
                text_list.append("アメリカ")
                text_list.append("大統領選挙")
            elif row[1]["原型"] == "ジョージ・ブッシュ":
                text_list.append("ブッシュ")
            elif row[1]["原型"] == "ブッシュ大統領":
                text_list.append("ブッシュ")
                text_list.append("大統領")
            else:
                text_list.append(row[1]["原型"])
                
    return text_list