# Factorial
# ? ex: 7! = 5040


def series(n):

    sum = 1

    for i in range(1, n + 1, 1):

        sum *= i

    return sum


num = int(input("Enter the last value => "))

print(f"{num} ! = ", series(num))
