# Name:
# Date:


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
print"Welcome to hangman."
print"Today in this game you will guess the letters and have a great time playing hangman"
print"you have 7 chances"
random_word= choose_word(wordlist)
#print random_word
list = []
str=random_word
for letter in str:
    list.append(letter)

list1=[]
len(list)
print "I am thinking of a word with ",len(list),"letters"
counter=0
for letter in list:
#len(list) == len(list):
    list1.append("_")
    counter=counter+1
print list1
count_guess = 0
lst2=[]
while list != list1 and count_guess< 8:
    counter1 = 0
    guess = raw_input("Enter guess here:")
    print"here are the letters that you have already used"
    lst2.append(guess)
    print lst2
    correct=False
    while counter1 < len(list):
        if guess == list [counter1]:
            list1[counter1]= guess
            correct=True
            print "That's correct!"
        counter1 = counter1 + 1
    if correct==False:
        count_guess = count_guess + 1
    print list1
#correct=False
    if correct==False and count_guess==1:
        print   "---------"
        print   "|       |"
        print   "|       O "
        print   "|         "
        print   "|         "
        print   "|         "
        print   "-------"
        print   "|      |________"
        print   "|               |"
        print   "|_______________|"

    if correct==False and count_guess==2:
        print   "---------"
        print   "|       |"
        print   "|       O "
        print   "|       | "
        print   "|         "
        print   "|         "
        print   "-------"
        print   "|      |________"
        print   "|               |"
        print   "|_______________|"

    if correct == False and count_guess == 3:
        print   "---------"
        print   "|       |"
        print   "|       O "
        print   "|      /| "
        print   "|         "
        print   "|         "
        print   "-------"
        print   "|      |________"
        print   "|               |"
        print   "|_______________|"

    if correct == False and count_guess == 4:
        print   "---------"
        print   "|       |"
        print   "|       O "
        print   "|      /|\ "
        print   "|         "
        print   "|         "
        print   "-------"
        print   "|      |________"
        print   "|               |"
        print   "|_______________|"

    if correct == False and count_guess == 5:
            print   "---------"
            print   "|       |"
            print   "|       O "
            print   "|      /|\ "
            print   "|       | "
            print   "|         "
            print   "-------"
            print   "|      |________"
            print   "|               |"
            print   "|_______________|"

    if correct == False and count_guess == 6:
            print   "---------"
            print   "|       |"
            print   "|       O "
            print   "|      /|\ "
            print   "|       | "
            print   "|      / "
            print   "-------"
            print   "|      |________"
            print   "|               |"
            print   "|_______________|"

    if correct == False and count_guess == 7:
            print   "---------"
            print   "|       |"
            print   "|       O "
            print   "|      /|\ "
            print   "|       | "
            print   "|      / \ "
            print   "-------"
            print   "|      |________"
            print   "|               |"
            print   "|_______________|"
if list==list1:
    print "Congratulations you have finished one round of hangman"
    print "-----   ----  --  --  -----  ---   ---  -------        |     ---  ------  ------   ---   --  --  -----"
    print "|       /  \  | \ |   /   _ |___| /___\    |    |    | |    /___\    |       |    /   \  | \ |   |___"
    print "|____   \__/  |  \|   \___/ |   \ |   |    |     |__|  |__  |   |    |     __|__  \___/  |  \|   ____|"
    print "You have guessed the right word,", random_word
if count_guess>7:
    print"You have run out of chances"
    print"-----    ---    --   --    -----      -----  --   --   ----    --- "
    print"/   _   /___\  /  \ /  \   | ___      /   \    \  /   | ___   |___| "
    print"\___/   |   |  |   v   |   | ___      \___/     \/    | ___   |   \ "
    print "The word was",random_word








