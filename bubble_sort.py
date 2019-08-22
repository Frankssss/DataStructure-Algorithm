__author__ = "Frank Shen"


# 冒泡排序
def bubble_sort(seq):
    n = len(seq)
    for i in range(n-1):
        for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]


def test_bubble_sort():
    import random
    seq = list(range(10))
    for i in range(10):
        random.shuffle(seq)
        bubble_sort(seq)
        assert seq == list(range(10))


test_bubble_sort()
