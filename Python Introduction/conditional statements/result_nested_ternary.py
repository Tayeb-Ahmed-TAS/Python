# ---------
# ! Result : Pass or Fail using Nested Ternary operator

marks = int(input("Enter your marks => "))

print("Result : Pass") if marks >= 33 and marks <= 100 else (
    print("Result : Fail") if marks <= 32 and marks >= 0 else print("Invalid Mark !!!")
)
