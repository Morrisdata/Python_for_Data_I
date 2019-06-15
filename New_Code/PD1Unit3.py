# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:58:47 2019

@author: Matthew
"""

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
# Commenting            
# Vocabulary            
# Basic Coding Concepts 
# Printing              
# Passing Variables     
# mkdir()
# import
# getcwd()
# chdir()
# open file
# Read file
# write to file
# append to file
# write to multiple lines
# write to multiple columns
# close()
# listdir()
# shutil(source,destination)



import os
os.getcwd

import os
from pathlib import Path

path = Path('//Users//Matthew//Desktop//GA//00_DATA_SETS//DEV')
os.chdir(path)
# Commenting            
# Vocabulary            
# Basic Coding Concepts 
# Printing              
# Passing Variables     
# mkdir()
# import
# getcwd()
# chdir()
# open file
# Read file
# write to file
# append to file
# write to multiple lines
# write to multiple columns
# close()
# listdir()
# shutil(source,destination)
# inputs
# functions
# Math functions and arguments
# If,Then, Else

t = open("python_skill_builder.csv", 'w+')
u1=input('Commenting:')  
u2=input('Vocabulary:')
u3=input('Basic Coding Concepts:')
u4=input('Printing:')
u5=input('Passing Variables:')
u6=input('Mkdir:')
u7=input('Import:')
u8=input('Getcwd:')
u9=input('Chdir:')
u10=input('Open file:')
u11=input('Read file:')
u12=input('Write to a file:')
u13=input('Append to a file:')
u14=input('Write mulitple lines:')
u15=input('Write multiple columns:')
u16=input('close():')
u17=input('listdir():')
u18=input('shutil():')
u19=input('inputs:')
u20=input('Functions:')   
u21=input('Math input and functions:')
u22=input('if then else:')


line1 ="SKILLS, LEVEL"
line2 ="Commenting,"+u1
line3 ="Vocabulary,"+u2
line4 ="Basic Coding Concepts,"+u3
line5 ="Printing,"+u4
line6 ="Passing Variables,"+u5
line7 ="mkdir(),"+u6
line8 ="import,"+u7
line9 ="getcwd(),"+u8
line10 ="chdir(),"+u9
line11 ="open file,"+u10
line12 ="read file,"+u11
line13 ="write to file,"+u12
line14 ="append to file,"+u13
line15 ="write to multiple lines,"+u14
line16 ="write to multiple columns,"+u15
line17 ="close(),"+u16
line18 ="listdir(),"+u17
line19 ="shutil(),"+u18
line20 ="inputs,"+u19
line21 ="functions,"+u20
line22 ="Math functions and arguments,"+u21
line23 ="if then else,"+u22
## line24 =(int(u1)+int(u2))

t.write(line1)
t.write("\n")   # \n is a carriage return that we are writing to file
t.write(line2)
t.write("\n")
t.write(line3)
t.write("\n")
t.write(line4)
t.write("\n")
t.write(line5)
t.write("\n") 
t.write(line6)
t.write("\n")
t.write(line7)
t.write("\n")
t.write(line8)
t.write("\n")
t.write(line9)
t.write("\n")
t.write(line10)
t.write("\n")
t.write(line11)
t.write("\n")
t.write(line12)
t.write("\n")
t.write(line13)
t.write("\n")
t.write(line14)
t.write("\n")
t.write(line15)
t.write("\n")
t.write(line16)
t.write("\n")
t.write(line17)
t.write("\n")
t.write(line18)
t.write("\n")
t.write(line19)
t.write("\n")
t.write(line20)
t.write("\n")
t.write(line21)
t.write("\n")
t.write(line22)
t.write("\n")
t.write(line23)
t.write("\n")
## t.write(line24)
## t.write("\n")
t.close()

a = open("python_skill_builder.csv","r")
b = a.readlines()
a.close()
print (b)