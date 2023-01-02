# -----------
# ! 1/1! + 1/2! + 1/3! + ...... + 1/n!

n = int(input("Enter the last integer => "))

sum, h = 0, 1

for i in range(1, n + 1, 1):

    h = h * i

    sum = sum + (1 / h)

print("The sum is ", sum)
