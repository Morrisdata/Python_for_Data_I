# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:58:47 2019

@author: Matthew
"""

''' PROJECT EXERCISE 
Remember the first exercise. We are going to do this again but this time
load that information into a file. Use this unit to help you:
    
Create a file that lists all the skills you have learned so far
rate yourself for each skill in a seperate column next to the skill
0 = Don't know
1 = Aquiring knowledge
2 = Can apply with 80% help from Google
3 = Can apply with 20% help from Google
4 = Can teach <20% help from Google
5 = Can design, review, optimize
What is your average score?
What areas are you doing great in, what areas do you need to study?
This Project will grow and be designed and redesigned several different ways
as you progress and revist.'''
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

t = open("multiline.csv", 'w+')

line1 = "SKILLS, LEVEL"
line2 = "Commenting, 5"
line3 = "Vocabulary, 5"
line4 = "Basic Coding Concepts, 5"
line5 = "Printing,5"
line6 = "Passing Variables, 5"
line7 = "mkdir(), 2"
line8 = "import, 3"
line9 = "getcwd(), 2"
line10 ="chdir(),2"
line11 ="open file,2"
line12 ="read file,2"
line13 ="write to file,2"
line14 ="append to file,2"
line15 ="write to multiple lines,3"
line16 ="write to multiple columns,5"
line17 ="close(), 3"
line18 ="listdir(),3"
line19 = "shutil(),2"

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
t.close()

a = open("multiline.csv","r")
b = a.readlines()
a.close()
print (b)