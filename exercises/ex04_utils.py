"""EX04 - This exercise implements algorithms to practice computational thinking."""

__author__ = "730669747"


def all(input: list[int], target: int) -> bool:
    """Defining all -should return a bool indicating whether or not all the ints in the
    list are the same as the given int"""
    if len(input) == 0:
        return False
    for number in input:
        if number != target:
            return False
    return True


def max(input: list[int]) -> int:
    """Defining max - max should return the largest in the List."""
    if len(input) == 0:
        raise ValueError(
            "max() arg is an empty List"
        )  # If list is empty return ValueError

    current_max = input[0]  # Setting current max to the first element at first
    for number in input:
        if number > current_max:
            current_max = number
    return current_max


def is_equal(a: list[int], b: list[int]):
    """return True if every element at every index is equal in both lists."""
    if len(a) != len(b):
        return False  # if the lists dont have same indexes it will return false

    for i in range(len(a)):
        if a[i] != b[i]:
            return False  #
    return True  # if none of the if statements are entered than it will return true


def extend(a: list[int], b: list[int]) -> None:
    """Defining eextend - mutate the first list of int values by appending the second
    lists values to the end of it."""
    for elem in b:
        a.append(elem)
    return None


if __name__ == "__main__":
    """Testing the functions to make sure they all work"""
    # Testing the `all()` function
    print(all([1, 2, 3], 1))  # Should print: False
    print(all([1, 1, 1], 1))  # Should print: True
    print(all([], 1))  # Should print: False

    # Testing the `max()` function
    print(max([1, 3, 2]))  # Should print: 3
    print(max([100, 99, 98]))  # Should print: 100
    # print(max([]))  # Should raise ValueError

    # Testing the `is_equal()` function
    print(is_equal([1, 0, 1], [1, 0, 1]))  # Should print: True
    print(is_equal([1, 1, 0], [1, 0, 1]))  # Should print: False

    # Testing the `extend()` function
    a = [1, 3, 5]
    b = [2, 4, 6]
    extend(a, b)
    print(a)  # Should print: [1, 3, 5, 2, 4, 6]

    c = [7, 8]
    extend(c, b)
    print(c)  # Should print: [7, 8, 2, 4, 6]
