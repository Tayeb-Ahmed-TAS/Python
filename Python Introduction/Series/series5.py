# ----------
# ! 1 + 2^2 + 3^3 + 4^4 + ...... + n^n

n = int(input("Enter the last integer => "))

sum = 0

for i in range(1, n + 1, 1):

    sum = sum + (pow(i, i))

print("The sum is ", sum)
