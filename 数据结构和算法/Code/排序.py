import random
import requests
requests.session().post()
# 选择冒泡 自己看
# 快排
# def kuaipai(l):
#     # 当列表中只有一个元素的时候 递归收敛
#     if len(l)<=1:
#         return l
#     # 找基准元素
#     k=l[-1]
#     # 将比基本元素小的元素放到它的左边，比它大的元素放到右边  相同元素另存
#     left=[i for i in l if i<k]
#     right = [i for i in l if i >= k]
#     deng = [i for i in l if i == k]
#     # 再对左右两个小数组进行快排
#     left=kuaipai(left)
#     right=kuaipai(right)
#     return left+deng+right
#
#
#



# def quick_sort(qlist):
#     if qlist == []:
#         return []
#     else:
#         qfirst = qlist[0]
#         qless = quick_sort([l for l in qlist[1:] if l < qfirst])
#         qmore = quick_sort([m f0or m in qlist[1:] if m >= qfirst])
#     return qless + [qfirst] + qmore
array=[4,5,6,7,3,2,6,9,8]
# quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
# print(quick_sort(array))
#  归并排序
def guibing(l):
    if len(l)<=1:
        return l
    #print(l)
    left=guibing(l[:(len(l))//2]) # 左边数组
    right=guibing(l[(len(l))// 2:])  # 右边数组

    return hebing(left,right)

def hebing(l1,l2):
    l1_index=l2_index=0
    r=[]
    while l1_index<len(l1) and l2_index<len(l2):
        if l1[l1_index]<=l2[l2_index]:
            r.append(l1[l1_index])
            l1_index+=1
        else:
            r.append(l2[l2_index])
            l2_index+=1
    return r+l1[l1_index:]+l2[l2_index:]

if __name__ == '__main__':
    l = list(range(11))
    random.shuffle(l)
    print(l)
   # l=[2,3,6,4,5,6]
    l=guibing(l)
    print(l)