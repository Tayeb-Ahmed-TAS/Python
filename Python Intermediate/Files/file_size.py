file = open("new_file.txt", "r")

text = file.read()

size = len(text)

print(size)  # ? Output : Total Character

file.close()
