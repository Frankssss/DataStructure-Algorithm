__author__ = "Frank Shen"

'''
堆是一种完全二叉树， 有最大堆和最小堆
最大堆：对于与每个非叶子节点V,V的值都比它的两个孩子打
最小堆：每个非叶子节点V, V的两个孩子的值都比它大。
'''

'''
parent = int((i-1)/2)
left = 2 * i + 1
right = 2 * i + 2
'''


class Array(object):
    def __init__(self, size=32, init=None):
        self._size = size
        self._items = [init] * self._size

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class MaxHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('Full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count-1)

    def _siftup(self, ndx):
        if ndx > 0:
            parent = int((ndx-1)/2)
            if self._elements[ndx] > self._elements[parent]:
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception("Empty")
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        largest = ndx
        if left < self._count and \
                self._elements[left] >= self._elements[largest] and \
                self._elements[left] >= self._elements[right]:
            largest = left
        elif right < self._count and \
                self._elements[right] > self._elements[largest]:
            largest = right
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            self._siftdown(largest)


def test_max_heap():
    n = 5
    h = MaxHeap(5)
    for i in range(n):
        h.add(i)
    for i in reversed(range(n)):
        print(h.extract(), i)


test_max_heap()