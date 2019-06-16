import pandas as pd
table=pd.read_csv(r'E:\AI145\机器学习\资料·\adult.txt',sep=',',usecols=(14,)) # 第一行会被当做列名
table.columns=['result']
#print(table)
#print(table.head(5)) # 查看前五行数据
#print(table.tail(5)) # 查看后五行数据
# table.columns=['age','workclass','fnlwgt','education','education-num','marital-status','occupation',
#                'relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country'
#                ] # 修改列名
#print(table[0:2]) # 取两行值
#print(table['age']) # 取一列值
# print(table.age) # 取一列值
# 取单行数据或者多行数据
#print(table.loc[0:2])  loc取值按照索引来取  行索引就是给绑定的下标 列索引是列名
#print(table.loc[0:2,'age':'fnlwgt']) # 取限定行，限定列的数据 注意列给列名
#print(table.loc[[0,2],['age','fnlwgt']])
#print(table.at[0,'age']) # 快速取值
# 以下标取值 行列都可以给下标
#print(table.iloc[0:2,0:2])
#print(table.iloc[[0,2],[0,2]])
#print(table.T) # 转置
#print(table.describe()) # 返回对数据的描述
#print(table.max()) # 数字直接比较大小 字母按照a-z的顺序比较每个字符
#print(table.sort_values(by=['age','hours-per-week'],inplace=True)) # inplace是否作用于原列表
#print(table['native-country'].drop_duplicates())
table[table['result'].str.strip()=='<=50K']=0  #.str可以把一列值当做字符串来处理
table[table['result'].str.strip()=='>50K']=1
print(table)