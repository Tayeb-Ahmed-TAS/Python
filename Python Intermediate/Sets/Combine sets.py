first = {1, 2, 3, 4, 5, 6}

second = {4, 5, 6, 7, 8, 9}

# Union

print(first | second)  # ? Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Intersection

print(first & second)  # ? Output: {4, 5, 6}

# Difference

print(first - second)  # ? Output: {1, 2, 3}

# Difference

print(second - first)  # ? Output: {8, 9, 7}

# Symmetric difference

print(first ^ second)  # ? Output: {1, 2, 3, 7, 8, 9}
