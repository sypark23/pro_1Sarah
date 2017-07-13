# REVIEW: Conditionals, for loops, lists, and functions

#INSTRUCTIONS:

#1:

# Make the string "sentence_string" into a list called "sentence_list"
# sentence_list should be a list of each letter in the string:
# ['H', 'e', 'l', 'l', 'o', ',', ' ', 'm', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's',
# ' ', 'M', 'o', 'n', 't', 'y', ' ', 'P', 'y', 't', 'h', 'o', 'n', '.']

# Hint: Use a for loop and with an append function: list.append(letter)

sentence_string = "Hello, my name is Monty Python."





#2:
# Print every item of sentence_list on a separate line using a for loop
# H
# e
# l
# l
# o
# ,
#
# m
# y
# .... keeps going on from here.





#3:
# write a for loop that goes through each letter in the list vowels
# in the for loop, if the letter is 'b', print out the index of that letter

vowels = ['a', 'b', 'i', 'o', 'u', 'y']






#4:
# use the index found above to change 'b' to 'e' in the list vowels






#5:
# Using a for loop that goes through each letter in the sentence and an if statement,
# that checks wheter a letter is in the list vowels, print the vowels in
# sentence_string







#6:
# Make a new function called "vowelFinder" that will return a list of  the vowels
# found in a list (no duplicates).
# The function's parameters should be "list" and "vowels."
#
# Example:
# vowelList = vowelFinder(sentence_list, vowels)
# print vowelList
# would print:
# ['a', 'e', 'i', 'o', 'y']

def vowelFinder(list, vowel_list):

    #Fill in the function and change the return statment.
    return ['s']








vowels = ['a', 'e', 'i', 'o', 'u', 'y']
print("Vowel Finder Tests")

# Test 11
if vowelFinder(['C', 'n', 's', 'n', 't', 's'], vowels) == []:
    print ("Test 11: PASS")
else:
    print ("Test 11: FAIL")

sentence_string = "Hello, my name is Monty Python."
sentence_list = []
for letter in sentence_string:
    sentence_list.append(letter)

# Test 12
if vowelFinder(sentence_list, vowels) == ['a', 'e', 'i', 'o', 'y']:
    print ("Test 12: PASS\n")
else:
    print ("Test 12: FAIL\n")