# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
# Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
num=0
x= raw_input ("How many fibonaci numbers would you like to generate?")
x=int(x)
previous=0
current=1
while num <x:
    num=num+1
    print current
    y=previous+current
    previous=current
    current=y

