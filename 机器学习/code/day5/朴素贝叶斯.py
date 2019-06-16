# 使用sk-learn开发朴素贝叶斯算法
import pandas
from sklearn.preprocessing import MinMaxScaler # 归一化的类
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
#GaussianNB 高斯贝叶斯  符合高斯分布  常用
#MultinomialNB 多项式贝叶斯 符合多项式分布
#BernoulliNB 伯努利贝叶斯 符合伯努利分布
from sklearn.model_selection import train_test_split  # 拆分测试集与训练集
filepath = r"E:\AI145\机器学习\资料·\dating.txt"
X=pandas.read_csv(filepath,usecols=[0,1,2],sep='\t') # 通用方法，将数据加载为一个二维数组 usecols选择读取哪些列
Y=pandas.read_csv(filepath,usecols=(3,),sep='\t') # 通用方法，将数据加载为一个二维数组 usecols选择读取哪些列
X=MinMaxScaler().fit_transform(X)
nb=GaussianNB()
for i in range(10):
    tarin_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.1)
    nb.fit(tarin_x,train_y)
    print(nb.score(test_x,test_y))
#knn.predict() # 预测x对应的y