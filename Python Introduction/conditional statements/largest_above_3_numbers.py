# ---------
# ! Largest above three numbers using nested if else

num1 = int(input("Enter The first number => "))

num2 = int(input("Enter The second number => "))

num3 = int(input("Enter The last number => "))

if num1 > num2:

    if num1 > num3:

        print(f"{num1} is largest")

    else:

        print(f"{num3} is largest")

else:

    if num2 > num3:

        print(f"{num2} is largest")

    else:

        print(f"{num3} is largest")
