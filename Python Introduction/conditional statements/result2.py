# ---------
# ! Result using else if ( elif )

marks = int(input("Enter your marks : "))

if marks >= 80 and marks <= 100:

    print("Result : A+")

elif marks >= 70 and marks < 80:

    print("Result : A")

elif marks >= 60 and marks < 70:

    print("Result : A-")

elif marks >= 50 and marks < 60:

    print("Result : B")

elif marks >= 40 and marks < 50:

    print("Result : C")

elif marks >= 33 and marks < 40:

    print("Result : D")

elif marks <= 32 and marks >= 0:

    print("Result : F")

else:

    print("Enter a valid mark !!!")
