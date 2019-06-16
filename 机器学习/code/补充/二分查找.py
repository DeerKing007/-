


# 是否存在
def search(l ,key):
    # 4、重复2-3步，直到找到或者数组（切过的数组）中没有值
    if len(l)<=1:
        return False
    # 1、每次访问中间值
    mid = len(l) // 2
    print(mid,l[mid])
    # 2、如果中间值大于关键字，到起始值以及中间值之间查找
    if l[mid]>key :  # 地板除得到整数
        return search(l[:mid],key)
    # 3、如果中间值小于关键字，到中间值以及终止值之间查找
    elif l[mid]<key:
        return search(l[mid:],key)
    # 当中间值等于关键字的时候 返回
    else:
        return True
# 找到返回下标 找不到False
def search1(l ,key,beg,end):
    # 4、重复2-3步，直到找到或者数组（切过的数组）中没有值
    if beg>=end:
        return False
    # 1、每次访问中间值
    mid = (beg+end) // 2
    # 2、如果中间值大于关键字，到起始值以及中间值之间查找
    if l[mid]>key :  # 地板除得到整数
        return search1(l,key,beg,mid)
    # 3、如果中间值小于关键字，到中间值以及终止值之间查找
    elif l[mid]<key:
        return search1(l,key,mid,end)
    # 当中间值等于关键字的时候 返回
    else:
        return mid


if __name__ == '__main__':
    import time
    import numpy as np
    #print(np.log2(100000000))
    l= range(10000000000)
    key = 500
    # time1=time.time()
    # for i in l:
    #     if i==key:
    #         print(l.index(i))
    time2=time.time()
    print(search1(l, key,0,len(l)-1))
    #print(time2-time1)
    print(time.time()-time2)