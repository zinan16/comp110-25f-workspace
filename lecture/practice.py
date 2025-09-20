def perimeter(length: float, width: float) -> float:
    """Calculate the perimeter of a rectangle."""
    return 2 * (length + width)


print(perimeter(length=10.0, width=8.0))


def love(name: str, times: int) -> str:
    """Express love for a given name a specified number of times."""
    return (f"I Love you {name}! I thought of you {times} times today!")


print(love(name="Tim", times=520))


def volume(length: float, width: float, height: float) -> float:
    """volume of an object"""
    return length * width * height


print(volume(length=2.0, width=4.0, height=9.0))


def check_first_letter(word: str, letter: str) -> str:
    if len(letter) != 1:
        return "letter's argument should be one character!"
    elif word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="happy", letter="s"))


def number(x: int) -> None:
    if x == 0:
        print("zero")
    elif x > 0:
        print("positive")
    else:
        print("negative")


number(x=0)


def check_first_letter(word: str, letter: str) -> str:
    if len(letter) != 1:
        return "letter's argument should be one character!"
    elif letter[0] == word[0]:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="happy", letter="s"))
print(check_first_letter(word="happy", letter="ha"))


def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(n=5))


def fizzbuzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        print("Fizz")
        return fizzbuzz(n + 1)
    elif n % 5 == 0:
        print("Buzz")
        return fizzbuzz(n + 1)
    else:
        print(str(n))
        return fizzbuzz(n + 1)

fizzbuzz(n=1)

def fizzbuzz(n: int) -> int:
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
        return n
    elif n % 3 == 0:
        print("Fizz")
        return fizzbuzz(n + 1)
    elif n % 5 == 0:
        print("Buzz")
        return fizzbuzz(n + 1)
    else:
        print(str(n))
        return fizzbuzz(n + 1)
    
fizzbuzz(n=1)

z: int = 1
z = z + 1
print(z)


def count_to_n(n: int) -> None:
    i: int = 0
    while i <= n:
        print(i)
        i = i + 1


count_to_n(n=5)


def summit(n: int) -> int:
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 0
    elif n % 2 == 0:
        return n + summit(n=n - 2)
    else:
        return n - 1 + summit(n=n - 3)


print(summit(n=-2))
print(summit(n=1))
print(summit(n=2))
print(summit(n=3))


def sum_or_factorial(number: int) -> int:
    if number < 0:
        return -1
    elif number % 2 == 0:
        sum: int = 0
        i: int = 0
        while i <= number:
            sum = sum + i
            i = i + 1
        return sum
    else:
        factorial: int = 1
        i: int = 1
        while i <= number:
            factorial = i * factorial
            i = i + 1
        return factorial


print(sum_or_factorial(number=-2))
print(sum_or_factorial(number=2))
print(sum_or_factorial(number=3))

def reverse(word: str)->str:
    index:int=len(word)-1
    result:str=""
    while index>=0:
        result=result+word[index]
        index=index-1
    return result
print(reverse(word="hello"))  # should print "olleh"

def reverse(word: str)->str:
    index:int=len(word)-1
    while index>=0:
        print(word[index])
        index=index-1
print(reverse(word="hello"))  # should print "olleh"

def lp2(n: int)->int:
    number: int = 2
    while number < n:
        number *= 2
    return int(number/2)

lp2(n=17)  # should return 16