# ---------
# ! List as input from user and compute the sum

n = input("Enter list elements as Number =>")  # ? Take input with space

new_list = n.split()

sum = 0

for i in new_list:

    sum += int(i)

print("The Sum is => ", sum)
