"""Practice with Functions"""

__author__ = "730669747"

"""Practice With Mimic"""


def mimic(message: str) -> str:
    return message


# Have to define main -- same as mimic
def main() -> None:
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
