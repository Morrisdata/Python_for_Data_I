# Python for Data I
# Matthew Morris 
# Matthewmorris.da@gmail.com

############################################################################### 
##                    PYTHON FOR DATA I - UNIT 5
##                         LOOPS AND LISTS    
## FOR LOOP
## WHILE LOOP
## LOOPS AND LISTS
###############################################################################
'''
You don't have to do lists but you will eventually want to in order
to avoid hand cramps from so much typing and headaches from the mental
math of basically doing loops manually. 

Loops are a way to reduce code and automate tasks that you would 
repeat over and over. 
A loop is a sequence of instructions that are continually repeated until
a certain condition is reached. 

There are 2 types of loops in python the FOR loop and the WHILE loop
For loops and While loops both allow us to perform an action over and over 
and over and over and over. 

FOR loops will iterate through list and perform its action once for each of 
those items. Lists and strings have a finite length.
So we know how many times a for loop will run based on the length of the list.

WASH
RINSE
repeat twice

A WHILE loop however will continue running and will check conditions to 
determine whether it should run the loop 1 more time. 
WASH
RINSE
until clean
'''
###############################################################################
# FOR LOOP                                                                   ##
###############################################################################
''' 
for x in n:
    do y
x

FOR container IN values:
        do something
In these values we are going to do something and put them in the container
'''
# Using a loop to Upper case your values
for color in ['red', 'blue', 'green']:
    print (color.upper())
color

for color in ['red', 'blue', 'green']:
    print (color.capitalize())

# What is this Loop doing?
for color in ['red', 'blue', 'green']:
    print (str.title(color))
color


# Using Count to see how a loop works
for count in [1, 2, 3]:
    print(count)
    print('Yes' * count)
print('Done counting.')


#In your own words what is happening below run the code and look at output
for color in ['red', 'blue', 'green']:
    if (color) is 'red':
        print ('Red')
    elif(color) == 'blue':
        print ('Blue')
    else: print('Green')
    print(color)


    

## EXERCISE
''' 
1. Run the code below
2. Why did the second for loop not bring back the entire phrase?
3. Change the code to bring back the entire phrase.
'''

for letter in "Python for Data":
    print (letter)
    
print() # what is this doing?
print()

loop = "Loops iterate"

for letter in loop:
    # Only print out the letter i
    if letter == "i":
        print (letter)


## EXERCISE
'''
Remember that list of family members you created 
Try using a loop to put all of their names in upper case
Bonus put the entire loop in a function and call the function.
Could you use input prompts to make this more dynamic?
Would psuedocode help in design and planning? 
'''




#Ranges
# We will be using ranges, randint, and importing to assist with loop examples 

# You can create a list of numbers using range 
list(range(4))
list(range(10))


# Comment up this codes to explain what is happening    
n=(range(6))
for count in n: 
    print(count) 
    print('Yes' * count)




# FOR work an 8 hour day
for count in range(1,9):
    print "Start of hour"
    print "End of hour"
    print str(count) +" hours"
print "Go home you have worked a full 8 hour day."

# Writing results into a list
''' 
Randint will randomly choose 1 of two numbers 0 or 1 for us
The code below is a coin flip simulator. 
This one is using 2 for loops and compressing some code. 
It may take a few passes to read through
this and manipulate it. Keep this as an extra credit assignment'''


from random import randint
num = 100
flips = [randint(0,1) for r in range(num)]
results = []
for object in flips:
        if object == 0:
            results.append('Heads')
        elif object == 1:
            results.append('Tails')
print results

## CHALLENGE 
'''
Count how many flips, how many heads, how many tails
Create a calculation that displays the % of times heads to tails
'''
##


###############################################################################
# WHILE LOOP                                                                   ##
###############################################################################

# WHILE  Work until boss leaves!
''' 
This is a while loop
You are not sure when your boss leaves so you complete a task and then look 
over at thier desk to see if they are gone. 
Once they are gone your weekend starts!!!!
'''

import random
#variables
boss_is_still_working_on_your_review = True
count = 0
#stay at work as long as your boss is working on your review
while boss_is_still_working_on_your_review:	
    print ("Heads down and complete a task!"	)
    print ("When task is finished see if they are gone!")	
    count +=1
    print (str(count) +" task(s) complete, good job!")
    print
    
    #Boss will randomly leave
    if random.randrange(0,10) ==0:
        boss_is_still_working_on_your_review = False
        print ("Go home you hard worker, boss is gone")

# Simpler example
nums = [1,2,3,4,5]
i = 0
while (i <4):
    print (nums)
    i +=1
# Why is this different?  
nums = [1,2,3,4,5]
i = 0
while (i <4):
    print (i)
    i +=1
###############################################################################
##                     LOOPS and LISTS                                       ##
###############################################################################        
LOOPS LISTS

# refresher on Loops
counts = [1,2,3,4,5]	
lunches = ['thai', 'deli', 'pcc', 'sandwich']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters'] # you can put different data types in a list
	
for count in counts:
    print (count)
	
for i in lunches:
	print ("Lunch options: %s" % i)

for i in change:
    print ("I have %r" % i)
	

# Building a list from a loop
'''
1. Create an empty list that will feed into a variable
2.	Use range to get a 0 thru 10 iteration
3.  Append new values to the ist
4. print the list out
'''    
# Example 1

values = []
for i in range(0, 6):
    print ("Adding %d to the list." % i)
    values.append(i)

for i in elements:
	print ("Value was: %d" % i)

# Example two less code	
values2 = range(6)
for i in elements2:
    print ("elements item was: %d" % i)
    
    
''' Summary loops and lists
There are for loops and that is what you want to use 9 times out of 10 because 
they have an end. While loops can go on into oblivion. 
You use loops when you have a repeatable process and you want to reduce code. 
Not sure when you would use a loop? Just code away and when you hit 
something where you think, "I wish there was a way to reduce this code and 
only code it once"...probably going to be a loop. 
For more information on loops checkout the documentation: 
    http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/loops.html'''
    

''' PROJECT EXERCISE
something that has been repeating in the project is if then else reviewing scores 
and recommendations. Can you think of how you might use loops and lists to reduce
the code to review scores and give recommendations?"
Take a look at unit one and working with files. 
Wouldn't it be great if you could use inputs into calculators then have that in
loops and lists to update these files. 
Yes this entire course is a loop, keep running it with your Skills assesment/Quiz/TrainingTracker/...
'''
    
###############################################################################    
##  BONUS Dictionaries and functions with lists                              ##
###############################################################################
    
webster = {

    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}
for items in webster:
    print (webster[items]) 

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for items in a:
    if items % 2== 0:
        print (items)

## EXERCISE
'''
1. create a random list of numbers
2. Bring back only the odd numbers
3. Write into a seperate list called odd
'''
##


##EXERCISE
'''
1. Run the code below
2. Use what you have learned to document what this code is doing
'''
##
def count(numbers):
    total = 0
    for n in numbers:
        if n == 'WA':
            total = total + 1
    return total

x = ['WA', 'ID', 'OR', 'WA','NOTWA','wa', 'WASHINGTON','OR','CA','WA' ]
y = count(x)
print (y)



