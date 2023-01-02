# ----------
# ! Inverse Half Pyramid of * (gap 2) ;
# ? Output:
# * * * * * * * 
# * * * * * 
# * * * 
# * 
# ? formula => (2 x i - 1) * "* "

n=int(input("Enter the number of rows => "))

for i in range(n, 0, -1):

    formula = 2 * i - 1

    print(formula * "* ")
