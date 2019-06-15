###############################################################################
##              FUNCTIONS, PRINTING, MATH, VARIABLES, 3 VALUE LOGIC          ##
###############################################################################
###############################################################################
##                      PYTHON FOR DATA I - UNIT 2
##               MATH AND 3 VALUE LOGIC(IF, THEN, ELSE)
## BASIC MATH
## DATA TYPES
## BOOLEAN
## STRINGS
## PROJECT EXERCISE 
###############################################################################

# BASIC MATH
''' 
Part of any programming or analytics is basic math. 
We will now combine math functions and print functions. 
'''

("I will now do some math:")
1+1
("basic math"), 1 + 9/ 2
("basic math"),  10/ 3
("modelo"), 10 % 3
("division with dec"), 10.0 /3.0

("What about order of operations?")

(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
((3 + 2 + 1) - (5 + 4 % 2) - 1 / (4 + 6))


# CONVERTING DATA TYPES FOR MATH
## Data types
'''
We can only scratch the surface on data types but as you begin to program and
your skill grow you may have deeper questions regarding data types. Here 
are 2 resource that may help with some of those tougher questions.

Data Types
https://realpython.com/python-data-types/

Conversion of data types and structures
https://www.geeksforgeeks.org/type-conversion-python/
'''

a= '100'
b= '50'

c= int(a)+int(b)
d= a+b
(c)
(d)

# Exercise
'''
Add a+b answer 
load into variable c
print results
answer should be 504
'''
a=4
b='500'


## BOOLEAN
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





# Conditionals pineapple pizza debate
## 3 value logic returns TRUE, FALSE or UNKNOWN. This is powerful logic

people = 100.00
pineapple = 49.00
antip =51.00
paying = "Terry"

    
if (pineapple/people)*100 > 50:  
    print ("pineapple does belong on pizza")
else: 
    print ("pineapple does not belong on pizza")


if (pineapple/people) *100 > 50 or paying == "Terry": print ("pineapple does belong on pizza")
else: print ("pineapple does not belong on pizza")


# Multiple filters and conditionals that are covered
weather = "Sunny"
day = "Monday"
time = "5am"
season = "SUMMER"


if weather == "Sunny" and day == "Monday" and time == "5am" and season == "Winter": 
    print("dont garden")
elif weather == "Sunny" and day == "Saturday" and time == "10am" and season == "Spring": 
    print("Garden")
else: print("Need more data")




## EXERCISE
'''
Create a function to evaluate IMU and suggest an action
BONUS : use inputs instead of the hard coded values below

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
##
#IMU evaluation and suggestions.















'''
PROJECT
You may learn things in programming that you cannot apply to your code right 
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






