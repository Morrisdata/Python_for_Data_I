# Python for Data I
# Matthew Morris 
# Matthewmorris.da@gmail.com
# dev2018
###############################################################################
##                 FUNCTIONS, PRINTING, MATH, VARIABLES                      ##
###############################################################################

'''
functions are a great way to consolodate several steps into one function that
you can call over and over again in different parts of your code
'''

#define lasagna():
#    mince garlic
#    cut tomato
#lasagna()#oversimplified recipe, will not result in actual lasagna

def ux():
    print ("Here is a function that listing out printing techniques.")
    print ('Single quotes work too!')
    print ("I'd  'use' double quotes to encapsulate 'single' quotes in your prints.")
    print ('OK "maybe"  one more')
ux()
 
    
print  ("not part of ux")

## Exercise 
# How did you get here today?
##


### Commenting
'''
We briefly looked at commenting in section 1. 

You should comment before each new section of code and can even comment line 
by line. Aside from that whenever you have a breakthrough comment instructions
on what you did for your future self to remember. Write your comment as though
someone who does not read code would understand what the code is doing from 
your comment. 
'''
# Typically, you just use the # sign to comment out everything that follows it on that line.

print("Not a comment")
#print("Am a comment") notice using the # to comment out code you don't want to run


''' 
Multiple line comments are slightly different. 
Simply use 3 single quotes before and after the part you want commented.
'''

'''
print("We are in a comment")
print ("We are still in a comment")
'''
print("We are out of the comment")


## Exercise
''' 
Take the code you created from the functions exercise copy and paste it 
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
a[0].upper()+a[:-1] #Uppercase of first letter in word

# checking length
len(a)      # returns 5 (number of characters)

## EXERCISE
'''
Create a function called proper, write your first name in all lowercase into Variable 'first' and your last 
name into variable 'last' Combine your name together with upper case for first 
letter of your first name and upper case for first letter of your last name 
ie Terry Smith
'''

# %r, %d, %s Passing objects into text
a = 'cats'
b = 'dogs'
c = 5

("I have %d %r and %d %r") %(c,b,c,a)



# MATH
''' 
Part of any programming or analytics is basic math. 
We will now combine math functions and print functions. 
'''

("I will now do some math:")

("basic math"), 1 + 9/ 2
("basic math"),  10/ 3
("modelo"), 10 % 3
("division with dec"), 10.0 /3.0

("What about order of operations?")

(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
((3 + 2 + 1) - (5 + 4 % 2) - 1 / (4 + 6))


'''
BOOLEAN logic bring back TRUE FALSE or UNKNOWN
Which can be extremely valuable in creating actionable reports
'''

("Is it true that 3 + 2 < 5 - 7?")

(3 + 2 < 5 - 7)

("Example of printing and Math")
("What is 3 + 2?", 3 + 2)
("What is 5 - 7?", 5 - 7)

("Oh, that's why it's False.")

("How about some more.")

("Is it greater?", 5 > -2)
("Is it greater or equal?", 5 >= -2)
("Is it less or equal?", 5 <= -2)

(3 ** 4) # 3 to the fourth power

('basic boolean', 3<7)
('basic boolean', 3>7)
('basic boolean', 1+2<7 ,"tests")



## EXERCISE
# Create your own basic math function  mixing text and the math problem
# Create a boolean function that brings back the text of what you are testing 
# and has an answer of False
##




# Variables and Math
'''  A variable is a container to hold a value
# X = 10
# X is a variable that now holds the number 10
# I can say X+1 and get 11
X = 100	
Y = 72	
Z = 14	
	(X-Y)+Z = ? '''
 
# VARIABLE EXAMPLE
departments = 100
available_headcount_by_dept = 15
current_managers = 90
current_employees = 1498

# print of just values in variables
print(departments)
print(available_headcount_by_dept)
print(current_managers)
print(current_employees)

# notice how you can concatinate strings with variables
print ("There are", departments, " departments in our company")
print ("There are only", current_managers," managers available")
 

# Finish the code EXERCISE
# Lets add some math in our variables with the above code

#VARIABLES
departments = 100
available_headcount_by_dept = 15
current_managers = 92
current_employees = 1498
managers_needed = departments
total_headcount = (departments * available_headcount_by_dept)+ managers_needed

# total_headcount minus (managers plus employees)
total_available_headcount = total_headcount-(current_managers + current_employees)

# employee divided by department

avg_employee_per_dept = 

# Create a print statement that tells you how many managers are needed, 
# what the total headcount is, the headcount 
# available and the average employee per department.







''' EXERCISE
Initial Markup (IMU) is the difference between the cost and selling price of an 
item when it is first introduced for sale. It is also called Initial Mark On, Markon or Markup. 
The formula for this calculation is: 
Selling price – cost = Initial Markup Dollars. 
If a buyer brings in a line of jeans with a cost of 25 per pair and initially 
prices them to sell at 55 per pair, the Initial Markup is 30. 
*Create an IMU calculator''' 


selling_price = 55
cost = 25
IMU = selling_price - cost
print "Your IMU is :", IMU







'''
PROJECT
You will learn things in programming that you cannot apply to your code right 
away but you can see where they may be useful.
you can create pseudo code!!!
This is not working code but logic a sketch and wireframe of what you want to
do. This can be a simple as typing out what you want a program to do or actually
keying out a structure for your code logic. 

Think about your Python quiz or program how can you take what you learned in 
Unit 1 and in Unit 2 and use them to begin creating a quize or reviewing your skills

remember psuedo code does not have to run but it gives you a nice outline

Write out your thoughts below about how you would start tackling your project
'''
