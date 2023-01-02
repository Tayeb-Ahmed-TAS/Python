# ----------
# ! 1! + 2! + 3! + 4! + ..... + n!

n = int(input("Enter the last integer => "))

sum = 0

h = 1

for i in range(1, n + 1, 1):

    h *= i

    sum += h

print("The sum is ", sum)
