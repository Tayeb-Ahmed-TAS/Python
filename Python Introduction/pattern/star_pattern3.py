# ----------
# ! Inverse Half Pyramid of * ;
# ? Output:
# * * * *
# * * *
# * *
# *

n = int(input("Enter the number of rows => "))

for i in range(n, 0, -1):

    print(i * "* ")
