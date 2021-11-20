"""
The program contains tests for the functions contained in the module 'task3.py'.
The library 'pytest' was used for testing. To install this resource, type the command into the console:

'pip install pytest'.

Available tests are used to validate the functionality of the 'justify()' function.
They include a check for proper justification of a string given as input to the function,
as well as the case when the input is incorrect.

Running the tests is possible by typing the command in the terminal:

'pytest task3_test.py'.

This command will execute all tests available in the module 'task3_test.py'.
"""

import pytest
from task3 import justify


@pytest.mark.parametrize("words, max_width, result", (
        ("Hey there mate, it’s nice to finally meet you!", 16,
         ['Hey  there mate,', 'it’s   nice   to', 'finally     meet', 'you!']),
        ("Hey there mate, it’s nice to finally meet you!", 13,
         ['Hey     there', 'mate,    it’s', 'nice       to', 'finally  meet', 'you!']),
        ("Hey there mate, it’s nice to finally meet you!", 20,
         ['Hey    there   mate,', 'it’s     nice     to', 'finally   meet  you!'])
))
def test_justify_text(words, max_width, result):
    print(justify(words, max_width))
    assert result == justify(words, max_width)
