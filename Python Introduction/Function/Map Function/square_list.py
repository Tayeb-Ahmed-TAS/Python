# Square all elements of a list


def square(sq):

    return pow(sq, 2)


list1 = [1, 2, 3, 4, 5, 6]

result = list(map(square, list1))

print(result)
