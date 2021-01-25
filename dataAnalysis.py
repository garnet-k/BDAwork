from package1 import MorphologicalAnalysis as ma
from package1 import NaiveBayes as nb
from package1 import SentimentAnalysis as sa
from package1 import TextFormatting as tf

import datetime
import pandas as pd

class DataAnalysis: # データを分析するクラス
    word_noun = [] # 形態素解析をした名詞を入れる配列
    word_nva  = [] # 形態素解析をした名詞、動詞、形容詞を入れる配列

    def __init__(self, comment):
        self.text_list = comment
        

    def parser(self): # 形態素解析をする
        for text in self.text_list:
            tmp = ma.parse2df(text)
            self.word_noun.append(ma.get_noun(tmp))
            self.word_nva.append(ma.get_nva(tmp))


    def tb_classification(self): # トランプ派かバイデン派かのスコアを返す
        return nb.get_scoreX(self.word_noun)


    def emotion_classification(self): # 感情分析のスコアを返す
        return sa.get_scoreY(self.word_nva)



if __name__ == "__main__":
    df = pd.read_csv('BDAdata/comment.csv')
    df = df.drop('num', axis = 1)
    
    # サーバー側からアンケートの結果を入れる配列
    questionnaire = ["私はトランプを支持する。", "私はトランプを支持しない。","私はバイデンを支持する", "私はバイデンを支持しない。"] 
    
    comment = []
    for text in questionnaire:
        comment.append(tf.text_formatting(text))

    da = DataAnalysis(comment)
    da.parser()
    
    dt_now = datetime.datetime.now()
    date = str(dt_now.year) + "/" + str(dt_now.month) + "/" + str(dt_now.day)
    name = "test"
    job  = "student"
    score_x = da.tb_classification()
    score_y = da.emotion_classification()
    
    list2 = [[date, name, job, "", "your comment", "", 0, score_x, score_y]]
    columns2 = ["date", "name", "job", "label", "comment", "url", "topic", "x", "y"]
    df2 = pd.DataFrame(data = list2, columns = columns2)
    df = df.append(df2)

    print(df) # 確認用
    df.to_csv('BDAdata/data.csv') # サーバー側に送るcsvファイル
