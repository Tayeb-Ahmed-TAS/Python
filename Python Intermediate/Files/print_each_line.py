file=open("new_file.txt","r")

text=file.readlines()

print(text[2])

file.close()