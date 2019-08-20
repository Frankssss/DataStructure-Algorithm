__author__ = "Frank Shen"


def linear_search(predicate, iterable):
    for index, val in enumerate(iterable):
        if predicate(val):
            return index
    return -1


print(linear_search(lambda x: x == 5, [1, 2, 3, 4, 5]))


def linear_search_recusive(array, value):

    if len(array) == 0:
        return -1
    index = len(array) - 1
    if array[index] == value:
        return index
    return linear_search_recusive(array[0: index], value)


print(linear_search_recusive([1, 2, 3, 4, 5], 5))
