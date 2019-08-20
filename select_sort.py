__author__ = "Frank Shen"


'''
选择排序
第一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，
然后再从剩余的未排序元素中寻找到最小（大）元素，然后放到已排序的序列的末尾。
以此类推，直到全部待排序的数据元素的个数为零
'''


def select_sort(seq):
    n = len(seq)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if seq[j] < seq[min_idx]:
                min_idx = j
        if min_idx != i:
            seq[i], seq[min_idx] = seq[min_idx], seq[i]


def test_select_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    select_sort(seq)
    print(seq)


test_select_sort()