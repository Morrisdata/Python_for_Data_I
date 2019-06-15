###############################################################################
##                      PYTHON FOR DATA I - UNIT 3
##                             FUNCTIONS
## CONCEPT AND SYNTAX
## INPUT(Prompts)
## ANATOMY AND PHYSIOLOGY OF A FUNCTIONS(use of arguements or arg!)
## STRINGS
## PROJECT EXERCISE 
###############################################################################		

#####################CONCEPT AND SYNTAX########################################
'''
Functions are a great way to consolodate several steps into one function that
you can call over and over again in different parts of your code. When you start
this class over try applying functions to Unit 1 and 2
'''

#define lasagna():
#    mince garlic
#    cut tomato
#lasagna()#oversimplified recipe, will not result in actual lasagna

def ux():
    print ("Here is a function that is listing out printing techniques.")
    print ('Single quotes work too!')
    print ("I'd  'use' double quotes to encapsulate 'single' quotes in your prints.")
    print ('OK "maybe"  one more')
1+1
ux()
 
    
print  ("not part of ux")

## Exercise 
# How did you get here today?
# Create a function Bonuse material use what you have learned so far in your
# function.
##



## Exercise
''' 
Take the code you created from the "how you got here" exercise copy and paste it 
below and then put comments in the code to help you understand what you did 
6 months from now
'''
##





## EXERCISE
''' 
Create a function that opens a new file or creates one called python_skills
then write each skill you have learned and how you rate yourself on a seperate line
next read the file
'''
##






########################INPUTS(Prompts)########################################
'''
Inputs are a great way to dynamically change variables. 
Hard coded variables have their place but prompts can automate and make your
life much easier.
'''

# When you run this you will have a prompt but no directions
answer = input() 

# It's always a good idea to give directions with your input prompts
answer2 = input('Ask a question...  :')
answer2


## EXERCISE
''' 
Review and fix the function below
Step 1)  q1 has no question for a prompt so this will need to be fixed
Step 2)  q2 doesn't even have a input or question
Step 3)  q3 is missing entirely

Fix the code You may need to refer to prior unit. 
'''

	
def ritest():		
    print "What is the code that allows for input?"		
    q1 = input()	
    print ('''How does it work? If you are not exactly sure take 1 second to go 
    online to research then answer.''')		
    q2 = 
    print "name at least 1 example where this might be handy?"
    		
    print "So, the code that allows for user input is {}"format())
    print "the way it works is: {} 
    print "and an example of why you would use this would be "		

ritest()



############A&P OF FUNCTIONS( Use of arguements or arg!)#######################

# We will define 3 functions with examples of arguments:
# print_none, print_one, print_two

def print_none():
    print ("Even though this has no arguements it is still important")
print_none()

#This function will take 1 arguement
def print_one(x):
    print (x) # 
print_one("x allows me to pass in a usable variable")
print_one()

# This function will take 2 arguements
def print_two(x, y):
    print (x,y)
print_two(2+3, "< that number is the x variables/arguement. This is the y")
    



# Math functions and arguements

# addition
def add(a, b):
   return a + b
add(10, 20)


# subtraction
a=in
b=5
def subtract(a, b):
   return a - b
subtract(a,b)

#division
def divide(a, b):
    a=10
    b=5
    return a/b
divide(a,b)

# EXERCISE:
'''
Write a function that takes two parameters (hours and rate), and returns the total pay.
Bonus - Use raw_input to make the variables dynamic
Total pay
'''
a = input("enter a number --->")
b = int(a)
b+1





## EXERCISE
'''
Use input prompts, passing objects into a string and arguements to create
a Calculator that outputs a message after use. If you cannot think of a calculator
you can modify one from above. Consider calculations you use on a daily basis.
'''












''' PROJECT EXERCISE
Revisit your previous project and consider how you might use 
Promppts, If then else, Math, arguements to update your 
scores, find your averages and give recommendations and what you can add to
your resume or what you need to practice.
Could you use input with If then else to create a Quiz? Maybe later you can
begin grading the quiz. A good starting point is to take what you have already 
created and use prompts to make your scores dynamic.
After that try putting all of your code into a function or functions that can be
called. Beyond this is creativity design and your own ideas. 

HINT: you may want to use concat with to get your skill, question for your skill and score
into seperate rows. Concat syntax is found in first chapter. 
'''


