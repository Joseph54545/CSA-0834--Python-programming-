word = input("Enter the word: ").upper()

vowels = sorted([char for char in word if char in "AEIOU"])
consonants = sorted([char for char in word if char not in "AEIOU" and char.isalpha()])

print("Vowels in alphabetical order:", ", ".join(vowels))
print("Consonants in alphabetical order:", ", ".join(consonants))
