# BDAwork
ナイーブベイズによる分類と感情分析をする。
docker上で動作することを確認。

## BDAdata
- comment.csv : 事前に解析したコメントのデータ。

- data.csv : サーバー側から受け取ったコメントを解析したものを加えたデータ。

- stop_words.txt : ストップワード。

著作権の関係から公開していない

## modelData
- clf_model.pickle : 作成したナイーブベイズのモデル

- count_vectorizer.pickle : 作成したcountVectorizerのモデル

- polar_dictionary.csv : 作成した極性辞書

## package1 
- MorphologicalAnalysis.py : 形態素解析に関する関数

- NaiveBayes.py : ナイーブベイズに関する関数

- SentimentAnalysis.py : 感情分析に関する関数

- TextFormatting.py : テキスト整形に関する関数

## dataAnalysis.py
- DataAnalysis : データを分析するクラス
