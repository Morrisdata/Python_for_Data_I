# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 10:56:55 2017

@author: Matthew
"""

#define lasagna():
#    mince garlic
#    cut tomato
#lasagna()#oversimplified recipe, will not result in actual lasagna

def ux():
    print "Here is a function that listing out printing techniques."
    print 'Single quotes work too!'
    print "I'd  'use' double quotes to encapsulate 'single' quotes in your prints."
    print 'OK "maybe"  one more'
ux()

# Exercise How did you get here today

### Commenting
'''
You should comment before each new section of code and can even comment line 
by line. Aside from that whenever you have a breakthrough comment instructions
on what you did for your future self to remember. Write your comment as though
someone who does not read code would understand what the code is doing from 
your comment. 
'''
# Typically, you just use the # (pound) sign to comment out everything that follows it on that line.

print("Not a comment")
#print("Am a comment")


# Multiple line comments are slightly different. Simply use 3 single quotes before and after the part you want commented.

'''
print("We are in a comment")
print ("We are still in a comment")
'''
print("We are out of the comment")


# Exercise
''' Take the code you created from the functions exercise copy and paste it 
below and then put comments in the code to help you understand what you did 
6 months from now'''

# Basic Math
''' Part of any programming or analytics is basic math. 
We will now combine math functions and print functions. '''

print "I will now do some math:"

print "basic math", 1 + 9/ 2
print "basic math",  10/ 3
print "modelo", 10 % 3
print "division with dec", 10.0 /3.0

print "What about order of operations?"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print (3 + 2 + 1) - (5 + 4 % 2) - 1 / (4 + 6)

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "Example of printing and Math"
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

print (3 ** 4) # 3 to the fourth power

print 'basic boolean', 3<7
print 'basic boolean', 3>7
print 'basic boolean', 1+2<7



# Basic Math functions
# Create your own basic math function  mixing text and the math problem
# Create a boolean function that brings back the text of what you are testing 
# and has an answer of False



#### Variables and Math
'''  A variable is a container to hold a value

# X = 10
# X is a variable that now holds the number 10

# I can say X+1 and get 11

X = 100	
Y = 72	
Z = 14	
	(X-Y)+Z = ? '''
 
#VARIABLES
departments = 100
headcount_by_dept = 15
managers = 92
employees = 1498

# notice how you can concatinate strings with variables
print "There are", departments, " departments in our company"
print "There are only", managers," managers available"
 

# Finish the code EXERCISE
# Lets add some math in our variables with the above code

#VARIABLES
departments = 100
headcount_by_dept = 15
managers = 92
employees = 1498
managers_needed = departments
total_headcount = (departments * headcount_by_dept)+ managers_needed

# total_headcount minus (managers plus employees)
total_headcount_available= 

# employee divided by department

avg_employee_per_dept = 

# Create a print statement that tells you how many managers are needed, what the total headcount is, the headcount 
# available and the average employee per department.


''' EXERCISE
Initial Markup (IMU) is the difference between the cost and selling price of an item when it is first introduced for sale. It is also called Initial Mark On, Markon or Markup. The formula for this calculation is: 
Selling price – cost = Initial Markup Dollars. 
If a buyer brings in a line of jeans with a cost of 25 per pair and initially prices them to sell at 55 per pair, the Initial Markup is 30. 
*Create an IMU calculator''' 
