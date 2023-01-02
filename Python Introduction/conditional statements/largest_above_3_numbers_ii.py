# ---------
# ! Largest above three numbers

n1 = int(input("Enter the first number => "))

n2 = int(input("Enter the second number => "))

n3 = int(input("Enter the last number => "))

if n1 > n2 and n1 > n3:

    print(f"{n1} is the largest number")

elif n2 > n1 and n2 > n3:

    print(f"{n2} is the largest number")

else:

    print(f"{n3} is the largest number")
