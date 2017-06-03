# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 12:58:34 2017

@author: Matthew
"""

import psycopg2 as psy
import sys
import pandas as pd
 

#Define our connection stri
conn_string = "host='analyticsga.cuwj8wuu6wbh.us-west-2.rds.amazonaws.com'dbname='iowa_liquor_sales_database' user='analytics_student' password='analyticsga'"
 
# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)
 
# get a connection, if a connect cannot be made an exception will be raised here
conn = psy.connect(conn_string)
 
# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"
 
df = pd.read_sql_query('select * from products', conn)
df


#RESET - Fix the code table name is products
df = pd.read_sql_query('', conn)

df.head() # print the first 30 and last 30 rows
df.head(3) # print the first 3 rows
df.head() # print the first 5 rows
df.tail() # print the last 5 rows
df.columns # column names (which is "an index")
df.dtypes # data types of each column
df.shape # number of rows and columns

# select a columns
df[['category_name','item_description']] # select one column
df.category_name # select one column using the DataFrame attribute
df.describe() # describe all numeric columns
df.describe(include=['object']) # describe all object columns
df.describe(include='all') # describe all columns
df.shelf_price.describe() # describe a single column
df.shelfprice.mean() # only calculate the mean
df.category_name.value_counts() # most useful for categorical variables


df.shelf_price.value_counts() # can also be used with numeric variables

'''
EXERCISE ONE
'''

# read sales into a DataFrame called df and be sure to limit rows to 1000 in your SQL
# print head and the tail

# print the 'item' Series

# Use describe to evaluate the Data

# use describe only on the 'total' column

# calculate the 'total' mean

# count the number of occurrences of each 'item' value

low_items= df.shelf_price < 8.00 # create a Series of booleans...
low_items

df[low_items] # use the above series created to filter rows

df[df.shelf_price < 8.00] # or, combine into a single step

df[df.shelf_price < 8.0].item_description # select one column from the filtered results

df[df.shelf_price < 8.00].item_description.value_counts() # value_counts of resulting Series

# boolean filtering with multiple conditions
df[(df.shelf_price < 8.00) & (df.category_name=='FLAVORED VODKA')] # ampersand for AND condition

df[(df.shelf_price < 8.00) | (df.proof > 60)] # pipe for OR condition

df.sort('category_name') # sort a DataFrame by a single column

# sorting
df.category_name.order() # sort a column
df.sort('category_name', ascending=False) # use descending order instead


# filter 'vendor' to only include 'Jim Beam Brands'

# filter 'vendor' to only include 'Jim Beam Brands' with shelf_price > 10

# Using bottle price and shelf price calculate the IMU, sort from highest IMU to lowest

