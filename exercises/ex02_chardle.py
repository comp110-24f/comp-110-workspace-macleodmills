"""EX02 - Chardle"""

__author__ = "730669747"


def input_word() -> str:
    """Prompt the user for a 5-character word and return it if valid."""
    word = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # Exits the program if the word length is not 5
    return word


def input_letter() -> str:
    """Prompt the user to enter a single character and return it if valid."""
    letter = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # Exits the program if the character length is not 1
    return letter


def contains_char(word: str, letter: str) -> None:
    """Search for the character in the word and print their indexs."""
    print(f"Searching for {letter} in {word}")
    count = 0
    for i in range(len(word)):
        if word[i] == letter:
            print(f"{letter} found at index {i}")
            count += 1
    if count == 0:
        print(f"No instances of {letter} found in {word}")
    elif count == 1:
        print(f"1 instance of {letter} found in {word}")
    else:
        print(f"{count} instances of {letter} found in {word}")


def main() -> None:
    """Main function to run the Chardle game."""
    word = input_word()
    letter = input_letter()
    contains_char(word, letter)


if __name__ == "__main__":
    main()
