import unittest
import pytest

import sys


class MyTestCase(unittest.TestCase):
    def test_something(self):
        assert 1 + 1 ==2  # add assertion here

print(sys.path)

if __name__ == '__main__':
    unittest.main()
