# 1.	加载数据集  分开特征矩阵和目标向量
# 2.    处理特征矩阵，将所有元素归一化到0-1之间  (除以每一列最大值)
# 3.	给定一个新样本 计算新样本到每个样本之间的距离 保存到距离数组中
# 4.	将距离排序，取出前k个距离最小(近)的样本
# 5.	统计取出样本的每个类别出现的次数
# 6.	把出现次数最多的那个类别作为新数据的类别
from collections import Counter
def load(filepath):
    # 返回特征矩阵(二维数组)和目标向量（一维数组）
    X = []
    Y = []
    with open(filepath)as r:
        for line in r.readlines():
            words = line.split('\t')
            X.append([float(words[0]),float(words[1]),float(words[2])])
            Y.append(words[-1].strip())
    return X, Y

def guiyihua(X):
    #找到每一列最大值
    max1=max2=max3=0
    # 找到所有最大值
    for x in X:
        if x[0]>max1:
            max1=x[0]
        if x[1] > max2:
            max2 = x[1]
        if x[2]>max3:
            max3=x[2]
    result=[]
    #将所有元素分别除以该列的最大值
    for x in X:
        result.append([x[0]/max1,x[1]/max2,x[2]/max3])
    return result

def get_dis(x, X):
    dis = []
    for old_x in X:
        dis.append(
            ((x[0] - old_x[0]) ** 2 + (x[1] - old_x[1]) ** 2 + (x[2] -old_x[2]) ** 2) ** 0.5)
    return dis


def get_class(dis, Y, k):
    new_dis = sorted(dis)[0:k]
    r=[]
    for d in new_dis:
        r.append(Y[dis.index(d)])
    return Counter(r).most_common(1)[0][0]
if __name__ == '__main__':
    #x=[48111,9.134528,0.728045]	#3
    #x = [43757, 7.882601, 1.332446]  # 3
    filepath = r"E:\AI145\机器学习\资料·\dating.txt"
    X, Y = load(filepath)
    X=guiyihua(X)
    test_X=X[0:100]
    tarin_X=X[100:]
    sum=0
    for i,x in enumerate(test_X):
        dis = get_dis(x, tarin_X)
        c=get_class(dis,Y[100:],5)
        if c==Y[i]:
            sum+=1
    print(sum)