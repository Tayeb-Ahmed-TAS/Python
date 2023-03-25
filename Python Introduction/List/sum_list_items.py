# ! Python program to find sum of elements in list

list = [1, 5, 6, 9, 7, 3, 10, 36, 45]

sum = 0

for i in list:
    text = f"{sum} + {i} = "

    sum += i

    print(text, sum)

print("Final sum is ", sum)


# ? Output:
# ? 0 + 1 =  1
# ? 1 + 5 =  6
# ? 6 + 6 =  12
# ? 12 + 9 =  21
# ? 21 + 7 =  28
# ? 28 + 3 =  31
# ? 31 + 10 =  41
# ? 41 + 36 =  77
# ? 77 + 45 =  122
# ? Final sum is  122