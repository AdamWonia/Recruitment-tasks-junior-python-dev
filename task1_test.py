"""
The program contains tests for the functions contained in the module 'task1.py'.
The library 'pytest' was used for testing. To install this resource, type the command into the console:

'pip install pytest'.

The available tests checking the correctness of the 'reverse_int()' function from the 'task1.py' module,
as well as the cases when the data given as an input has a different data type than int.

Running the tests is possible by typing the command in the terminal:

'pytest task1_test.py'.

This command will execute all tests available in the module 'task1_test.py'.
"""

import pytest
from task1 import reverse_int


@pytest.mark.parametrize("input_numb, output_numb", (
        (10, 1),
        (2147483647, 7463847412),
        (2147483648, 0),
        (-10, -1),
        (-2147483648, -8463847412),
        (-2147483649, 0),
))
def test_reverse_number(input_numb, output_numb):
    assert output_numb == reverse_int(input_numb)


@pytest.mark.parametrize("input_numb, output_numb", (
        (1.3, 3.1),
        (122.32, 23.221),
        ('ad', 'da'),
        ('-xy', '-yx'),
))
def test_reverse_number_invalid_input(input_numb, output_numb):
    with pytest.raises(Exception):
        assert output_numb == reverse_int(input_numb)
