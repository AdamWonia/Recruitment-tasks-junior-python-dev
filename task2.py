"""
Task 2.

Alright, here's the second task. Let's say you have a phone dial, like in the picture below.

-----------------
|   1   2   3   |
|      ABC DEF  |
|   4   5   6   |
|  GHI JKL MNO  |
|   7   8   9   |
| PQRS TUV WXYZ |
|  *    0   #   |
|       +       |
-----------------

You have to generate all the possible letter combinations for phone numbers that the user
might want to check. There are some examples below; you'll get it!

Example 1:
Input: digits = "46"
Output: ["gm", "gn", "go", "hm", "hn", "ho", "im", "in", "io"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a", "b","c"]


The module 'task2_test.py' contains tests for the class 'Solution' in this programme.
"""

# Dictionary with phone numbers with corresponding letters:
dial_dict = {
    '2': 'abc', '3': 'def',
    '4': 'ghi', '5': 'jkl', '6': 'mno',
    '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}


def combinations(digits):
    """
    Function using recursive internal solve() function finds all combinations of
    letters corresponding to given dial digits
    :param digits: string containing digits
    :return: list with all letters combinations
    """
    result = []

    def solve(current_str, i):
        if len(current_str) == len(digits):
            result.append(current_str)
            return
        for c in dial_dict[digits[i]]:
            solve(current_str + c, i + 1)

    # Start looking for combinations if 'digits' is not empty:
    if digits:
        solve("", 0)

    return result


if __name__ == '__main__':
    digits = "23"
    print(combinations(digits))
