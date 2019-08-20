__author__ = "Frank Shen"


def quick_sort(seq):
    if len(seq) < 2:
        return seq
    else:
        pivot_index = 0
        pivot = seq[pivot_index]
        less_part = [i for i in seq[pivot_index+1:] if i <= pivot]
        great_part = [i for i in seq[pivot_index+1:] if i > pivot]
        return quick_sort(less_part) + [pivot] + quick_sort(great_part)


def test_quick_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    print(quick_sort(seq))


test_quick_sort()

def partition(array, beg, end):
    pivot_index = beg
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1
    while True:
        while left <= right and array[left] < pivot:
            left += 1

        while right >= left and array[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]
    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right


def quick_sort_inplace(array, beg, end):
    if beg < end:
        pivot = par
