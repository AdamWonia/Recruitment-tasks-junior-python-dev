"""
The program contains tests for the functions contained in the module 'task2.py'.
The library 'pytest' was used for testing. To install this resource, type the command into the console:

'pip install pytest'.

The available tests checking the correctness of the 'combinations()' function from the 'task2.py' module.
The remaining tests check the correctness of the returned letter combinations created from the input
variable 'digits', including cases where the input data is incorrect.

Running the tests is possible by typing the command in the terminal:

'pytest task2_test.py'.

This command will execute all tests available in the module 'task2_test.py'.
"""

import pytest
from task2 import combinations


@pytest.mark.parametrize("digits, combs", (
        ("23", ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
        ("28", ['at', 'au', 'av', 'bt', 'bu', 'bv', 'ct', 'cu', 'cv']),
        ("67", ['mp', 'mq', 'mr', 'ms', 'np', 'nq', 'nr', 'ns', 'op', 'oq', 'or', 'os']),
        ("79", ['pw', 'px', 'py', 'pz', 'qw', 'qx', 'qy', 'qz', 'rw', 'rx', 'ry', 'rz', 'sw', 'sx', 'sy', 'sz']),
        ("234",
         ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei',
          'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']),
        ("2", ['a', 'b', 'c']),
        ("", [])
))
def test_combinations(digits, combs):
    assert combs == combinations(digits)


@pytest.mark.parametrize("digits, combs", (
        ("sd", []),
        ("12", []),
        ("2a", []),
))
def test_combinations_invalid_input(digits, combs):
    with pytest.raises(Exception):
        assert combs == combinations(digits)
