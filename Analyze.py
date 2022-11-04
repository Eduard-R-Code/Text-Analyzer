import string
from collections import Counter

text = "I have lots of cats and dogs. I have 3 dogs and 16 cats. I love dogs and dogs and dogs!"
print("\n")
words = text.split()
print(f"Total words used: {len(words)}")
print("\n")



#Clean-up for unique
text = text.lower()
for val in string.punctuation:
    if val not in ("'"):
        text = text.replace(val, "")


#Unique
wordz = set(words)
print(f"Unique words used: {len(wordz)}")

print("\n")
#Most used word:

word_occurence = Counter(text.split())
print(f"Top 3 most used words in the input text are: \n    {word_occurence.most_common(3)}")


freq_dict = {}
for word in words:
    freq_dict[word] = text.count(word)
list_most_used = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))



print("\n")








#The longest sentence has {} words.
#Longest sentence is:
