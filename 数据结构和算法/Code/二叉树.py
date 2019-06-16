# 二叉树代码实现思路：
# Class Node：
#       属性：item，左子树，右子树
# Class Tree：
#       属性：根节点
#       方法：添加节点方法
#       遍历树的方法
class Node(object):
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None
class Tree(object):
    def __init__(self):
        self.root=None

    def add(self,item):
        node=Node(item)
        # 1. 判断根节点是否存在  不存在  添加
        if not self.root:
            self.root=node
            return
        # 2. 存在 将根节点添加到待访问队列
        q=[self.root]
        # 6. 重复3-5步
        while True:
            # 3. 从带访问队列中取出一个节点
            cur_node=q.pop(0)
            # 4. 判断其左右子树是否为空 为空 添加
            if not cur_node.left:
                cur_node.left=node
                return
            if not cur_node.right:
                cur_node.right = node
                return
            # 5. 将左右子树添加到带访问队列
            q.append(cur_node.left)
            q.append(cur_node.right)
    # 先序遍历 先访问根节点 再访问左子树，右子树  深度优先
    def xianxu(self,node):
        if not node:
            return []
        # 访问左子树
        left=self.xianxu(node.left)
        # 访问右子树
        right=self.xianxu(node.right)
        return [node]+left+right
    # 中序遍历 先访问左子树 再访问根节点,右子树
    def zhongxu(self,node):
        if not node:
            return []
        left=self.zhongxu(node.left)
        right = self.zhongxu(node.right)
        return left+[node]+right
    # 后序遍历 先访问左子树 再访问根节点,右子树
    def houxu(self,node):
        if not node:
            return []
        left=self.houxu(node.left)
        right = self.houxu(node.right)
        return left+right+[node]
    def cengci(self):
        # 如果根节点为空 返回空列表
        if not self.root:
            return []
        q=[self.root]
        result=[]
        while q:
            cur_node=q.pop(0)
            result.append(cur_node)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        return result

if __name__ == '__main__':
    t=Tree()
    for i in range(1,16):
        t.add(i)
    l=t.cengci()
    for n in l:
        print(n.item,end=' ')
