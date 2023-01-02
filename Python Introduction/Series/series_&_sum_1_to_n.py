# ---------
# ! 1 + 2 + 3 + ....... + n

n = int(input("Enter the last value => "))

sum = 0

for i in range(1, n + 1, 1):

    sum += i

    print(i, end=" ")

    if i < n:

        print("+", end=" ")

print("= ", sum)
