# Sum of numbers using xargs


def sum(*numbers):

    sum = 0

    for i in numbers:

        sum += i

    print("Sum => ", sum)


sum(10, 30)

sum(10, 30, 40)

sum(10, 30, 20, 40)

sum(10, 30, 40, 50, 60)
