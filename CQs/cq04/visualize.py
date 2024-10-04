from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

"""This is where I called everything for the everything to work."""

x = "123"
y = "abc"


if __name__ == "__main__":  # calling concat and coords
    print(concat(x, y))
    get_coords(x, y)
