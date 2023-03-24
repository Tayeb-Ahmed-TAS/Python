# ---------
# ! Write a program to print multiplication table of a given number
# ? Input:
# ? Enter the number => 4
# ? Enter the row of the table => 5
# ? Output:
# ? 4 * 1 = 4
# ? 4 * 2 = 8
# ? 4 * 3 = 12
# ? 4 * 4 = 16
# ? 4 * 5 = 20


n = int(input("Enter the number => "))

row = int(input("Enter the row of the table => "))

for i in range(1, row + 1):
    print(f"{n} * {i} = {n*i}")
