def voter(age):
    if age < 18:
        raise ValueError("You are not a voter !")

    return "You are a voter"


try:
    n = int(input("Enter your age => "))

    print(voter(n))

except ValueError as e:
    print(e)
