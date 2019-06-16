from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer # 对文本做特征处理
import jieba
# ['今天天气', '很', '好']
# ['我', '今天', '找到', '对象', '了']
# ['程序员', '要', '面向对象编程']
# ['程序员', '不能', '有', '对象']
# ['我', '今天', '不想', '做', '程序员', '了']
texts=['今天天气很好', # 0   2
       '我今天找到对象了', # 1  1
       '程序员要面向对象编程', # 2  0
       '程序员不能有对象', # 2   0
       '我今天不想做程序员了' # 1  1
       ]
def get_txet(text):
    return jieba.cut(text)
tf=TfidfVectorizer(tokenizer=get_txet)
X=tf.fit_transform(texts)
db=DBSCAN(min_samples=1,eps=1.05)
print(db.fit_predict(X))
