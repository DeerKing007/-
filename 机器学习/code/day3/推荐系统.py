import numpy as np
items=['Item1',  'Item2', 'Item3',  'Item4' , 'Item5',  'Item6']
k = 3
n = 2
# 1.	加载数据
users_items = np.array([[5, 3, 0, 0, 1, 5],
                        [0, 5, 2, 0, 0, 5],
                        [0, 2, 0, 5, 0, 0],
                        [5, 2, 5, 0, 0, 5],
                        [0, 0, 5, 2, 5, 0],
                        [0, 5, 2, 5, 0, 0]])
user1 = users_items[0]
# 2.	计算用户之间的距离   1. 欧式距离  2.余弦距离  3.杰卡德距离 计算两个集合之间的距离  交集/并集
dis = []  # 距离数组
for user in users_items:
    # 1. ((user1-user)*(user1-user)).sum()
    # 2. sum=0
    # for i in range(len(user)):
    #     (sum+=(user1[i]-user[i])**2)**0.5
    dis.append(np.sqrt((user1 - user).dot((user1 - user).T)))  # sqrt(n)  对n做开方
# 3.	取距离最近的前k个用户
users = np.array([users_items[dis.index(d)] for d in sorted(dis)if d != 0][0:k])
# 4.	求k个用户对所有商品的平均评分
scores=users.mean(axis=0)
# 5.	过滤掉用户已经消费过的商品
#new_scores=[scores[user1.tolist().index(u)] for u in user1 if u==0]  #user1.tolist()转成python list对象
new_scores=[]
for i,u in enumerate(user1):
    if u==0:
        new_scores.append(scores[i])
# 6.	取出平均评分最高的前n个商品或者取出所有满足阈值的商品
new_scores=sorted(new_scores,reverse=True)[0:n]
index=[]
for i,s in enumerate(scores):
    if s in new_scores:
        index.append(i)
# 7.	输出所有取到的商品
for i in index:
    if user1[i]==0:
        print(items[i])