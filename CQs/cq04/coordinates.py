"""This should print the formatted pairs of each character in the two input strings."""

_author_ = "730669747"


def get_coords(xs: str, ys: str) -> None:  # defining get coords
    i = 0  # index to start
    while i < len(xs):  # outer loop will iterate over every character in xs
        j = 0  # index to start
        while j < len(ys):  # inner loop will iterate over every character in ys
            print(f"({xs[i]},{ys[j]})")  # print xs and ys
            j += 1
        i += 1
