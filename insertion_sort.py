__author__ = "Frank Shen"


def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos-1]:
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = value


def test_insertion_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    insertion_sort(seq)
    print(seq)


test_insertion_sort()


def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if seq[j] < seq[j-1]:
                seq[j-1], seq[j] = seq[j], seq[j-1]


def test_insertion_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    insertion_sort(seq)
    print(seq)


test_insertion_sort()

