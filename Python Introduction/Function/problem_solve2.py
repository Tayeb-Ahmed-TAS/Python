# Problem Solve

# ! You’re working on a search engine. Watch your back Google!

# ! The given code takes a text and a word as input and passes them to a function called search().

# ! The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.

# ? Sample Input :

# ? "This is awesome"

# ? "awesome"

# ? Sample Output :

# ? Word found


def search(a, b):

    if b in a:

        return "Word found"

    else:

        return "Word not found"


text = input("Enter a sentence => ")
word = input("Enter a word")

print(search(text, word))
