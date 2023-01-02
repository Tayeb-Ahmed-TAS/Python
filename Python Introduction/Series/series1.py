# ---------
# ! 1^2 + 3^2 + 5^2 + ....... + n^2

n = int(input("Enter the last integer => "))

sum = 0

for i in range(1, n + 1, 2):

    sum += pow(i, 2)

print("The sum is ", sum)
