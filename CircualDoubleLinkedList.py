__author__ = "Frank Shen"


class Node(object):
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class CircularDoubleLinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def tailNode(self):
        return self.root.prev

    def headNode(self):
        return self.root.next

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')
        node = Node(value=value)
        tailNode = self.tailNode()

        tailNode.next = node
        node.prev = tailNode

        self.root.prev = node
        node.next = self.root
        self.length += 1

    def appendLeft(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')
        node = Node(value=value)

        if self.root.next is self.root:
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            headNode = self.headNode()
            node.prev = self.root
            self.root.next = node
            node.next = headNode
            headNode.prev = node
        self.length += 1

    def remove(self, node):  # O(1)  node
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iterNode(self):
        if self.root.next is self.root:
            return
        curNode = self.root.next
        while curNode.next is not self.root:
            yield curNode
            curNode = curNode.next
        yield curNode

    def __iter__(self):
        for node in self.iterNode():
            yield node.value

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return
        curNode = self.root.prev
        while curNode.next is not self.root:
            yield curNode
            curNode = curNode.prev
        yield curNode


def test_double_linked_list():
    a = CircularDoubleLinkedList()
    a.append(0)
    a.append(1)
    a.append(2)
    a.append(3)
    a.appendLeft(5)
    print(len(a))
    for node in a:
        print(node)


test_double_linked_list()
