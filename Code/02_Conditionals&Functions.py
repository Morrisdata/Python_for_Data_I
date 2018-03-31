# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 08:39:11 2017

@author: Matthew
"""
'''		
As a coder search engines like google and sites like stack overflow can be
your best resources for coding. Take a moment and do a google search for raw_input()
after this look up raw_input() Python 3		
'''		
		
answer = raw_input() # when you run this you will have a prompt but no directions

answer2 = raw_input('Ask a question...  :')

# EXERCISE
# This code has a few blanks that need to be fixed.		
	
def ritest():		
    print "What is the code that allows for input?"		
    q1 = raw_input()	
    print ('''How does it work? If you are not exactly sure take 1 second to go 
    online to research then answer.''')		
    q2 = 
    print "name at least 1 example where this might be handy?"
    		
    print "So, the code that allows for user input is %r, the way it works is: %r and an example of why you would use this would be %r. Cool!" % (		
            q1, q2, q3)		
ritest()		

# We will define 3 functions with examples of arguments:
# print_none, print_one, print_two

def print_none():
    print "Even though this has no arguements it is still important"

#This function will take 1 arguement
def print_one(arg1):
    print "arg1: %r" % arg1 # %r is raw data that is accepted and arg1 represents what is being passed in

# This function will take 2 arguements
def print_two(arg1, arg2):
    print "arg1 %r arg2: %r" % (arg1, arg2)

print_none()
    
print_one("t") 
'''Notice I'm calling print_one function
I'm then passing text as an arguement'''

print_two("1+1", "This is arguement2")
'''I'm now calling print_two and calling 2 arguements)'''


# Math functions and arguements
a=10
b=5
def add(a, b):
   return a + b
add(a,b)

a=10
b=5
def subtract(a, b):
   return a - b
subtract(a,b)


def divide(a, b):
    a=10
    b=5
    return a/b
divide(a,b)

# EXERCISE:
# Write a function that takes two parameters (hours and rate), and returns the total pay.
# Bonus - Use raw_input to make the variables dynamic
# Total pay
hours = 10
rate = 1000


def moula(hours,rate):
    return hours*rate
moula(hours,rate)


# Conditionals pinapple pizza debate
people = 100.00
pineapple = 40.00
antip =60.00
paying = "Terry"

    
if (pineapple/people)*100 > 50: print "pinapple does belong on pizza"
else: print "pineapple does not belong on pizza"


if (pineapple/people) *100 > 50 or paying == "Terry": print "pinapple does belong on pizza"
else: print "pineapple does not belong on pizza"

'''Exercise
Create a function to evaluate IMU and suggest an action
BONUS : use raw_inputs instead of the hard coded values below

Here is a list of products and how much they cost the store to buy
Jean_cost = 25
Shirt_cost = 15
Shoe_cost = 10

Here is a list of what they are being sold for
Jean_price = 60
Shirt_price = 20
Shoe_price = 11

We want to keep our margins begween 2% and 14% Create a function that evaluates the cost and the sell price
If it is over 14% bring back directions to markdown
If it is under 2% bring back directions to markup
If it is in range bring back directions to keep same
'''

#IMU evaluation and suggestions.





''' PROJECT EXERCISE
Let's think about breaking your learning into UNITS
Unit 1 has topic like:
Printing
Basic Math
Raw_input
Functions
etc

Unit 2 has topics like
Conditionals and arguments

Revisit your previous project and consider how you might use 
If then else, Math, arguements, raw_input and conditionals to update your 
scores, find your averages and give recommendations and what you can add to
your resume or what you need to practice.
Could you use Raw_input with If then else to create a Quiz? Maybe later you can
begin grading the quiz.
'''
