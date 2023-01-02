# ---------
# ! 1 + 3 + 5 + ....... + n

n = int(input("Enter the last integer => "))

sum = 0

for i in range(1, n + 1, 2):

    sum += i

print("The sum is ", sum)
