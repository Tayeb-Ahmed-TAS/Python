# Named function vs Lambda function

# ? Named function


def named_fnc(x):
    return x**2 + 5 * x + 4


print(named_fnc(3))


# ? Lambda function

res = (lambda x: x**2 + 5 * x + 4)(3)  # ? Here (3) is the value of x

print(res)
