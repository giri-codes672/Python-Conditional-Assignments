# Random Number Odd or Even

import random

number = random.randint(1, 100)

print("Generated Number:", number)

if number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")
