"""
The program contains tests for the class 'Solution' contained in the module 'task2.py'.
The library 'pytest' was used for testing. To install this resource, type the command into the console:

'pip install pytest'.

The available tests check the correct functionality of the 'Solution' class. The first test checks that an object of
this class is correctly created.

The remaining tests check the correctness of the returned letter combinations created from the input
variable 'digits', including cases where the input data is incorrect.

Running the tests is possible by typing the command in the terminal:

'pytest task2_test.py'.

This command will execute all tests available in the module 'task2_test.py'.
"""

import pytest
from task2 import Solution


@pytest.fixture(scope='function')
def solution():
    solution = Solution()
    return solution


def test_initialization(solution):
    assert solution


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
def test_combinations_passed(solution, digits, combs):
    assert combs == solution.combinations(digits)


@pytest.mark.parametrize("digits, combs", (
        ("32", ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
        ("45", ['jg', 'jh', 'ji', 'kg', 'kh', 'ki', 'lg', 'lh', 'li']),
))
def test_combinations_failed(solution, digits, combs):
    assert not combs == solution.combinations(digits)


@pytest.mark.parametrize("digits, combs", (
        ("sd", []),
        ("12", []),
        ("2a", []),
))
def test_combinations_invalid_input(solution, digits, combs):
    assert combs == solution.combinations(digits)
