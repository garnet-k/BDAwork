"""
感情分析
"""

import pandas as pd
import numpy as np

df_dic = pd.read_csv('modelData/polar_dictionary.csv') # 極性辞書

def get_scoreY(word_list): # 感情分析のスコアを返す関数
    y = 0
    y_list = np.array([-0.14892710197126388, 0.4472879118982551]) # 感情分析のスコアの最大値と最小値
    if len(word_list) == 0:
        return 0
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
    if y == 0:
        return 0.0
    y_list = np.append(y_list, [y])
    y_std = (y - y_list.min()) / (y_list.max() - y_list.min())
    
    print("len", len(word_list))
    print(" y ", y)
    print("y_std", y_std)
    print("min", y_list.min())
    print("max", y_list.max())
    
    return y_std * 2 - 1