"""This program is to calculate the cost of a tea party given number of guests"""

__author__: str = "730768654"


def main_planner(guests: int) -> None:
    """This function prints out the number of tea bags, treats, and total cost for the party."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """This function calculates the number of tea bags needed for the party."""
    return people * 2


def treats(people: int) -> int:
    """This function calculates the number of treats needed for the party."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This function calculates the total cost of the tea party."""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
