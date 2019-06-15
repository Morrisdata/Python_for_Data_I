# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:58:47 2019

@author: Matthew
"""

''' PROJECT EXERCISE
Finally you can create a dictionary and list to store your skills and scores.
Something you can update and change. Review your project code and notes. How 
can you implement Data structures to help you with your studying?
As you try to write these lists or dictionaries to a file you may have difficulty
without loops.... 
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
u2=input('Commenting:')  
u3=input('Vocabulary:')
u4=input('Basic Coding Concepts:')
u5=input('Printing:')
u6=input('Passing Variables:')
u7=input('Mkdir:')
u8=input('Import:')
u9=input('Getcwd:')
u10=input('Chdir:')
u11=input('Open file:')
u12=input('Read file:')
u13=input('Write to a file:')
u14=input('Append to a file:')
u15=input('Write mulitple lines:')
u16=input('Write multiple columns:')
u17=input('close():')
u18=input('listdir():')
u19=input('shutil():')
u20=input('inputs:')
u21=input('Functions:')   
u22=input('Math input and functions:')
u23=input('if then else:')


line1 ="SKILLS, LEVEL"
line2 ='Commenting'+u2
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
line24a =(int(u2)+int(u2))
line24 =str(line24a)

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
t.write(line24)
t.write("\n")
t.close()

a = open("python_skill_builder.csv","r")
b = a.readlines()
a.close()
print (b)