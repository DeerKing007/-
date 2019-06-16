# 使用sk-learn开发线性回归算法
import pandas
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler # 归一化的类
from sklearn.linear_model import LogisticRegression # 逻辑回归
from sklearn.model_selection import train_test_split  # 拆分测试集与训练集
filepath = r"E:\AI145\机器学习\资料·\dating.txt"
X=pandas.read_csv(filepath,usecols=[0,1,2],sep='\t') # 通用方法，将数据加载为一个二维数组 usecols选择读取哪些列
Y=pandas.read_csv(filepath,usecols=(3,),sep='\t') # 通用方法，将数据加载为一个二维数组 usecols选择读取哪些列
X=MinMaxScaler().fit_transform(X)
lr=LogisticRegression()
for i in range(10):
    tarin_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.1)
    lr.fit(tarin_x,train_y)
    print(lr.score(test_x,test_y))
#knn.predict() # 预测x对应的y