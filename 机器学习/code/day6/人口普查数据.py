from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
import pandas as pd
import numpy as np
# 将所有非数值的列处理为数字
def get_X(X):
    # 1. 遍历每一列
    result={}
    for c in X.columns:
    # 2. 取出每列中不重复的类别
        index=0
        for d in X[c].drop_duplicates():
    # 3. 把每个列中不重复类别分别赋值为一个数字(自增索引)
            X[c][X[c]==d]=index
            result[c+d]=index # 数据字典
            index+=1
    return X,result
data=pd.read_csv(r'E:\AI145\机器学习\资料·\new_adult.txt',sep=',',usecols=range(15))
test_data=pd.read_csv(r'E:\AI145\机器学习\资料·\new_adult_test.txt',sep=',',usecols=range(15))
train_X=data.drop([' <=50K',' 12345678901'],axis=1) # 去掉特定行或者列
test_X=test_data.drop([' <=50K.',' 226802'],axis=1) # 去掉特定行或者列
tarin_Y=data[' <=50K']
test_Y=test_data[' <=50K.']
#print(tarin_Y.name) # 查看列名
tarin_Y[tarin_Y.str.strip()=='<=50K']=0  #.str可以把一列值当做字符串来处理
tarin_Y[tarin_Y.str.strip()=='>50K']=1
test_Y[test_Y.str.strip()=='<=50K.']=0  #.str可以把一列值当做字符串来处理
test_Y[test_Y.str.strip()=='>50K.']=1
train_X,result=get_X(train_X)
tarin_X=pd.DataFrame(train_X,dtype=np.int64)
#test_X=pd.DataFrame(get_X(test_X),dtype=np.int64)
tarin_Y=pd.Series(tarin_Y,dtype=np.int64)
test_Y=pd.Series(test_Y,dtype=np.int64)
nb=MultinomialNB()
nb.fit(train_X,tarin_Y)
print(nb.score(test_X,test_Y))