# Create a list of multiples of 3 from 0 to 20
# ? Output: [0, 3, 6, 9, 12, 15, 18]

lst = [i for i in range(0, 21) if i % 3 == 0]

print(lst)
