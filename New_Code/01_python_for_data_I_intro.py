# Python for data I
# Matthew Morris 
###############################################################################
##                      INTRO TO PYTHON, BASIC CODE CONCEPTS                 ##
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



########################EXERCISE###############################################
'''
1. Create your own mad libs game.

2. Place this in a function that you call

3. Later we will learn about inputs if you are curious feel free to google this
after you complete the exercise to continue updating your code. 
'''
## Example Game
def the_news():
    a = input('We need your help reporting on the local news! Enter a noun:')
    b = input('Enter a state:')
    c = input('Enter a verb:')
    d = input('Enter a noun:')
    e = input('Enter a proper name...someones name:')
    f = input('Enter a verb:')
    g = input('Enter a noun:')
    h = input('Enter a verb:')
    i= input('Enter a noun:')
    j = input('Enter a part of the body:')
    k = input('Enter a adjective:')
    l = input('Enter a relative type:')
    m = input('Enter a activity:')
    n = input('Enter a chain resteraunt:')
    o = input('Enter a adjective past tense:')
    p = input('Enter a month:')
    q = input('Enter a verb:')
    r = input('Enter a noun:')
    s = input('Enter a verb past tense:') 
    t = input('Enter a adjective:')
    u = input('Enter a verb:')
    v = input('Enter a noun:')
    w = input('Enter a plural noun:')

    ml= "A {} in {} was arrested this morning after he {} a in front of  {}.\n\
      {}, had a history of {}, but no one, not even his {} ever imagined \n\
      he'd {} with a{} stuck in his {}. \n\
      \n\
      'I always though he was {}, but I never thought he'd do something \n\
      like this. Even his {} was surprised.' \n\
      \n\
      After a brief {}, cops followed him to a {}, where he reportedly {}\n\
      in the fry machine. \n\
      \n\
      In {}, a woman was charged with a similar crime. But rather than {} \n\
      a {}, she {} with a {} dog. Either way, we imagine that after  \n\
      witnessing him {} with a {} there are probably a whole lot of {} \n\
      that are going to need some therapy.".format(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w)

    print(ml)
the_news()
###############################################################################

















