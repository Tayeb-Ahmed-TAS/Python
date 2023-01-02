# ---------
# ! Factorial of an integer

n = int(input("Enter the integer => "))

h = 1

for i in range(1, n + 1, 1):

    h *= i

print(n, "! = ", h)
