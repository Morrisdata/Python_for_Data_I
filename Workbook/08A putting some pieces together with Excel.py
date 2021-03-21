# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 08:21:36 2021

@author: msmorris
"""

# INTRO
'''
This is just a brief introduction to get you started. There is a lot more that you
can do. The approach shared here is just a quick version I put together, if you have
time and a plan you can automate most anything. 
'''

# PYTHON FOR DATA I PUTTING IT ALL TOGETHER WITH EXCEL
'''
Python libraries when working with Excel
openpyxl
The recommended package for reading and writing Excel 2010 files (ie: .xlsx)

xlsxwriter
An alternative package for writing data, formatting information and, in particular, charts in the Excel 2010 format (ie: .xlsx)

pyxlsb
This package allows you to read Excel files in the xlsb format.

pylightxl
This package allows you to read xlsx and xlsm files and write xlsx files.

xlrd
This package is for reading data and formatting information from older Excel files (ie: .xls)

xlwt
This package is for writing data and formatting information to older Excel files (ie: .xls)

xlutils
This package collects utilities that require both xlrd and xlwt, including the ability to copy and modify or filter existing excel files.
NB: In general, these use cases are now covered by openpyxl!

Csv
basic read write for .csv files

When working with Data you will also use Numpy, Pandas and quite a few more
'''

#GETTING SET UP
'''
We will be using openpyxl because it does not come directly with python we will need
to install it  using pip
'''
pip install openpyxl 
# establish your cwd
import os
cwd = "C:\\Users\\msmorris\\Documents\\PythonScripts\\PythonForData01\\"
os.chdir(cwd)



#as noted you may need to restart kernal for this to work
#Read a spreadsheet from the workbook
import os, openpyxl as xl, pandas as pd
files = os.listdir()
#Review what is in openpyxl
help(xl)

# Prototype of a very simple read and write to Excel
''' 
you will need to have the basic_example.xlsx in your cwd for this to work
'''

def load_file():
    # create global variables that will be used in other functions
    # file name
    global file
    # workbook obj
    global wb
    # worksheets 
    global wb_sheets
    # 
    
    global loc
    print("Current directory\n", cwd)
    print("Available files\n", files)
    file = input("Enter Name of file you would like to open: \n")
    loc = "C:\\Users\\msmorris\\Documents\\PythonScripts\\PythonForData01\\"+ file
    wb = xl.load_workbook(file)
    wb_sheets= wb.sheetnames
    print("Sheets available in workbook: \n",wb_sheets)


#explore and get informatino from the spreadsheet
def exp_sheets():
    global req
    
    # active sheet to object
    global sheet_obj
    
    # get # of rows and columns
    global rows
    global columns
    
    req = (input("what sheet would you like info for? {}\n".format(wb_sheets)))
    #make sheet active
    wb.active = wb.sheetnames.index(req)

    sheet_obj = wb.active 
    

    rows = sheet_obj.max_row
    columns = sheet_obj.max_column
     # Loop will print all columns name 
    
    headers= [] 
    for i in range(1, columns + 1): 
        cell_obj = sheet_obj.cell(row = 1, column = i) 
        headers.append(cell_obj.value) 
        #output    
    print("HEADERS\n", 
       headers, 
       120*"=","\n"+
      "Number of Columns : ", columns, "\n"+
      "Number of Rows : ",rows,"\n")

def view_obj():
    df = pd.DataFrame(sheet_obj.values)
    print(df)

def menu():
    menu = int(input("1 to make more changes 2 to close out:  "))
    if menu == 1:
        exp_sheets()
        view_obj()
        change_val()
    else:
        exit
#move sheet to data frame and create conditional input change
def change_val():
    df = pd.DataFrame(sheet_obj.values)
    col = int(input("Enter column to test : "))
    ctrl = int(input("what value should it equal: "))
    col2 = int(input("What column would you like to change: "))
    new_val = input("What new value you would you like entered: ")
    df.loc[df[col]== ctrl, [col2]] = new_val
    df.to_excel(file, sheet_name = req, index_label=False, index=False, header=False)
    menu()
    
def start():
   load_file()
   exp_sheets()
   view_obj()
   change_val() 
    
start()

#UPGRADES What to add
# Add menu item to see results 
# Logic for Change value is very basic can you make it more complex.
# Create a field that is a formula from 2 other fields
# How to write to a specific sheet
# How to do all of this just using Pandas
# How to do all of this just using Openpyxl
# Rather than using Index for change value logic can there be readible content?
# Changing Formatting
# Creating split screen for input and output
# . . . 

    
    

