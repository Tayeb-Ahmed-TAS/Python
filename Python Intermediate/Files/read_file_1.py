file = open("new_file.txt", "r")

# ? If the file is readable it'll return True otherwise False

print(file.readable())  # ? Output : True

text = file.read()

print(text)

file.close()
