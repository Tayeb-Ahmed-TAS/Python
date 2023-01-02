# -----------
# ! Write a program to control entrance to a club.
# ! Only people who are 18 or older are allowed to enter the club.
# ! Your program takes the age of the person who tries to enter, and outputs "Allowed"  if they are allowed to enter the club, and "Sorry" if they are younger than the allowed age.
# ? Sample Input: 24
# ? Sample Output: Allowed

age = int(input("Enter your age => "))

if age >= 18:

    print("Allowed")

else:

    print("Sorry")
