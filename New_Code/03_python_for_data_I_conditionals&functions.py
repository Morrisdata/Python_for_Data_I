###############################################################################
##                INPUT, Arguements and IF THEN ELIF logic                   ##
###############################################################################		

# When you run this you will have a prompt but no directions
	
answer = input() 
answer2 = input('Ask a question...  :')
answer2


## EXERCISE
''' 
review the function below
q1 has not question for a prompt so this will need to be fixed
q2 doesn't even have a input or question
q3 is missing entirely

see if you can fix the code	
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







# We will define 3 functions with examples of arguments:
# print_none, print_one, print_two

def print_none():
    print "Even though this has no arguements it is still important"
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



## EXERCISE
'''
Use input prompts, passing objects into a string and arguements to create
a Calculator that outputs a message after use. If you cannot think of a calculator
you can modify one from above
'''







# Conditionals pineapple pizza debate
people = 100.00
pineapple = 40.00
specials = 
antip =60.00
paying = "Terry"

    
if (pineapple/people)*100 > 50: print "pinapple does belong on pizza"
else: print "pineapple does not belong on pizza"


if (pineapple/people) *100 > 50 or paying == "Terry": print "pinapple does belong on pizza"
else: print "pineapple does not belong on pizza"


weather = "Sunny"
day = "Monday"
time = "5am"
season = "Winter"


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





''' PROJECT EXERCISE
Revisit your previous project and consider how you might use 
If then else, Math, arguements, raw_input and conditionals to update your 
scores, find your averages and give recommendations and what you can add to
your resume or what you need to practice.
Could you use input with If then else to create a Quiz? Maybe later you can
begin grading the quiz.
'''


