try:
    n1 = int(input("Enter first integger => "))

    n2 = int(input("Enter second integer => "))

    result = n1 / n2

    print(result)

except (ValueError, ZeroDivisionError):
    print("You have entered incorrect input !")

    # ? ValueError => 2.36 , s

finally:
    print("Thanks !")
