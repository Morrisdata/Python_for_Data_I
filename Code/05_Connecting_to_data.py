# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 09:41:04 2017

@author: Matthew
"""

''' Read Data From a file
Lets take a look at what the code is going to do. with most code you have to 
be able to read it backwards. Yoda talk. so reading this backwards we are : 
taking a drinks.csv file and reading it using a read_csv functions from 
pd(pandas) and then loading that data into a variable called drinks. 
drinks = pd.read_csv('~/Desktop/DataScience/drinks.csv')
You will want to adjust the link to navigate to where your file is located.'''

# read in the drinks data
import pandas as pd
drinks = pd.read_csv('~/Desktop/DataScience/drinks.csv')
drinks

# Connect to a database and run SQL
''' You may need to install psycopg2 from your CMD line type the following
sudo apt-get install libpq-dev python-
pip install psycopg2
connect
connect and run a query
Connect to Postgres
Connect to the Postgres Database using authentication. Catch and print a connection error if one occurs.
'''
#!/usr/bin/python
import psycopg2
import sys
 

#Define our connection string
conn_string = "host='analyticsga.cuwj8wuu6wbh.us-west-2.rds.amazonaws.com'dbname='iowa_liquor_sales_database' user='analytics_student' password='analyticsga'"
 
 
# print the connection string we will use to connect
print "Connecting to database\n ->%s" % (conn_string)
 
# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)
 
# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"
 

#### Perform a Select
''' This example shows how to connect to a database, and then obtain and use a 
cursor object to retrieve records from a table.'''

import psycopg2
import sys
import pprint
import pandas 
 

#Define our connection stri
conn_string = "host='analyticsga.cuwj8wuu6wbh.us-west-2.rds.amazonaws.com'dbname='iowa_liquor_sales_database' user='analytics_student' password='analyticsga'"
 
# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)
 
# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)
 
# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"
 
df = pd.read_sql_query('select * from products', conn)
df
# retrieve the records from the database
# records = cursor.fetchall()
 
# print out the records using pretty print
# note that the NAMES of the columns are not shown, instead just indexes.
# for most people this isn't very useful so we'll show you how to return
# columns as a dictionary (hash) in the next example.
# records

''' EXERCISE - Explore Iowa Liquor Sales Database
Adjust the code to review other tables in the Iowa liquor sales database:
stores
products
sales (CAUTION this table will run forever change your SQL to have LIMIT of 100 records)
'''

#stores

# products

# sales

# You may be thinking to yourself "Awesome! I'm connecting to AWS I'm running SQL, 
# I'm seeing data this is great but... now what? We will want to explore the 
# data further using Pandas before we do let's do a review In the next exercise you will: 
# Define a function called mem and print off all of the things you have learned so far in this class. 
# Do this strictly from memory. 

# Define another function called rev and review the syllabus and exercises to create a list of things that were covered. 

# Define a function that prints everything you learned from memory

#### Review 
'''Create you own examples of code for each section that has been covered in this series so far. 
As you go through each section think about ways it may help you with data you would retrieve'''


