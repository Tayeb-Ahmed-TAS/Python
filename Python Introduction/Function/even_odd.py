def even_odd(num):

    if num % 2 == 0:

        return "Even"

    else:

        return "Odd"


n = int(input("Enter an integer => "))

print(f"{n} is ", even_odd(n))
