__author__ = "730669747"


def find_and_remove_max(lst: list[int]) -> int:
    if not lst:  # If the list is empty, return -1
        return -1

    max_value = max(lst)  # Find the maximum value in the list
    while max_value in lst:
        lst.remove(max_value)  # Remove all instances of the maximum value

    return max_value  # Return the maximum value
