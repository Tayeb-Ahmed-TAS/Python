a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)  # ? Output: 1

print(b)  # ? Output: 2

print(c)  # ? Output: [3, 4, 5, 6, 7, 8]

print(d)  # ? Output: 9

a, b, c, d, *e, f, g = range(20)

print(len(e))  # ? Output: 14
