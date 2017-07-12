# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""

x= raw_input("Enter a random word")
while len(x) >1:
    if x[0]!=x[-1]:
        variable=False
        break
    if x[0]==x[-1]:
        x=x[1:-1]
        x[0] == x[-1]
        variable=True

if variable == True:
    print"the word is a palindrome"
if variable == False:
    print"the word is not a palindrome"










