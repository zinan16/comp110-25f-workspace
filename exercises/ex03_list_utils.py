"""This program constructs list utility functions."""

__author__: str = "730768654"

def all(list: list[int], number: int) -> bool:
    """This function checks if all the integers in a list are the same as a given integer."""
    if len(list) == 0:
        return False
    if list == []:
        return False
    index: int = 0
    while index < len(list):
        if list[index] != number:
            return False
        index += 1
    return True

def max(list: list[int]) -> int:
    """This function returns the largest integer in a list."""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    max: int = list[0]
    index: int = 1
    while index < len(list):
        if max<list[index]:
            max = list[index]
        index += 1
    return max

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """This function checks if two lists are identical."""
    if len(list1) != len(list2):
        return False
    index: int = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1
    return True