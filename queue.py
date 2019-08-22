__author__ = "Frank Shen"

'''
queue (FIFO)
push pop
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
        self.root.next = None
        self._tail = self.root.next
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
        return self._item_linked_list.pop_left()


def test_queue():
    q = Queue()
    q.push(0)
    q.push(1)
    q.push(2)
    print(q.pop())
    print(q.pop())
    print(len(q))


test_queue()