"""This program is to compute the wordle game."""

__author__: str = "730768654"

WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def input_guess(expected_length: int) -> str:
    """This function prompts the user for a word of a certain length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    if len(guess) == expected_length:
        return str(guess)
    else:
        print(f"That wasn't {expected_length} chars! Try again:")
        return input_guess(expected_length)


def contains_char(word: str, single_character: str) -> bool:
    """This function checks if a single character is found in a word."""
    assert len(single_character) == 1, f"len('{single_character}') is not 1"
    if word == "":
        return False
    if word[0] == single_character:
        return True
    else:
        return contains_char(word[1:], single_character)


def emojified(guess: str, secret: str) -> str:
    """This function compares a guess to the secret word and returns a string of emoji boxes color in green, yellow or white."""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    emoji: str = ""
    index: int = 0
    while index < len(secret):
        if guess[index] == secret[index]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[index]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        index += 1
    return emoji


def main(secret: str) -> None:
    """The main game loop: entrypoint of the game."""
    turn: int = 1
    won: bool = False
    while turn <= 6 and not won:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        result: str = emojified(guess, secret)
        print(result)

        if guess == secret:
            won = True
            print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
    if not won:
        print(f"X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
