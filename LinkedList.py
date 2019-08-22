__author__ = "Frank Shen"

'''
LList
prepend append popLeft remove find len 
'''


class Node(object):
    def __init__(self, elem=None, next_=None):
        self.elem = elem
        self.next = next_


class LinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.length = 0
        self._tail = None

    def __len__(self):
        return self.length

    def is_empty(self):
        return self._tail is None

    def append(self, elem):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')
        if self._tail is None:
            self.root.next = Node(elem)
            self._tail = self.root.next
        else:
            self._tail.next = Node(elem)
            self._tail = self._tail.next
        self.length += 1

    def prepend(self, elem):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')
        head = self.root.next
        if self._tail is None:
            self.root.next = Node(elem, head)
            self._tail = self.root.next
        else:
            self.root.next = Node(elem, head)
        self.length += 1

    def _iter_node(self):
        node = self.root.next
        while node is not None:
            yield node
            node = node.next

    def __iter__(self):
        for node in self._iter_node():
            yield node.elem

    def find(self, elem):
        index = 0
        for node in self._iter_node():
            if node.elem == elem:
                return index
            index += 1
        return -1

    def pop_left(self):
        if self._tail is None:
            raise Exception('Empty')
        head = self.root.next
        if self.root.next is self._tail:
            self.root.next = head.next
            self._tail = self.root.next
        else:
            self.root.next = head.next
        self.length -= 1
        return head.elem

    def remove(self, elem):
        prev = self.root
        for node in self._iter_node():
            if node.elem == elem:
                prev.next = node.next
                if node is self._tail:
                    self._tail = prev
                self.length -= 1
                return node.elem
            prev = node
        return None

    def clear(self):
        for node in self._iter_node():
            node = None
        self.root.next = None
        self._tail = self.root.next
        self.length = 0


def test_linked_list():

    l = LinkedList(4)
    l.append(1)
    l.append(2)
    l.append(3)
    l.prepend(0)
    assert len(l) == 4
    assert l.find(3) == 3
    assert l.find(2) == 2
    l.pop_left()
    assert [i for i in l] == [1, 2, 3]
    assert len(l) == 3
    assert l.find(0) == -1
    assert l.remove(2) == 2
    l.remove(2)
    assert [i for i in l] == [1, 3]
    assert l.find(3) == 1
    l.clear()
    assert len(l) == 0
    assert l.is_empty() is True
    l.append(1)
    l.append(2)
    l.append(3)
    l.prepend(0)
    assert len(l) == 4
    assert l.find(3) == 3
    assert l.find(2) == 2
    l.pop_left()
    assert [i for i in l] == [1, 2, 3]
    assert len(l) == 3
    assert l.find(0) == -1
    assert l.remove(2) == 2
    l.remove(2)
    assert [i for i in l] == [1, 3]
    assert l.find(3) == 1


test_linked_list()
