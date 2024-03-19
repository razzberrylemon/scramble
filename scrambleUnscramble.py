# this will prompt the user to enter something in the console then scramble the alphabet randomly
# then using this alphabet, the user can input text and get back their text scrambled 
import random

punctuation = list(range(32, 65)) + list(range(91, 97)) + list(range(123, 127)) + [9,10]
# holds actual ascii values
non_scramble = list(range(97, 123)) 
# holds scrambled values
scrambled = list(range(97, 123))

random.shuffle(scrambled)

dict = {}

# chr() converts ascii to char
for key, value in zip(non_scramble, scrambled):
    ch = chr(key)
    scram = chr(value)
    dict[ch] = scram
    print(ch, " = ", scram)

# add punctuation to the dictionary
for kv in punctuation:
    dict[chr(kv)] = chr(kv)


print("\nEnter some text to scramble: \n\n")

inp = input()
text = ""

# for each letter in the input
for i in inp:
    # if the letter is uppercase, convert it to lowercase to search the dictionary
    # but, add the uppercase encoded letter to 'text'
    if i.isupper():
        text = text + dict.get(i.lower()).upper()
    # if the letter isn't uppercase, don't worry about any of the above
    else:
        text = text + dict.get(i)

print("----------------------------")

print(text)


print("\n\nPress 'Enter' to unscramble: ")
inp = input()
untext = ""

print ("\n" + text)
print("----------------------------")

# for each letter of the original scramble 
for i in text:
    # these lists will allow us to locate a key, given a value 
    keys = list(dict.keys())
    values = list(dict.values())
    # if letter is uppercase, search values for lowercase instance
    # but, add the uppercase key to 'untext'
    if i.isupper():
        pos = values.index(i.lower())
        untext = untext + (keys[pos]).upper()
    # if the letter isn't uppercase, don't worry about any of the stuff above
    else:
        pos = values.index(i)
        untext = untext + (keys[pos])

print(untext + "\n")
