# ----------

import random

# ! randint() is use to generate small gap random numbers

random_small = random.randint(1, 10)  # ? It will generate random number between 1 to 10

print(random_small)

# ! random() is use to generate large gap random numbers

random_large = random.random() * 100

# ? It will generate random number between 1 to 99 in floating point

print(random_large)
