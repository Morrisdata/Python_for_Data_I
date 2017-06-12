# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 09:09:01 2017

@author: Matthew
"""

#You can create a list of numbers using range
list(range(4))
list(range(10))

#Create a range  of 100


''' Loops and Lists
For and While loop
Coin toss example
For loop
While loop Creating list of products
For and While loop
Loops are a way to reduce code and automate tasks that you would repeat over and over. 
A loop is a sequence of instructions that are continually repeated until
a certain condition is reached. 
For loop examples
An item of data is retrieved or changed
Then a condition is checked to see if all criteria has been met
if not the process is repeated. 
We do this all the time in life 
Shampoo directions
Rinse
Wash
Rinse
Repeat until clean 
There are 2 types of loops in python the FOR loop and the WHILE loop
For loops and While loops both allow us to perform an action over and over 
and over and over and over. 
for loops will iterate through list and perform its action once for each of those items
lists and strings have a finite length
So we know how many times a for loop will run based on the length of the list
A while loop however will continue running and will check conditions to determine whether it should run the loop 1 more time. 
Work and 8 hour day For loop
So you will work 8 hours and for every 1 hour you work 
you will look ask have I worked 8 hours yet? '''

for count in range(1,9):
    print "Start of hour"
    print "End of hour"
    print str(count) +" hours"
print "Go home you have worked a full 8 hour day."

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

#BONUS Excercise - come back to this code and update it to count the number of 
# flips. Do some math to bring back results that show the % of times heads and the % of times tails

# Work until boss leaves!
''' This is a while loop
You are not sure when your boss leaves so you complete a task and then look 
over at thier desk to see if they are gone. Once they are gone your weekend starts!!!!'''

import random
#variables
boss_is_still_working_on_your_review = True
count = 0
#stay at work as long as your boss is working on your review
while boss_is_still_working_on_your_review:	
    print "Heads down and complete a task!"	
    print "When task is finished see if they are gone!"	
    count +=1
    print str(count) +" task(s) complete, good job!"
    print
    
    #Boss will randomly leave
    if random.randrange(0,10) ==0:
        boss_is_still_working_on_your_review = False
        print "Go home you hard worker, boss is gone"

        # couple more examples
n=(range(6))
for count in n: 
    print(count) 
    print('Yes' * count)

for count in [1, 2, 3]:
    print(count)
    print('Yes' * count)
print('Done counting.')

for color in ['red', 'blue', 'green']:
    print(color)
    
''' summary loops and lists
There are for loops and that is what you want to use 9 times out of 10 because 
they have an end. While loops can go on into oblivion. '''
You use loops when you have a repeatable process and you want to reduce code. If youre not sure when you would use a loop just code away and when you hit something where you think, "I wish there was a way to reduce this code and only code it once...probably going to be a loop." For more information on loops checkout the documentation: http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/loops.html
