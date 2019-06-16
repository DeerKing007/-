# 1.	垃圾邮件和正常邮件的内容有区别
# 2.	每个邮件中出现的单词次数不一样


# 5.	构建目标变量 选择模型进行训练
# 6.	评估模型
# 7.	如果模型的效果不好—优化：增大数据集  调整超参数  换模型  特征选择 检查代码逻辑
import os
from collections import Counter
import numpy as np
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
# 3.	获取所有邮件中出现的前3000个常见单词
def load_datas(filepaths, tingyong):
    result = []  # 保存所有邮件中的词
    # 获取所有文件的绝对路径
    files = [os.path.join(filepaths, f) for f in os.listdir(filepaths)]
    # 读取每个文件，获取文件中的单词
    words = []
    for f in files:
        f_words = []
        # 将文件中的所有单词放入到同一个列表中
        with open(f)as r:
            # 遍历文件中所有词，去除非数字和字符的词，停用词
            for word in r.read().split():
                if word.isalpha() and word not in tingyong and len(word) > 1:
                    f_words.append(word) # 保存文件中出现的所需要的单词
                    words.append(word) # 抽取特征
        result.append(f_words)
    return list(dict(Counter(words).most_common(3000)).keys()),result


# 根据常用词构建特征矩阵，样本是邮件 特征值是单词在邮件中出现的次数
def get_X(words, result):
    X=np.zeros((len(result),len(words)))
    for y,word in enumerate(words):
        for x,f_words in enumerate(result):
            X[x][y]=f_words.count(word)  # 给特征矩阵赋值
    return X
if __name__ == '__main__':
    train_filepaths = r'E:\AI145\机器学习\资料·\email\train-mails'
    test_filepaths = r'E:\AI145\机器学习\资料·\email\test-mails'
    tingyong = ['is', 'are']
    words,result = load_datas(train_filepaths, tingyong)
    print(words)
    test_words, test_result = load_datas(test_filepaths, tingyong)
    X=get_X(words,result)
    test_X=get_X(words,test_result) # 和训练集使用同一个特征矩阵
    Y=np.zeros(702)
    Y[0:351]=1  # 1是正常邮件 0代表垃圾邮件
    test_Y = np.zeros(260)
    test_Y[0:130] = 1  # 1是正常邮件 0代表垃圾邮件
    nb=GaussianNB()
    nb.fit(X,Y)
    print(nb.score(test_X,test_Y))