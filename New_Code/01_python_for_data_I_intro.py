# Python for data I
# Matthew Morris 
###############################################################################
##                      PYTHON FOR DATA I
## UNIT 1 PROGRAMMING PRINCIPLES, INTRO TO STRINGS
## UNIT 2 MATH AND 3 VALUE LOGIC(IF, THEN, ELSE)
## UNIT 3 FUNCTIONS
## UNIT 4 WORKING WITH FILES
## UNIT 5 DATA STRUCTURES
## UNIT 6 LOOPS AND LISTS
##
## The class is desinged to be a loop, once you finish you can start over
## and continue to build your program and skills. 
###############################################################################
'''
EXTRA NOT IN COVERED IN CLASS - running your program
Script are eventually meant to be run. 
Starting out you can do this from a few different places 
but it does fall outside the scope of the class. Primarly because, configuring
can take up time for 1 person and not another and today we want to focus on
programming. 

However, here are some helpful links to get you started on running your 
programs from the command line after class.

CONFIGURING YOUR ENVIRONMENT VARIABLES
This varies from device to device. You may get lucky and not have to do much
or you may need to spend a decent part of a Saturday surfing the web to 
work through various troubleshooting, here are a few to get you started

https://geek-university.com/python/add-python-to-the-windows-path/
https://stackoverflow.com/questions/34030373/anaconda-path-environment-variable-in-windows

In your start menu run anaconda command prompt for easier access
use Conda CMD to navigate using CD change directory to where your scripts 
are stored
C:\Users\Matthew\Desktop\GA\02_BOOTCAMPS\PYTHON\Python_for_Data_I\SCRIPTS>
nameofscript
you may need to associate your scripts to the python executable(python.exe)
Not the funnest configuring everything but once your done, 
it's programming time!
'''
###############################################################################
##                      PYTHON FOR DATA I - UNIT 1
##               PROGRAMMING PRINCIPLES, INTRO TO STRINGS
## COMMENTING
## PROGRAMMING PRINCIPLES
## STRINGS
## PROJECT EXERCISE 
###############################################################################


########################COMMENTING YOUR CODE###################################

# Enter one line of comments
''' 
Enter
Multiple 
Lines 
Of
Comments
'''
'''
in 

'''

'''
print("We are in a comment")
print ("We are still in a comment")
'''
print("We are out of the comment")

###############################################################################
##                       NICE HEADERS                                        ##
###############################################################################

print ('we wont be learning Hello World') # we want to divide nlc by cost


## More on Commenting
'''
You should comment before each new section of code and can even comment line 
by line. Aside from that whenever you have a breakthrough comment instructions
on what you did for your future self to remember. Write your comment as though
someone who does not read code would understand what the code is doing from 
your comment. 
'''
# Commenting out code
print("Not a comment")
#print("Am a comment") notice using the # to comment out code you don't want to run


########################PROGRAMMING PRINCIPLES#################################

# PYTHON PHILOSOPHY
'''
Beautiful is better than ugly
Explicit is better than implicit
Simple is better than complex
Complex is better than complicated
Readability counts

to read all of the python philosphy simply run import this.
'''
import this #Restart kernal to display again, and again

# more documentation https://www.python.org/doc/

####################VOCABULARY#################################################
'''
There are a lot of new terms to learn here are just a few to get started

LIBRARY
Python library is a collection of functions and methods that allows you to 
perform many actions without writing your code. For example, the Python imaging 
library (PIL).is one of the core libraries for image manipulation in Python.
Concept: import a library building
Syntax: import library

MODULE import 
a file consisting of Python code. A module can define functions, classes and 
variables. A module can also include runnable code.
Concept: Import history section from the library building
Syntax: import libary.history_section

FUNCTION f() 
reusable code, sometimes called a method (object oriented programming)
A process for making something. IE recipe for pizza

CLASSES 
A class is a code template for creating objects
design for a car


OBJECTS 
instance of a class 
actual car created from design

Expressions - returns a value 
Statements - statement is a line of code
 1 statement per line while code line reduction is good multiple statements
 per line is not
 '''

##EXAMPLES OF GOOD CODE VS BAD CODE

# Good code
import platform
print (platform.python_version())
("let's get to the hands on exercises!")

# Better code
import platform
print ((platform.python_version())+" "+("let's get to the hands on exercises!"))

# Bad code
import platform
print(platform.python_version()); print("let's get to the hands on exercises")

##CODING USES CODING USES CODING
# Brief over view of coding 
def traffic_cop():
    go()
    
def go():
    print("wave cars to go")

traffic_cop()

###############################################################################
##                             STRINGS                                       ##
###############################################################################
''' If you have ever done any amount of working with SQL or EXCEL you will be 
familiar with the need to review and manipulate strings.
If you have not these basic concepts may come in handy 
in the future. '''

# creating
a = 'hello'     # can use single or double quotes

# slicing
a[0]        # returns 'h' (works like list slicing)

# slicing
a[1:3]      # returns 'el'

# slicing
a[-1]       # returns 'o'

# concatenating concats are the same as Excel or SQL you can concat blanks or multiple columns
a + ' there'        # use plus sign to combine strings

# concatenating ()
str(5) + ' there'   # cast 5 to a string in order for this to work

# uppercasing
a.upper()       # string method (this method doesn't exist for lists)

# upper casing 
a[0].upper()+a[:-1] #Uppercase of first letter in word

# checking length
len(a)      # returns 5 (number of characters)

## EXERCISE
'''
Create a function called proper, write your first name in all lowercase into 
Variable 'first' and your last name into variable 'last' Combine your name 
together with upper case for first letter of your first name and upper case for 
first letter of your last name 
ie Terry Smith
'''

# %r(raw), %d(Decimal), %s(string) Passing varibables into text 
a = 'cats'
b = 'dogs'
c = 5

("I have %d %r and %d %r") %(c,b,c,a)


# Using format to accomplish the same task
a = 'cats'
b = 'dogs'
c = 5
("I have {} {} and {} {}").format(c,b,c,a)

x = "fun"
print("Mad_libs is a {} game".format(x))

##Example 2
print("Mad_libs is a {} game.".format("fun"))


# variables often times are loaded into variables
x = "fun"
y = "dog"
print("Mad_libs is a {} game. I like to play with my {}.".format(x,y))


x = "fun"
y = "dog"
z = "Mad_libs is a {} game. I like to play with my {}.".format(x,y)
print (z)


''' PROJECT EXERCISE - Make a list of skills and score it. 

0 = Don't know
1 = Aquiring knowledge
2 = Can apply with 80% help from Google
3 = Can apply with 20% help from Google
4 = Can teach <20% help from Google
5 = Can design, review, optimize

1) Create Variables that will hold each rating score
    a = "3"

2) Review what has been covered and 
3) Print a line for each skill you have learned and rate it by passing variable in
    z= "printing        : {}".format(a)

What areas are you doing great in, what areas do you need to study?
This Project will grow and be designed and redesigned several different ways
as you progress and revist. When you have completed the course come back to this lesson
and update it. Think about the new things you have learned and how you can modify your 
first block of code.
As you create the code think of what you would like to make it easier, maybe a prompt?
If you think,"There has to be an easier way!" There usually is.  take notes on any
ideas or thoughts," Can I do an average score?". "How?" '''




