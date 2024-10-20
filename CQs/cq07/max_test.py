import unittest
from find_max import find_and_remove_max

__author__ = "730669747"


class TestFindAndRemoveMax(unittest.TestCase):

    def test_find_and_return_max_value(self) -> None:
        # Test if the function returns the correct maximum value
        lst: list[int] = [4, 2, 7, 3, 7]
        result = find_and_remove_max(lst)
        self.assertEqual(result, 7)

    def test_list_mutation(self) -> None:
        # Test if the function correctly mutates the input list
        lst: list[int] = [5, 5, 3, 5]
        find_and_remove_max(lst)
        self.assertEqual(lst, [3])

    def test_empty_list(self) -> None:
        # Test the edge case of an empty list
        lst: list[int] = []
        result = find_and_remove_max(lst)
        self.assertEqual(result, -1)
        self.assertEqual(lst, [])


if __name__ == "__main__":
    unittest.main()
