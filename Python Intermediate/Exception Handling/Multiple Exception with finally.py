queue = [10, 0, 30, 15]

try:
    n = int("2:")  # ! Its a ValueError

    result = queue[0] / queue[n]

    print(result)

except ZeroDivisionError:
    print("Dividing by zero is not possible !")

except IndexError:
    print(f"Index Error ! Index {n} is not available !")

finally:
    print("Successful !")

    # ? The error will occur but this part will work.
