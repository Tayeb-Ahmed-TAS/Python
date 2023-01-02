# -------
# ! Check wheather a number is Prime or Not

n = int(input("Enter an integer => "))

f = 0

m = int(n / 2)

if n == 0 or n == 1:
    f = 1

for i in range(2, m + 1, 1):

    if n % i == 0:

        f = 1

        break

print("Invalid Number! Enter a positive Integer") if n < 0 else (
    print(n, " is a prime number") if f == 0 else print(n, " is not a prime number")
)
