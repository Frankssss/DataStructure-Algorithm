__author__ = "Frank Shen"

'''
图, 简单的说就是由节点（node）和边（edge）组成的一种数据结构
图分为有向图和无向图
'''

'''
遍历图的两种方式
BFS(广度优先搜索)
DFS(深度优先搜索)
'''

from collections import deque

# 邻接表
GRAPH = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D'],
}

# FIFO


class Queue(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.popleft()

    def __len__(self):
        return len(self._deque)


def bfs(graph, start):
    search_queue = Queue()
    search_queue.push(start)
    searched = set()
    while search_queue:
        cur_node = search_queue.pop()
        if cur_node not in searched:
            print(cur_node)
            searched.add(cur_node)
            for node in graph[cur_node]:
                search_queue.push(node)


bfs(GRAPH, 'A')


DFS_SEARCHED = set()


def dfs(graph, start):
    if start not in DFS_SEARCHED:
        print(start)
        DFS_SEARCHED.add(start)
    for node in graph[start]:
        if node not in DFS_SEARCHED:
            dfs(graph, node)


# dfs(GRAPH, 'A')