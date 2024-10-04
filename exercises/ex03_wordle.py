"""EX03 - Wordle - A word guessing game."""

__author__ = "730669747"


def input_guess(expected_len: int) -> str:
    """Prompt the user to input a guess of the correct length."""
    guess = input(f"Enter a {expected_len} character word: ")
    # Loop until the user inputs a guess of the correct length
    while len(guess) != expected_len:
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    return guess


def contains_char(word: str, char: str) -> bool:
    """Check if char is in word."""
    assert len(char) == 1  # Make sure char is a single character
    # Loop through each character in the word to find a match
    for letter in word:
        if letter == char:
            return True
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Compare guess and secret and return a string of emojis representing the accuracy."""
    assert len(guess) == len(secret)  # Ensure guess and secret are of the same length

    emoji_result = ""
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            emoji_result += GREEN_BOX  # Green for correct character and position
        elif contains_char(secret, guess[i]):
            emoji_result += YELLOW_BOX  # Yellow for correct character, wrong position
        else:
            emoji_result += WHITE_BOX  # White for character not in the secret word
    return emoji_result


def main(secret: str) -> None:
    """Main game loop for the Wordle game."""
    turns = 1
    won = False
    max_turns = 6

    while turns <= max_turns and not won:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess = input_guess(len(secret))  # Prompt the user for a guess

        # Generate emoji feedback
        emoji_feedback = emojified(guess, secret)
        print(emoji_feedback)

        if guess == secret:
            print(f"You won in {turns}/{max_turns} turns!")
            won = True
        else:
            turns += 1

    if not won:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")  # codes is the word they are trying to guess
