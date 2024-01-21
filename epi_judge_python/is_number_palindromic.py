from test_framework import generic_test

def reverse_number(x: int) -> int:
    num = 0
    while x > 0:
        num_ones_place = x % 10
        num = (num * 10) + num_ones_place
        x //= 10
    return num

def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    return x == reverse_number(x)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
