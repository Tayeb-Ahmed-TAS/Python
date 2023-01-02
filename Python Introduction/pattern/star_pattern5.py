# -----------
# ? Output:
#        * 
#      * * 
#    * * * 
#  * * * * 
# ? Formula=> (n - i) * "  " , i * "* "


n=int(input("Enter the number of rows => "))

for i in range(1, n + 1):

    formula = n - i

    print(formula * "  ", i * "* ")
