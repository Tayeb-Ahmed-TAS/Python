# Find Vowels from the list and show output in the tuple


def find_vowel(x):

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    return True if x in vowels else False


letters = ["T", "a", "y", "e", "b"]

result = tuple(filter(find_vowel, letters))

print(result)
