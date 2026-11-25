import unittest


def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6)

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5)


if __name__ == "__main__":
    unittest.main()
