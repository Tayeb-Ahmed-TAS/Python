# -----------
# ! A
# ! B B
# ! C C C
# ! D D D D

n=int(input("Enter the number of rows => "))

j = 1

for i in range(n):

    print(j * f"{chr(65 + i)} ")

    j += 1
