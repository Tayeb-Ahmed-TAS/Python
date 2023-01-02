str = ["Tony", "Thor", "Steve", "T'Chala"]

add=", ".join(str)

print(add)

# ?  Output : Tony, Thor, Steve, T'Chala

add=" & ".join(str)

print(add)

# ?  Output : Tony & Thor & Steve & T'Chala

add=" ".join(str)

print(add)

# ?  Output : Tony Thor Steve T'Chala