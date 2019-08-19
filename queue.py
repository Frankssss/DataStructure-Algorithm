__author__ = "Frank Shen"

'''
queue (FIFO)
push pop
'''

class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.length = 0
        self.root = Node()
        self.tailNode = None

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')
        node = Node(value=value)
        tailNode = self.tailNode
        if tailNode is None:
            self.root.next = node
        else:
            self.tailNode.next = node
        self.tailNode = node
        self.length += 1

    def appendLeft(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')
        node = Node(value=value)
        headNode = self.root.next
        self.root.next = node
        node.next = headNode.next
        self.length += 1

    def iterNode(self):
        curNode = self.root.next
        while curNode is not self.tailNode:
            yield curNode
            curNode = curNode.next
        if curNode is not None:
            yield curNode

    def __iter__(self):
        for node in self.iterNode():
            yield node.value

    def remove(self, value):  # O(n)
        prevNode = self.root
        for curNode in self.iterNode():
            if curNode.value == value:
                prevNode.next = curNode.next
                if curNode is self.tailNode:
                    self.tailNode = prevNode
                del curNode
                self.length -= 1
                return 1
            prevNode = curNode
        return -1

    def find(self, value):
        index = 0
        for node in self.iterNode():
            if node.value == value:
                return index
            index += 1
        return -1

    def popleft(self):
        if self.tailNode is None:
            raise Exception('Empty')
        headNode = self.root.next
        self.root.next = headNode.next
        self.length -= 1
        value = headNode.value
        del headNode
        return value

    def clear(self):
        for node in self.iterNode():
            del node
        self.root.next = None
        self.tailNode = None
        self.length = 0


class Queue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_linked_list = LinkedList()

    def __len__(self):
        return len(self._item_linked_list)

    def push(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')
        return self._item_linked_list.append(value)

    def pop(self):
        if len(self) <= 0:
            raise Exception('Empty')
        return self._item_linked_list.popleft()


def test_queue():
    q = Queue()
    q.push(0)
    q.push(1)
    q.push(2)
    print(q.pop())
    print(q.pop())
    print(len(q))


test_queue()