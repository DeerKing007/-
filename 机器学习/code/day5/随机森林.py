# 使用sk-learn开发随机森林算法
import pandas
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split  # 拆分测试集与训练集
filepath = r"E:\AI145\机器学习\资料·\dating.txt"
X=pandas.read_csv(filepath,usecols=[0,1,2],sep='\t') # 通用方法，将数据加载为一个二维数组 usecols选择读取哪些列
Y=pandas.read_csv(filepath,usecols=(3,),sep='\t') # 通用方法，将数据加载为一个二维数组 usecols选择读取哪些列
#X=MinMaxScaler().fit_transform(X)
rf=RandomForestClassifier(n_estimators=300)
for i in range(10):
    tarin_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.1)
    rf.fit(tarin_x,train_y)
    print(rf.score(test_x,test_y))
#knn.predict() # 预测x对应的y