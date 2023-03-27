# ! ---------

# ! Show Vowels or ignore consonant

# ? Sample Input: Awesome

# ? Sample Output: ['a', 'e', 'o', 'e']


user_inp = input("Enter a word => ")

vowels = ["a", "e", "i", "o", "u"]

user_inp = user_inp.lower()

res = [i for i in user_inp if i in vowels]

print(res)
