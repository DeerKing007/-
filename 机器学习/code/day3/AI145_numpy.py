import numpy as np
#print(np.ones((200,300))) # 用1填充矩阵
#print(np.zeros(5)) # 用0填充矩阵
#nd=np.array([[1,2],[3,4],[5,6]],ndmin=2,dtype=np.int8) # object:list ndmin指定最小维度  dtype指定元素的类型(int,float)
# print([[1,2],[3,4]])
#print(nd)
# print(type(nd))
# print(nd.T) # 转置
#nd.dtype=np.int16 改变数组中元素的类型
#print(nd)
#print(nd.shape)  #(2, 2) 查看数组的形状
#nd.shape=(4,4) # 修改数组的形状 要求元素个数不能改变
#print(nd.size) # 查看元素个数
# nd.size=8  #！！！！错误 不能修改
# print(nd.ndim) #查看数组的维度
# 方法
#print(nd.sum(axis=1)) #不指定轴 ,求所有元素的和  0轴把每列元素求和  1把每一行的元素求和
#print(nd.max(axis=1))#不指定轴 ,求所有元素的最大值  0轴求每列的最大值  1把每行的最大值
#print(nd.min(axis=1))#不指定轴 ,求所有元素的最小值  0轴求每列的最小值  1把每行的最小值
#print(nd.mean(axis=1))#不指定轴 ,求所有元素的平均值  0轴求每列的平均值  1把每行的平均值 自动转为float
#print(nd.std(axis=1))# 求标准差  方差的开方
#print(nd.var(axis=1))# 求方差  表示数据的离散程度
#nd1=np.array([[2,2],[3,4]])
#print((nd==nd1).all())  # 做两个矩阵的对比  会对比每个元素 返回一个结果矩阵 当结果所有元素都为True的时候，才返回True
# print(nd.cumsum())  # 求累和
# print(nd.prod(axis=0)) # 求乘积
# print(nd.cumprod())  # 求累乘
#print(nd.argmax()) # 返回最大值的索引 所有元素方入一维数组中以后再查索引
#print(nd.argmin()) # 返回最小值的索引 所有元素方入一维数组中以后再查索引
#print(nd.reshape((2,2))) # 和shape属性的用法类似 有返回值 不作用于原数组
#nd.resize(4) # 改变原数组的元素个数 直接作用于原数组 没有返回值 如果元素个数不够，填充0
#print(nd.reshape((2,2)))
#print(nd)
#print(nd.swapaxes(0,1)) # 交换轴的位置
# 切片
nd=np.array([[1,2],[3,4]],ndmin=2,dtype=np.int8)
#print(nd[0:2]) # ,逗号分隔  第一个切片切行 第二个切片切列 全要用： 一个切片默认切行
#print(nd[1]) # 取出某一行数据
#print(nd[:,0]) # 取出某一列
nd1=np.array([[1,2]],ndmin=2,dtype=np.int8)
#print(nd+nd1) # 矩阵做加减法 直接做
#print(nd*nd1) # 两个矩阵直接乘  对位元素做了乘法
#print(nd1.dot(nd)) # 矩阵的乘法（按照矩阵的乘法规则）
#print(np.dot(nd1,nd)) # 矩阵乘法 第一个矩阵在前