# --------
# ! First n-th prime numbers

n = int(input("Enter the last integer => "))

f = 0

print(f"First {n} prime numbers =>\n")

for i in range(2, n + 1, 1):

    k = int(i / 2)

    f = 0

    for j in range(2, k + 1, 1):

        if i % j == 0:

            f = 1

            break

    if f == 0:

        print(i, end="  ")
