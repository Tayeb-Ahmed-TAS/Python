# -----------
# ! A
# ! A B
# ! A B C
# ! A B C D

n=int(input("Enter the number of rows => "))

for i in range(n):  # ? 0 to n-1

    for j in range(i + 1):  # ? 0 to i

        print(chr(65 + j), end=" ")

    print("")
