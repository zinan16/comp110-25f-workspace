"""This program is to practice dictionary functions."""

__author__: str = "730768654"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """This function inverts the keys and values of a dictionary."""
    inverted_dict: dict[str, str] = {}
    for key in dictionary:
        if dictionary[key] in inverted_dict:
            raise KeyError("error message of your choice here!")
        inverted_dict[dictionary[key]] = key
    return inverted_dict


invert({"a": "z", "b": "y", "c": "x"})
invert({"kris": "jordan", "michael": "jordan"})


def favorite_colors(colors: dict[str, str]) -> str:
    """This function returns the color that appears most frequently in the dictionary."""
    count: dict[str, int] = {}
    for name in colors:
        if colors[name] in count:
            count[colors[name]] += 1
        else:
            count[colors[name]] = 1
    most_frequent: str = ""
    for color in count:
        if most_frequent == "":
            most_frequent = color
        elif count[color] > count[most_frequent]:
            most_frequent = color
    return most_frequent


def count(list: list[str]) -> dict[str, int]:
    """This function counts the number of times each item appears in a list."""
    count: dict[str, int] = {}
    for item in list:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """This function returns a dictionary with the first letter of each word as the key and a list of words that start with that letter as the value."""
    alphabet: dict[str, list[str]] = {}
    for word in words:
        if word.lower()[0] in alphabet:
            alphabet[word.lower()[0]].append(word)
        else:
            alphabet[word.lower()[0]] = [word]
    return alphabet


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, name: str
) -> None:
    """This function updates the attendance log with the given day and name."""
    if day in attendance_log:
        attendance_log[day].append(name)
    else:
        attendance_log[day] = [name]
    return None
