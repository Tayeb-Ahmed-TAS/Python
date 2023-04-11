num = int(input("Enter an integer => "))

try:
    result = 20 / num

    print(f"20 / {num} = {result}")

except ZeroDivisionError:
    print("Dividing by zero is not possible !")

print("End")
