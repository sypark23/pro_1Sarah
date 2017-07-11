# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
x=raw_input("How many fibonachi numbers would you like to generate?")
x=int(x)
y=x+x
loop_control= True
x=1
y=1
sum=x+y
sum=sum+y
sum=0
x = raw_input("enter a random number")
x = int(x)
sum=x
while x>0:
    x =(raw_input("enter a random number"))
    x = int(x)
    sum=x+sum
print("the sum of the numbers you typed are "),sum

