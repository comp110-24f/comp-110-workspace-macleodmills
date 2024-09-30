"Tea Party Exercise 1"

__author__: str = "730669747"


# Defining main planner
def main_planner(people: int) -> None:
    """Defining main planner to print outputs of tea bags, treats, and total cost."""
    tea_count: int = tea_bags(people)
    treat_count: int = treats(people)
    print(f"A Cozy Tea Party for {people} People")
    print(f"Tea bags: {tea_count}")  # Print tea bags needed
    print(f"Treats: {treat_count}")  # Print treats needed
    print(f"Total cost: ${cost(tea_count, treat_count)}")  # Total cost added together


# Defining Tea Bags
def tea_bags(people: int) -> int:
    """Returns the number of tea bags required."""
    return int(people * 2)


# Defining Treats
def treats(people: int) -> int:
    """Returns the number of treats based on tea bags."""
    return int(tea_bags(people=people) * 1.5)


# Defining Cost of everything
def cost(tea_count: int, treat_count: int) -> float:
    """Multiply total treats and total tea bags by cost for each."""
    treat_cost: float = treat_count * float(0.75)  # total cost of treats
    tea_cost: float = tea_count * float(0.50)  # total cost of teas
    total_cost: float = treat_cost + tea_cost  # total cost of everything
    return total_cost  # returning the answer


if __name__ == "__main__":
    """Asking for user input in order to get number of guests."""
    people: int = int(input("How many guests are attending your tea party? "))
    main_planner(people=people)  # asks how many people are coming
