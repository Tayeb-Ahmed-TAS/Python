n = input("Enter an alphabet => ")

vowels = ["a", "e", "i", "o", "u"]

n = n.lower()

print("Vowel") if n in vowels else print("Consonant")
