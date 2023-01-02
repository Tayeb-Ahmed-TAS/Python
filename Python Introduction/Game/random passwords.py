# -----------
# ! Generate Random Password

from random import sample

lower_case = "abcdefghijklmnopqrstuvwxyz"

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers = "0123456789"

special_characters = "`~!@#$%^&*()_-+/|\:;"

pass_val = lower_case + upper_case + numbers + special_characters

length = int(input("Enter password length => "))  # ? Maximum length 82

password = "".join(sample(pass_val, length))

print("Password : ", password)
