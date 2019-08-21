__author__ = "Frank Shen"


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


def test_array():

    size = 10
    a = Array(size)
    a[0] = 1
    a[1] = 2
    a[2] = 3
    assert len(a) == 10
    assert [i for i in a if i is not None] == [1, 2, 3]
    assert a[0] == 1
    a.clear()
    assert a[0] is None


test_array()