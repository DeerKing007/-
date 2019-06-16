import numpy.linalg as lg # 科学计算包
import numpy as np
#A=np.mat('1,2,3;4,5,6')
#A=np.mat('1 2 3 ;4 5 6') # 把字符串转为矩阵
A=np.array([[1,1],[1,1]])
#print(lg.eigvals(A)) # 求A的特征值
#print(A)
# X,Y=lg.eig(A) # 特征值与特征向量(按列对应)
# print(X)
#print(A.dot(Y[0:,0]))
# print(Y[0:,0]*X[0])
# A*x=B 求解x
a = np.array([[3,1], [1,2]])
b = np.array([9, 8])
x = lg.solve(a, b)
print(x)