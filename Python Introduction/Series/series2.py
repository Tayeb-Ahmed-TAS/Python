# ---------
# ! 2^3 + 4^3 + 6^3 + ....... + n^3

n = int(input("Enter the last integer => "))

sum = 0

for i in range(2, n + 1, 2):

    sum += pow(i, 3)

print("The sum is ", sum)