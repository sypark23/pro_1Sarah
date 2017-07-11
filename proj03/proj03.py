# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.
previous=int(previous)
current=int(current)
"""

x=raw_input("type in a number between 0 and 10[not including them]")
x=int(x)
import random
computer_number=random.randint(1,9)
print computer_number
while computer_number != x:
    if x>computer_number:
        print("the number is too big")
        x=raw_input("guess again")
        x=int(x)
    if x<computer_number:
        print("the number is too small")
        x = raw_input("guess again")
        x=int(x)
    if x==computer_number:
        print("You guessed the number congratulations!")
