# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
w= raw_input("would you like to play this game and earn $1000?[please answer yes or no]")
if w =="yes":
    print"that's great you have a chance to earn a a thousand dollars!"
    x=raw_input("guess a random number between 0 and 10 \n")
    x=int(x)
    import random
    y=1
    computer_number=random.randint(1,9)
    while y<4:
        if x> computer_number:
            print("number is too big")
            x=raw_input("guess again")
            x=int(x)
            y=y+1
        if x< computer_number:
            print ("number is too small")
            x=raw_input("guess again")
            x=int(x)
            y=y+1
        if x==computer_number:
            print ("congratulations, you guessed the right number you will earn a $1000 dollars in your sleep!")
            y=y+1
            w = raw_input("would you like to play again?")
        elif y>=4:
            print("you have run out of chances")
            w=raw_input("would you like to play again?")
else:

    print"too bad your playing anyway"
    x=raw_input("guess a random number between 0 and 10 \n")
    x=int(x)
    import random
    y=1
    computer_number=random.randint(1,9)
    while y<4:
        if x> computer_number:
            print("number is too big")
            x=raw_input("guess again")
            x=int(x)
            y=y+1
        if x< computer_number:
            print ("number is too small")
            x=raw_input("guess again")
            x=int(x)
            y=y+1
        if x==computer_number:
            print ("congratulations, you guessed the right number you will earn a $1000 dollars in your sleep!")
            y=y+1
            w = raw_input("would you like to play again?")
        elif y>=4:
            print("you have run out of chances")
            w=raw_input("would you like to play again?")


while w=="yes":
    print"that's great you have a chance to earn a a thousand dollars!"
    x = raw_input("guess a random number between 0 and 10 \n")
    x = int(x)
    import random

    y = 1
    computer_number = random.randint(1, 9)
    while y < 4:
        if x > computer_number:
            print("number is too big")
            x = raw_input("guess again")
            x = int(x)
            y = y + 1
        if x < computer_number:
            print ("number is too small")
            x = raw_input("guess again")
            x = int(x)
            y = y + 1
        if x == computer_number:
            print ("congratulations, you guessed the right number you will earn a $1000 dollars in your sleep!")
            y = y + 1
            w = raw_input("would you like to play again?")
        elif y >= 4:
            print("you have run out of chances")
            w = raw_input("would you like to play again?")

else:
   print ("you will never be able to play this game again!")
   print ("regretting it? TOO BAD")