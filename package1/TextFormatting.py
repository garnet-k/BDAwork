"""
テキスト整形
"""

import emoji
import re

def text_formatting(text):
    text = re.sub(r"。", "。\n", text)   #文(「。」）毎に改行
    text = re.sub(r"…", "", text)  #…を削除
    text = re.sub(r"→", "", text)  #→を削除
    text = re.sub(r'[︰-＠]', "", text) #全角記号を削除
    text = re.sub(r'[【.+?】]', "", text) #【】を削除
    text = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)", "" ,text) # urlを削除
    text = re.sub(r"#(\w+)", "", text) # ハッシュタグの削除
    text = re.sub(r'@[a-zA-Z]+', '', text) #＠ユーザ名を削除
    text = text.lower() # 英語を小文字に
    text = ''.join(['' if c in emoji.UNICODE_EMOJI else c for c in text]) # 絵文字の削除
    return text