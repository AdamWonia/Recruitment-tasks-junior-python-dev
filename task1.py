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


There are two functions in the programme. The first one 'input_int()' is used to get a number of type int from the user.
In case of wrong input data a message is displayed. The function retrieves data from the user
until the correct input is given.

The second function 'reverse_int()' is responsible for reversing the order of digits of the input number
including its sign.

The program is started by pressing the Run button in the programming environment or by typing commands in the console:

'python task1.py'

The module 'task1_test.py' contains tests for the functions in this programme.
"""


# This function returns only int from input
def input_int():
    exit_flag = True
    while exit_flag:
        try:
            n = int(input('Input: '))
            exit_flag = False
        except ValueError:
            print("Wrong input number! Type integer...")

    return n


# This function reverses a given number
def reverse_int(n):
    # Check the sign of a number:
    if n > 0:
        sign = ''
    else:
        sign = '-'
    # Check overflow of number:
    if abs(n) > ((1 << 31) - 1):
        rev_n = 0
    else:
        rev_n = int(sign + str(abs(n))[::-1])

    return rev_n


if __name__ == '__main__':
    # Insert input number of integer:
    N = input_int()

    # Reversing input number:
    rev_N = reverse_int(N)
    print('Output: ', rev_N)
