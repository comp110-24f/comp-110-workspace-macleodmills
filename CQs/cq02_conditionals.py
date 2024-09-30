__author__: str = "730669747"  # Make sure the author format is correct


def guess_a_number() -> None:
    secret: int = 7  # Secret number to guess

    # Prompt the user to guess
    x: str = input("Guess a number: ")

    # Echo the user's guess
    print("Your guess was " + x)  # Ensure exact format

    # Conditionals for feedback
    if int(x) == secret:
        print("You got it!")  # Exact match
    elif int(x) < secret:
        print(f"Your guess was too low! The secret number is {secret}")
    else:
        print(f"Your guess was too high! The secret number is {secret}")

    return None


# Ensure the function runs only if this script is executed directly
if __name__ == "__main__":

    guess_a_number()
