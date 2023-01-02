# --------
# ! Count the total number of digits in a number
# ? Input: 75869
# ? Output: 5

n = int(input("Enter an integer => "))

s = 0

while n != 0:

    n = n // 10

    s = s + 1

print(s)
