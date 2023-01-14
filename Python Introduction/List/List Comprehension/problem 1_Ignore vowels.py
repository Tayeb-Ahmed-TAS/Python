# Ignore Vowels

"""
! Given a word as input, output a list, containing only the letters of the word that are not vowels.

! The vowels are a, e, i, o, u. 

? Sample Input: awesome

? Sample Output: ['w', 's', 'm'] 

"""

word = input("Enter a word => ")

vowels = ["a", "e", "i", "o", "u"]

out = [i for i in word if i not in vowels]

print(out)
