__author__ = "Frank Shen"


class Node(object):
    def __init__(self, elem=None, next_=None, prev=None):
        self.elem = elem
        self.next = next_
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

    def _tail(self):
        return self.root.prev

    def _head(self):
        return self.root.next

    def append(self, elem):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')
        node = Node(elem)
        tail = self._tail()
        tail.next = node
        node.prev = tail

        self.root.prev = node
        node.next = self.root
        self.length += 1

        # tail.next = Node(value, self.root, self.tail)

    def prepend(self, elem):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')
        node = Node(elem)

        if self.root.next is self.root:
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            head = self._head()
            node.prev = self.root
            self.root.next = node
            node.next = head
            head.prev = node
        self.length += 1

    def remove(self, node):  # O(1)  node
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def _iter_node(self):
        if self.root.next is self.root:
            return
        p = self.root.next
        while p.next is not self.root:
            yield p
            p = p.next
        yield p

    def __iter__(self):
        for node in self._iter_node():
            yield node.elem

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return
        p = self.root.prev
        while p.next is not self.root:
            yield p
            p = p.prev
        yield p


def test_double_linked_list():
    a = CircularDoubleLinkedList()
    a.append(1)
    a.append(2)
    a.append(3)
    a.prepend(0)
    print(len(a))
    for elem in a:
        print(elem)
    for node in a.iter_node_reverse():
        print(node.elem)


test_double_linked_list()
