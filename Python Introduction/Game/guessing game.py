from random import random
from math import floor

user_guess = int(input("Enter an integer between 1 to 100 => "))

random_number = floor(random() * 101)

if user_guess == random_number:

    print("You have won")

else:

    print("You have lost")

    print("Random number was  ", random_number)
