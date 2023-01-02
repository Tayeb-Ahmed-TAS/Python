# ---------
# ! Write a program to print multiplication table of a given number

n=int(input("Enter the number => "))

row=int(input("Enter the row of the table => "))

for i in range(1, row + 1):

    print(n * i)
