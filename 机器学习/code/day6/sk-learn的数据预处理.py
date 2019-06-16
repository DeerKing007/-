from sklearn.preprocessing import LabelEncoder,StandardScaler # 标签编码器 对一个列表中不同值的元素进行编码
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier,RandomForestClassifier
def a(x,le):
    return le.fit_transform(x)
data=pd.read_csv(r'E:\AI145\机器学习\资料·\adult.txt',sep=',',usecols=range(15))
test_data=pd.read_csv(r'E:\AI145\机器学习\资料·\adult_test.txt',sep=',',usecols=range(15))
train_X=data.drop([' <=50K'],axis=1) # 去掉特定行或者列
test_X=test_data.drop([' <=50K.'],axis=1) # 去掉特定行或者列
train_Y=data[' <=50K']
test_Y=test_data[' <=50K.']
le = LabelEncoder()
train_X=train_X.apply(a,axis=0,args=(le,)) # 把train_X的每一列都作用于a方法
train_Y=le.fit_transform(train_Y)
test_X=test_X.apply(a,axis=0,args=(le,)) # 把train_X的每一列都作用于a方法
test_Y=le.fit_transform(test_Y) # 把train_X的每一列都作用于a方法
# ss=StandardScaler()
# train_X=ss.fit_transform(train_X)
# test_X=ss.fit_transform(test_X)
nb=SVC()
print(train_X)
# train_X.apply()
nb.fit(train_X,train_Y)
print(nb.score(test_X,test_Y))
