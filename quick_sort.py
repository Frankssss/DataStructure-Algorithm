__author__ = "Frank Shen"


# 递归实现
def quick_sort(seq):
    if len(seq) < 2:
        return seq
    else:
        pivot = seq[0]
        left = [elem for elem in seq[1:] if elem <= pivot]
        right = [elem for elem in seq[1:] if elem > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


def test_quick_sort():
    import random
    ll = list(range(10))
    for i in range(10):
        random.shuffle(ll)
        assert quick_sort(ll) == list(range(10))


test_quick_sort()


# def test_quick_sort():
#     import random
#     seq = list(range(10))
#     random.shuffle(seq)
#     print(quick_sort(seq))
#
#
# test_quick_sort()
#
# def partition(array, beg, end):
#     pivot_index = beg
#     pivot = array[pivot_index]
#     left = pivot_index + 1
#     right = end - 1
#     while True:
#         while left <= right and array[left] < pivot:
#             left += 1
#
#         while right >= left and array[right] >= pivot:
#             right -= 1
#         if left > right:
#             break
#         else:
#             array[left], array[right] = array[right], array[left]
#     array[pivot_index], array[right] = array[right], array[pivot_index]
#     return right
#
#
# def quick_sort_inplace(array, beg, end):
#     if beg < end:
#         pivot = par
