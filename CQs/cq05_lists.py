"""Mutating functions."""

__author__ = "730669747"


def manual_append(numbers: list[int], new_number: int) -> None:
    """Append an integer to the end of a list of integers."""
    numbers.append(new_number)


def double(numbers: list[int]) -> None:
    """Double each element in a list of integers."""
    idx: int = 0  # Index variable to iterate over the list
    while idx < len(numbers):
        numbers[idx] *= 2  # Double the value at the current index
        idx += 1  # Move to the next index


# Global variables
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1  # list_2 references the same list as list_1

# Call double function on list_2
double(list_2)

# Print statements to see the results
print(f"list_1: {list_1}")  # Output: [2, 4, 6]
print(f"list_2: {list_2}")  # Output: [2, 4, 6]
