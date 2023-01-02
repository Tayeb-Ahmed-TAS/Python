# ----------
# ! C Program to find first n Fibonacci Sequence
# ! ex: First 10 Fibonacci Numbers : 0  1  1  2  3  5  8  13  21  34

n = int(input("Enter the last integer => "))

b, c = 1, 0

for i in range(1, n + 1, 1):

    print(c, end="  ")

    a = b

    b = c

    c = a + b
