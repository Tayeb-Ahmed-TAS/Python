# Square up
# ! Tuples can be used to output multiple values from a function.
# ! You need to make a function called calc(), that will take the side length of a square as its argument and return the perimeter and area using a tuple.
# ! The perimeter is the sum of all sides, while the area is the square of the side length.
# ? Sample Input:
# ? 3
# ? Sample Output:
# ? Perimeter: 12
# ? Area: 9


def calc(x):

    return (x * 4, x**2)


side = int(input("Enter the side length => "))

perimeter, area = calc(side)

print("Perimeter: ", perimeter)

print("Area: ", area)
