__author__ = "Frank Shen"


'''
树结构是一种包含节点（node）和边(edge)的拥有层级关系的一种结构
根节点(root)：树的最上层节点
路径(path)： 从起始节点到终止节点经历过的边
父亲（parent）: 除了根节点，每个节点的上一层边链接的节点就是它的父亲
孩子（children）：每个节点由边指向的下一层节点
兄弟（siblings）:同一个父亲并且处在同一层的节点
子树(subtree): 每个节点包含它所有的后代组成的子树
叶子节点（leaf node): 没有孩子的节点
'''

'''
二叉树
每个节最多只能包含两个孩子
节点深度 depth： 节点对应的level数字
树的高度 height: level+1
树的宽度 width: 包含对多节点的层级的节点树
数的size： 二叉树的节点总个数
'''

'''
满二叉树： 如果每个内部节点（非叶节点）都包含两个孩子， 就成为满二叉树
完美二叉树： 当所有的叶子节点都在同一层就是完美二叉树，毫无间隙填充了h层
完全二叉树： 1、叶子结点只可能在层次最大的两层上出现；2、前k-1层中的结点都是“满”的，且第 k 层的结点都集中在左边
'''

'''
先序遍历： 先处理根， 之后是左子树， 然后是右子树
中序遍历： 先处理左子树， 之后是根，然后是右子树
后序遍历； 先处理左子树，之后是右子树，最后是跟
'''
from collections import deque


class Queue(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.popleft()

    def __len__(self):
        return len(self._deque)


class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinTree(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)

    def perorder_trav(self, subtree):
        if subtree is not None:
            print(subtree.data)
            self.perorder_trav(subtree.left)
            self.perorder_trav(subtree.right)

    def inorder_trav(self, subtree):
        if subtree is not None:
            self.inorder_trav(subtree.left)
            print(subtree.data)
            self.inorder_trav(subtree.right)

    def postorder_trav(self, subtree):
        if subtree is not None:
            self.postorder_trav(subtree.left)
            self.postorder_trav(subtree.right)
            print(subtree.data)

    def levelorder_trav(self, subtree):
        if subtree is not None:
            q = Queue()
            q.push(subtree)
            while q:
                node = q.pop()
                print(node.data)
                if node.left:
                    q.push(node.left)
                if node.right:
                    q.push(node.right)


node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]


btree = BinTree.build_from(node_list)
# btree.perorder_trav(btree.root)
# btree.inorder_trav(btree.root)
# btree.postorder_trav(btree.root)
# btree.levelorder_trav(btree.root)