# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 08:39:11 2017

@author: Matthew
"""

people = 100.00
pineapple = 60.00
antip =40.00
paying = "Terry"

    
if (pineapple/people)*100 > 50: print "pinapple does belong on pizza"
else: print "pineapple does not belong on pizza"

if (pineapple/people) *100 > 50 and paying == "Terry": print "pinapple does not belong on pizza"
else: print "pineapple does not belong on pizza"

'''Exercise
Create a function to evaluate IMU and suggest an action
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


# We will define 3 functions:
# print_none, print_one, print_two

def print_none():
    print "Even though this has no arguements it is still important"

#This function will take 1 arguement
def print_one(arg1):
    print "arg1: %r" % arg1

# This function will take 2 arguements
def print_two(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

print_none()
    
print_one("this is an arguement") 
'''Notice I'm calling print_one function
I'm then passing text as an arguement'''

print_two("1+1", "This is arguement2")
'''I'm now calling print_two and calling 2 arguements)'''

# EXERCISE
# Build a function that prints off and gives examples of the things things you have learned so far.


# Math functions
def add(a, b):
    a=10
    b=5
    return a + b
add(a,b)

def subtract(a, b):
    a=10
    b=5
    return a - b
subtract(a,b)

def divide(a, b):
    a=10
    b=5
    return a/b
divide(a,b)

# EXERCISE:
# Write a function that takes two parameters (hours and rate), and returns the total pay.

# Total pay

# STRINGS
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
a[0].upper()+a[1:] #Uppercase of first letter in word

# checking length
len(a)      # returns 5 (number of characters)

''' EXERCISE
Write your first name in all lowercase into Variable 'first' and your last 
name into variable 'last' Combine your name together with upper case for first 
letter of your first name and upper case for first letter of your last name 
ie Terry Smith'''

