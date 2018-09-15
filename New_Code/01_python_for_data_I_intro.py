# Python for data I
# Matthew Morris 
###############################################################################
##                      INTRO TO PYTHON, READING FILES                       ##
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
###############################################################################
##                       NICE HEADERS                                        ##
###############################################################################

print 'we wont be learning Hello World' # inline commments should be avoided

##
#Excercise
##
#####################PYTHON INTRO##############################################

# PYTHON PHILOSOPHY
'''
Beautiful is better than ugly
Explicit is better than implicit
Simple is better than complex
Complex is better than complicated
Readability counts

to read all of the python philosphy simply run import this.
'''
import this

# more documentation https://www.python.org/doc/

####################VOCABULARY#################################################
'''
There are a lot of new terms to learn here are just a few to get started
LIBRARY from
MODULE import
FUNCTION f() reusable code, sometimes called a method
CLASSES definition    design for a car
OBJECTS instance of a class actual car created from design

Expressions - returns a value 
Statements - statement is a line of code
 1 statement per line while code line reduction is good multiple statements
 per line is not
'''

##############EXAMPLES OF GOOD CODE VS BAD CODE################################

# Good code
import platform
print (platform.python_version())
print("let's get to the hands on exercises!")

# Better code
import platform
print ((platform.python_version())+" "+("let's get to the hands on exercises!"))

# Bad code
import platform
print(platform.python_version()); print("let's get to the hands on exercises")

##############CODING USES CODING USES CODING ##################################
# Brief over view of coding
def traffic_cop():
    go()
    
def go():
    print("wave cars to go")

traffic_cop()

################ Passing variables into text###################################
##Example 1
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


















