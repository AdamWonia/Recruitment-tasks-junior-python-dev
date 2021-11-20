"""
Task 1.

Let's say you have a 32-bit long integer - call it N . You have to return it with its digits in
reversed form. If the modified value will go over the 32-bit integer range (signed), return 0.

Example 1:
Input: x = 512
Output: 215

Example 2:
Input: x = -954
Output: -459


The module 'task1_test.py' contains tests for the functions in this programme.
"""


# This function returns only int numbers from input
def input_int():
    """
    Function takes integer number from standard input
    :return: returns the specified integer or displays an error
    """
    exit_flag = True
    n = 0
    while exit_flag:
        try:
            n = int(input('Input: '))
            exit_flag = False
        except ValueError:
            print("Wrong input number! Insert integer...")

    return n


# This function reverses a given number
def reverse_int(n):
    """
    This function reverses the digit order of the input number n including its sign.
    param n: the given integer
    return: an integer with the reversed digit order or zero
    """
    # Check the sign of a number:
    sign = '' if n > 0 else '-'
    # Check overflow of number:
    rev_n = 0
    if -2 ** 31 <= n <= 2 ** 31 - 1:
        rev_n = int(sign + str(abs(n))[::-1])

    return rev_n


if __name__ == '__main__':
    # Insert input number of integer:
    N = input_int()

    # Reversing input number:
    rev_N = reverse_int(N)
    print('Output: ', rev_N)
