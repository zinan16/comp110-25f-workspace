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

my_numbers: list[float] = list()
my_numbers: list[float] = [1, 2, 3]

my_numbers.append(1.5)

print(my_numbers)

game_point: list[int] = [102, 86, 94]

print(game_point)

game_point[1] = 72

print(game_point)

game_point.pop(1)

print(game_point)

game_point.append(102)

print(game_point)

def contains(needle: int, haystack: list[int]) -> bool:
    index: int = 0
    while index<len(haystack):
        if haystack[index]==needle:
            return True
        index+=1
    return False

print(contains(3, [1, 2, 3, 4, 5]))  # should return True

def gen(n: int) -> list[int]:
    result: list[int] = []
    i: int = 0
    while i < n:
        result.append(i)
        i += 1
    return result

print(gen(5))  # should return [0, 1, 2, 3, 4]

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 10, "strawberry": 5}

ice_cream["mint"] = 3
print(ice_cream)

ice_cream["vanilla"] = 7
print(ice_cream)

for flavor in ice_cream:
    print(f"{flavor} has {ice_cream[flavor]} orders")

if "mint" in ice_cream:
    print(f"we have {ice_cream["mint"]} orders of mint ice cream")

my_list: list[str] = ["w", "x", "y", "z"]
           
for index in my_list:
    print(index)

for index in range(0, len(my_list)):
    print(index)