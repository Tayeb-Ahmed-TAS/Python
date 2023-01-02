# ---------
# ! First n-th factorial

n = int(input("Enter the last integer => "))

h = 1

for i in range(1, n + 1, 1):

    h *= i

    print(i, "! \t=\t ", h)
