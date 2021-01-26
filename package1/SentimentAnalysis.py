"""
感情分析
"""

import pandas as pd
import numpy as np

df_dic = pd.read_csv('modelData/polar_dictionary.csv') # 極性辞書

def get_scoreY(word_list): # 感情分析のスコアを返す関数
    y = 0
    y_list = np.array([-9.622200773328238, 2.095296998796651]) # 感情分析のスコアの最大値と最小値
    for text in word_list:
        y_tmp = 0
        for word in text:
            try:
                tmp = df_dic[df_dic['word'] == word].score
                y_tmp += list(tmp)[0]
            except:
                continue
        if (len(text) != 0):
            y += y_tmp / len(text)
        else:
            y += y_tmp
    y /= len(word_list)
    y_list = np.append(y_list, [y])
    y_std = (y - y_list.min()) / (y_list.max() - y_list.min())
    return y_std * 2 - 1