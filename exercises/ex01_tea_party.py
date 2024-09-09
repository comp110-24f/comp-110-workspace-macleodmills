"Tea Party Exercise 1"

__author__: str = "730669747"


# Defining main planner
def main_planner(guests: int) -> None:
    tea_count = tea_bags(guests)
    treat_count = treats(guests)
    print(f"The cozy tea party will have {guests} guests!!!")
    print(f"Tea bags needed: {tea_count}")  # Print tea bags needed
    print(f"Treats needed: {treat_count}")  # Print treats needed
    print(f"Total cost: ${cost(treat_count, tea_count)}")  # Total cost added together


# Defining Tea Bags
def tea_bags(guests: int) -> int:
    tea_count = guests * 2
    return int(tea_count)  # Two teabags per person


# Defining Treats
def treats(guests: int) -> int:
    return int(guests * float(1.5))  # 1.5 treats per person

    # Defining Cost of everything


def cost(treat_count: int, tea_count: int) -> float:
    treat_cost = treat_count * 0.75  # total cost of treats
    tea_cost = tea_count * 0.50  # total cost of teas
    total_cost = treat_cost + tea_cost  # total cost of everything
    return total_cost  # returning the answer


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party? "))
    )  # asks how many people are coming
