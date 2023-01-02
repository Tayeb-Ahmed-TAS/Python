def even(x):

    if x % 2 == 0:

        return True

    return False


num = [1, 2, 3, 4, 5, 6]

result = list(filter(even, num))

print(result)
