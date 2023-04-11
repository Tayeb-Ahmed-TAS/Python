queue = [10, 0, 30, 15]

try:
    n = int(input("Enter the index from 0 to 3 => "))

    result = queue[0] / queue[n]

    print(result)

except ZeroDivisionError:
    print("Dividing by zero is not possible !")

except IndexError:
    print(f"Index Error ! Index {n} is not available !")

except ValueError:
    # ? example of ValueError is 2:

    print("Value Error !")

print("Successful !")
