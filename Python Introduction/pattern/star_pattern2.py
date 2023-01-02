# -----------
# ! Half Pyramid of * (Gap 2) ;
# ? Output:
# *
# * * *
# * * * * *
# * * * * * * *
# ? formula => (2 x i - 1) * "* "

n=int(input("Enter the number of rows => "))

for i in range(1, n + 1):  # ! Here increment is 1

    formula = 2 * i - 1

    print(formula * "* ")
