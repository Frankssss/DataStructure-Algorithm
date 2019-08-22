__author__ = "Frank Shen"


def binary_search(sorted_array, val):
    if not sorted_array:
        return -1
    beg = 0
    end = len(sorted_array) - 1
    while beg <= end:
        mid = int((beg + end) / 2)
        if sorted_array[mid] == val:
            return mid
        elif sorted_array[mid] > val:
            end = mid - 1
        else:
            beg = mid + 1
    return -1


print(binary_search([1, 2, 3, 4, 5], 4))

