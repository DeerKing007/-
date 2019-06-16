from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas
from sklearn.datasets import load_iris
from sklearn import datasets
# 鸢尾花数据集
# filepath = r"E:\AI145\机器学习\资料·\dating.txt"
# X=pandas.read_csv(filepath,usecols=[0,1,2],sep='\t') # 通用方法，将数据加载为一个二维数组 usecols选择读取哪些列
# Y=pandas.read_csv(filepath,usecols=(3,),sep='\t') # 通用方法，将数据加载为一个二维数组 usecols选择读取哪些列
datas=load_iris()
dt=DecisionTreeClassifier()
for i in range(10):
    tarin_x,test_x,train_y,test_y=train_test_split(datas.data,datas.target,test_size=0.1)
    dt.fit(tarin_x,train_y)
    print(dt.score(test_x,test_y))
#knn.predict() # 预测x对应的y