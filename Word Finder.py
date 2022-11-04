
#Word Finder



print("This part of the software will return how many times a specific word is found in your text.")
text = input("Input text: \n")
print("\n")
keyz = []

print("Caution: This software returns the exact value as written by the user, aka is case-sensitive")
keyz.append(input("Enter the word you want to search the text for: \n"))
print("\n")


word1_counter = text.count(keyz[0])

print(f"The word has been found {word1_counter} times.")

