# -*- coding: utf-8 -*-

import pytest
from num_checker import check_num

class TestNumChecker(object):
    @pytest.mark.parametrize("num, expected", [
        (1, "1\n"),
        (3, "Fizz\n"),
        (5, "Buzz\n"),
        (15, "FizzBuzz\n")
    ])
    def test_success(self, num, expected):
        actual = check_num(num)
        assert actual == expected


if __name__ == '__main__':
    pytest.main()
