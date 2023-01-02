# format string using format() function

numbers = [4, 5, 6]

msg = "Numbers => {0} {1} {2}".format(numbers[0], numbers[1], numbers[2])

print(msg)

# ? Output : Numbers => 4 5 6

msg = "Numbers => {1} - {0} - {2}".format(numbers[0], numbers[1], numbers[2])

print(msg)

# ? Output : Numbers => 5 - 4 - 6

print("{0}{1}{0}".format("abra", "cad"))

# ? Output : abracadabra

a = "{x}, {y}".format(x=5, y=12)

print(a)

# ? Output : 5, 12
