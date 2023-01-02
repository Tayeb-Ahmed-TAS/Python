# -------
# ! 1 + 1/3 + 1/5 + 1/7 + ..... + 1/n

n = int(input("N = "))

sum = 0

for i in range(1, n + 1, 2):

    sum = sum + (1 / i)

print("Sum is ", format(sum, ".3f"))
