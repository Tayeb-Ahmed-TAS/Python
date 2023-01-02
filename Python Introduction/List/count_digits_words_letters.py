# --------
# ! Count digits, letters, and words the user inputs

user_input = input("Enter the sentence => ")

digits, words, letters = 0, 1, 0

# ? words = 1 because space is 1 less than total words

for i in user_input:

    # ? Converts all the characters to lowercase because we applied the lowercase condition

    i = i.lower()

    if i >= "a" and i <= "z":

        letters += 1

    elif i >= "0" and i <= "9":

        digits += 1

    elif i == " ":

        words += 1

print(f"Total Letters \t= {letters}\nTotal Words \t= {words}\nTotal Digits \t= {digits}")
