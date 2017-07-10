# Name:Sarah Park
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

x = raw_input("enter your age")

y= raw_input("enter your name")
b= raw_input("have you had your birthday this year?")
c= raw_input("Is your name 7 or more letters?")
x=int(x)
z=2017-x
#print z
if b=="no":
    z=z-1
w=z+100
my_str=y
y=my_str[0]
y=y.upper()
a=my_str.lower()
a=end_slice=my_str[1:]
if c== "yes":
    print "woooah your name is long"
else:
    print"your name legnth is reasonable :)"

print (y+a),("will turn 100 in the year"),w
print (y+a), ("is able to watch G rated movies")
if x<8:
    print (y+a),"is able to watch PG rated movies with parental guidance"
else:
    print (y+a),"is able to watch PG rated movies without parental guidance"


if x>=13:
    print (y+a),"is able to watch PG-13 rated movies without parental guidance"
else:
    print (y+a), "is able to watch PG-13 rated movies with parental guidance"

if x>=17:
    print (y+a), "is able to watch R rated movies"
else:
    print (y+a), "is unable to watch R rated movies"

