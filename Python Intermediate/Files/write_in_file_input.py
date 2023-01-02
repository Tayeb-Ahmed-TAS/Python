file = open("new_file.txt", "a")

name = input("Enter name => ")

age = int(input("Enter age => "))

title = input("Enter title => ")

file.write(f"\n{name} \t\t{age} \t\t\t{title}")

file.close()
