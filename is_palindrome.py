__author__ = 'Frank Shen'


def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])


print(is_palindrome('fsf'))