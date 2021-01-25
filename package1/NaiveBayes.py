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

except_words = ["アメリカ", "投票", "大統領", "結果", "指示", "民主党", "共和党", 
                '失言', '嫌い', '世界', '副大統領', '個人的', '対応', '討論会', '議論',
                '印象', '記事', '政治', '当選',
                '明らか', '選挙結果', '数カ月',
                '政権', 'ディベート', '勝利', '選挙', 'コロナ', '大統領選挙'] # ここに入れた単語が除外される


def corpus_list(word_list): # corpusを作成する関数
    corpus = []
    num = 0
    for text in word_list:
        for word in text[:len(text)]:
            if (num == 0):
                if not(word in except_words):
                    temp = word
                    num += 1
            else:
                if not(word in except_words):
                    temp += (" " + word)
        num = 0
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
            ans = result[0][2] / 1.5
        else:
            ans = -(result[0][2] / 1.5)
    if (abs(ans) > 0.5):
        return (ans / abs(ans)) * 0.5
    else:
        return ans


def get_scoreX(word_list): # トランプ派かバイデン派かのスコアを返す関数
    x = 0
    x_list = np.array([0.4403539418449606, -0.5])  # NBのテストデータでの最大値と最小値
    
    corpus = corpus_list(word_list)
    wc = cv.transform(corpus)
    wc_array = wc.toarray()
    
    for i in range(len(wc_array)):
        x += define_x(clf_model.predict_proba(wc_array[i:i+1]))
    x /= len(wc_array)
    x_list = np.append(x_list, [x])
    x_std1 = (x - x_list.min()) / (x_list.max() - x_list.min())
    x_scaled = x_std1 * 2 - 1
    if x_scaled > 0:
        x_scaled -= 0.45
    else:
        x_scaled += 0.45
    x_std2 = (x_scaled + 0.55) / 1.1
    return x_std2 * 2 - 1