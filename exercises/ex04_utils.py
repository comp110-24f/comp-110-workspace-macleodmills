"""EX04 - This exercise implements algorithms to practice computational thinking."""

__author__ = "730669747"


def all(input: list[int], target: int) -> bool:
    if len(input) == 0:
        return False
    for number in input:
        if number != target:
            return False
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    current_max = input[0]
    for number in input:
        if number > current_max:
            current_max = number
    return current_max


def is_equal(a: list[int], b: list[int]):
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def extend(a: list[int], b: list[int]) -> None:
    for elem in b:
        a.append(elem)


if __name__ == "__main__":
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
