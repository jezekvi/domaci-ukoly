
from collections import Counter

word = input("Zadej slovo:")
#letters = list(word)
#counter = Counter(letters)

#print(counter)

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency(word))

