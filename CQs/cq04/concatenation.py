"""This should return the concatenation of the two input strings."""

_author_ = "730669747"


# defining concat and setting up parameters
def concat(str1: str, str2: str) -> str:
    return str1 + str2  # returning str1 and str2


# defining word 1 and word 2
word1 = "happy"
word2 = "tuesday"

if __name__ == "__main__":  # this will result in "helloworld"
    print(concat(word1, word2))
