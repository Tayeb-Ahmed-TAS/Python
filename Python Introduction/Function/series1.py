# Series 1
# ! 1 + 2 + 3 + 4 + ...... + n


def series(n):

    sum = 0

    for i in range(1, n + 1, 1):

        sum += i

    return sum


n = int(input("Enter the last value => "))

print("The sum is ", series(n))
