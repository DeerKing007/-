import pandas as pd
result=[]
with open(r'E:\AI145\机器学习\资料·\adult_test.txt')as r:
    for line in r.readlines():
        if '?' not in line:
            result.append(line.strip())
with open(r'E:\AI145\机器学习\资料·\new_adult_test.txt','w')as w:
    w.write('\n'.join(result))