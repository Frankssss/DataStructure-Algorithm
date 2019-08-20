__author__ = "Frank Shen"


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))


def print_num_recursive(n):
    if n > 0:
        print_num_recursive(n-1)
        print(n)


print_num_recursive(5)


from collections import deque


class Stack(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def is_empty(self):
        return len(self._deque) == 0


def print_num_user_stack(n):
    s = Stack()
    while n > 0:
        s.push(n)
        n -= 1
    while not s.is_empty():
        print(s.pop())


print_num_user_stack(10)