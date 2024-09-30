"Tea Party Exercise 1"

__author__: str = "730669747"


# Defining main planner
def main_planner(guests: int) -> None:
    """Defining main planner to print outputs of tea bags, treats, and total cost."""
    tea_count = tea_bags(guests)
    treat_count = treats(guests)
    print(f"A Cozy Tea Party for {guests} People")
    print(f"Tea bags: {tea_count}")  # Print tea bags needed
    print(f"Treats: {treat_count}")  # Print treats needed
    print(f"Total cost: ${cost(treat_count, tea_count)}")  # Total cost added together


# Defining Tea Bags
def tea_bags(guests: int) -> int:
    """Returns the number of tea bags required."""
    return int(guests * 2)


# Defining Treats
def treats(guests: int) -> int:
    """Returns the number of treats based on tea bags."""
    return int(tea_bags(guests) * 1.5)


# Defining Cost of everything
def cost(treat_count: int, tea_count: int) -> float:
    """Multiply total treats and total tea bags by cost for each."""
    treat_cost = treat_count * float(0.75)  # total cost of treats
    tea_cost = tea_count * float(0.50)  # total cost of teas
    total_cost = treat_cost + tea_cost  # total cost of everything
    return total_cost  # returning the answer


if __name__ == "__main__":
    """Asking for user input in order to get number of guests."""
    main_planner(
        guests=int(input("How many guests are attending your tea party? "))
    )  # asks how many people are coming
