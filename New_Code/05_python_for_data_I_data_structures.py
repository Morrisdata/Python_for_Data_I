############################################################################### 
##                    PYTHON FOR DATA I - UNIT 5
##                  LISTS [ ] TUPLES () DICTIONARIES{}      
## You have been creating a list of skills and scores lets look at this more
## formally.
###############################################################################

''' 
List can contain integers, characters or a mix of both

list1 = [1,2,3,4,5,6]
list1

list2 = ["soy", "bread", "eggs"]

list3 = [1,5.2,"bread"]

* Lists can contain lists

list4 = ["soy", "bread", "eggs",["corn", "kale", "carrots"]]
list4

* List of things you can do with lists

Delete, Append, Extend, Insert, Populate, Remove, Reverse, 
Sort, Add lists together. 

For now we will focus on creating lists and :

* adding lists together
* append values
* replace a list element
* remove list elements
* exploring data
* sorting data
* slicing data

This is just an intro later you will begin to see how lists can be used with 
data.
'''
### creating
a = [1, 2, 3, 4, 5]     # create lists using brackets
a
		


### slicing
a[0]        # returns 1 (Python is zero indexed)
a[0:3]      # returns [2, 3] (inclusive of first index but exclusive of second)
a[-2]       # returns 5 (last element)


## EXERCISE
'''
1. Bring back the first animal
2. Bring back the two middle animals
3. Bring back the last animal
'''
a = ['duck', 'goose', 'fox', 'ox']
       0        1       2      3
a[1:2]


#appending
a = [1, 2, 3, 4, 5] 
a[5] = 6       # error because you can't assign outside the existing range

a.append(6)     # list method that appends 6 to the end
a
a = a + [0, .5]     # use plus sign to combine lists
a
#checking length
len(a)      # returns 7

#checking type
type(a)     # returns list
type(a[0])  # returns int

#sorting
sorted(a)               # sorts the list
sorted(a, reverse=True) # reverse=True is an 'optional argument'
sorted(a, True)         # error because optional arguments must be named

## EXERCISE
'''
1. Make a list of your favorite foods, or bands
2. display your list
3. add a new value to your list
4. sort your list 
'''
##








## EXERCISE:
'''Create a list of the first names of your family members.
Print the name of the last person in the list.
add a new person to your family make it a celebrity
Change the name of the new person to lowercase using the string method 'lower'.
Sort the list in reverse alphabetical order. '''





# Tuple() is the same as a list but it cannot be changed


# Dictionary{}

family = {'dad':'Goerge Sr.', 'mom':'Gangi', 'size':2}
family


# check the length
len(family) # returns 3 (number of key-value pairs)

# use the key to look up a value (fast operation regardless of dictionary size)
family['dad'] # returns 'Dr.Venture'

# add a new entry
family['pet'] = 'mother'
family

# keys must be unique, so this edits an existing entry
family['pet'] = 'ostrich'
family['pet']

# delete an entry
del family['pet']

# keys can be strings or numbers or tuples, values can be any type
family['kids'] = ['michael', 'lindsey','gob'] # value can be a list
family

# useful methods
family.keys() # returns list: ['dad', 'kids', 'mom', 'size']
family.values() # returns list: ['Goerge Sr.', ['Michael', 'Lindsey','Gob'], 'unknown', 2]
family.items() # returns list of tuples:
# [('dad', 'Goerge Sr.'), ('kids', ['Michael', 'Lindsey','Gob']), ('mom', 'Gangi'), ('size', 2)]

#1. Print the name of the mom.

#2. Change the size to 5.

#3. Add 'Tobias' to the list of kids. 


#4 Add to the family dictionary grandkids 'Goerge Michael and Maeby'

#Writing Dictionaries to .csv


''' Project Exercise
Review your project code and notes. 
can you implement Data structures to help you with your studying?
As you try to write these lists or dictionaries to a file you may have difficulty
without loops

How do you write this to EXCEL?
Uou could attempt export and that is worth a look and you could explore data frames
but that is another story for another time. For now just use this unit to practice
after the next units you may get some ideas how to populate excel with your 
Dictionaries, Lists and Tuples

...

'''

