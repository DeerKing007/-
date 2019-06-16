import jieba
# 分3类
texts=['今天天气很好', # 0
       '我今天找到对象了', # 1
       '程序员要面向对象编程', # 2
       '程序员不能有对象', # 2
       '我今天不想做程序员了' # 1
       ]
for t in texts:
    print(list(jieba.cut(t)))
