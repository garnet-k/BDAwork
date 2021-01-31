"""
ナイーブベイズ
"""

import pickle 
import numpy as np

f = open('modelData/clf_model.pickle', 'rb')
clf_model = pickle.load(f) # ナイーブベイズのロード
f.close()
f = open('modelData/count_vectorizer.pickle', 'rb')
cv = pickle.load(f)        # countVectorizerのロード
f.close()

except_words = ['アメリカ', 'バイデン', 'トランプ', '投票', '大統領', '結果', '指示', '民主党', '共和党',
                '副大統領', 'コロナ', 'ヒラリー', '優勢', '世界', '個人的', '影響', '陣営', '相手', 
                '討論会', '大統領選挙', '再選', '分断', '完全', '外交', '息子', '理由', '当選', '白人', 
                '記事', '可能性', '比較', '英語', '追記', 'コメント', '候補', '批判', '対応','支持', 
                '黒人'] # ここに入れた単語が除外される


def corpus_list(word_list): # corpusを作成する関数
    corpus = []
    temp = ""
    for text in word_list:
        temp = ""
        for word in text[:len(text)]:
            if not(word in except_words):
                temp += (" " + word)
        corpus.append(temp)
    return corpus


def define_x (result): # ナイーブベイズの確率からスコアを定義する関数
    ans = 0
    if (result[0][0] > result[0][1]) and (result[0][0] >= result[0][2]): # トランプ
        ans = result[0][0]
    elif (result[0][1] > result[0][0]) and (result[0][1] >= result[0][2]): # バイデン
        ans = -result[0][1]
    else:
        if result[0][0] > result[0][1]:
            ans = result[0][2] / 4.0
        else:
            ans = -(result[0][2] / 4.0)
    return ans


def get_scoreX(word_list): # トランプ派かバイデン派かのスコアを返す関数
    x = 0
    
    corpus = corpus_list(word_list)
    wc = cv.transform(corpus)
    wc_array = wc.toarray()
    
    for i in range(len(wc_array)):
        x += define_x(clf_model.predict_proba(wc_array[i:i+1]))
        
    if (len(wc_array) == 0):
        return 0
    else:
        x /= len(wc_array)
        
    return x