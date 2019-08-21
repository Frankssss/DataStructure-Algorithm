__author__ = "Frank Shen"

'''
LList
prepend append popLeft find len 
'''


class Node(object):
    def __init__(self, elem=None, next_=None):
        self.elem = elem
        self.next_ = next_


class LinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self._tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def is_empty(self):
        return len(self) == 0

    def append(self, elem):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('Full')
        if self._tail is None:
            self.root.next_ = Node(elem)
            self._tail = self.root.next_
        else:
            self._tail.next_ = Node(elem)
            self._tail = self._tail.next_
        self.length += 1

    def prepend(self, elem):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('Full')
        head = self.root.next_
        self.root.next_ = Node(elem, head)
        self.length += 1

    def _iter_node(self):
        p = self.root.next_
        while p is not None:
            yield p
            p = p.next_

    def __iter__(self):
        for p in self._iter_node():
            yield p.elem

    def find(self, elem):
        index = 0
        for p in self._iter_node():
            if p.elem == elem:
                return index
            index += 1
        return -1

    def popLeft(self):
        if len(self) <= 0:
            raise Exception('Empty')
        head = self.root.next_
        self.root.next_ = head.next_
        self.length -= 1
        value = head.elem
        del head
        return value

    def remove(self, elem):
        if len(self) <= 0:
            raise Exception('Empty')
        prev = self.root
        for p in self._iter_node():
            if p.elem == elem:
                prev.next_ = p.next_
                if p is self._tail:
                    self._tail = prev
                del p
                self.length -= 1
                return elem
            prev = p
        return -1

    def clear(self):
        for p in self._iter_node():
            del p
        self.root.next_ = None
        self._tail = None
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
    l.popLeft()
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


test_linked_list()
