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


class Slot(object):
    def __init__(self, key, value):
        self.value = value
        self.key = key


class HashTable(object):
    UNUSERD = None
    EMPTY = Slot(None, None)

    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSERD)
        self.length = 0

    @property
    def _load_factor(self):
        return self.length / float(len(self._table))

    def __len__(self):
        return self.length

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSERD:
            if self._table[index] is HashTable.EMPTY:
                index = (index * 5 + 1) % _len
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index * 5 + 1) % _len
        return None

    def _slot_can_insert(self, index):
        return (self._table[index] is HashTable.EMPTY or
                self._table[index] is HashTable.UNUSERD)

    def _find_slot_for_insert(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index * 5 + 1) % _len
        return index

    def __contains__(self, key):
        index = self._find_key(key)
        return index is not None

    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            self._table[index].value = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self._load_factor >= 0.8:
                self._rehash()
            return True

    def _rehash(self):
        old_table = self._table
        newsize = len(self._table) * 2
        self._table = Array(newsize, init=HashTable.UNUSERD)
        self.length = 0

        for slot in old_table:
            if slot is not HashTable.UNUSERD and slot is not HashTable.EMPTY:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value

    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError()
        value = self._table[index].value
        self.length -= 1
        self._table[index] = HashTable.EMPTY
        return value

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.UNUSERD, HashTable.EMPTY):
                yield slot.value


def test_hash_table():
    h = HashTable()
    h.add(0, 4)
    h.add(1, 'adf')
    h.add(2, 'safda')
    h.remove(2)
    for item in h:
        print(item)


test_hash_table()