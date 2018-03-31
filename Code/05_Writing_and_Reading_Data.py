
''' Read and write data to a file'''
# Open a file or create one if it is not open
a = open("new_file.csv","w+")

# Write a line to the document
a.write("First line in my doc.")
# Close file
a.close()

#Open file and write a record to the file
b = open("new_file.csv","r")
# Read record into a variable
c = b.readlines()
# output results to the screen
print c


# Write several lines to a file and read them
print "Opening the file..."			
target = open("multiline.csv", 'w+')			

# Use Raw_inputs to create 3 lines of in your file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")   # \n is a carriage return
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Close the file."
target.close()





# Find your file and review it
# Close your file and rerun the above code using commas test, 1, blue, 2
# Open file and see how this has behaved


# Next append a file to the end
  # Open the file for appending text to the end
target = open("multiline.csv","a+")
target.write("append_test, 4")
target.close()
target

# Reopen your file and review


# For reference here is examples of taking read and write then putting into loops
def main():  
  # Open a file for writing and create it if it doesn't exist
  f = open("textfile.txt","w+")
  
  # Open the file for appending text to the end
#  f = open("textfile.txt","a+")

  # write some lines of data to the file
  for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
  
  # close the file when done
  f.close()
  
  # Open the file back up and read the contents
  f = open("textfile.txt","r")
  if f.mode == 'r': # check to make sure that the file was opened
    # use the read() function to read the entire file
#     contents = f.read()
#     print contents
    
    fl = f.readlines() # readlines reads the individual lines into a list
    for x in fl:
      print x


''' Read Data From a file
Lets take a look at what the code is going to do. with most code you have to 
be able to read it backwards. Yoda talk. so reading this backwards we are : 
taking a drinks.csv file and reading it using a read_csv functions from 
pd(pandas) and then loading that data into a variable called drinks. 
drinks = pd.read_csv('~/Desktop/DataScience/drinks.csv')
You will want to adjust the link to navigate to where your file is located.'''

# read in the drinks data
import pandas as pd
a = pd.read_csv('~\multiline.csv')
a

# Read a dataset from your desktop
b = pd.read_csv('C:\Users\Matthew\Desktop\DATASETS\RATS.csv')
b

'''PROJECT EXERCISE
You have been rating your skills and evaluating areas of focus needed. 
Review your previous code and determing how you could best write all of your
skills into a csv with your scores.


PART II QUIZ
Using what you have learned design a 
True False and Multiple Choice Python quiz. Store answers in a file
and use conditionals to check if you answered questions correctly. Store graded
quiz in seperate file.'''

''' Next up in Python for Data II we will review how to connect to multiple
data sources, prepare and  analyze data in Python"
