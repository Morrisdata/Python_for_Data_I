# Python for Data I
# Matthew Morris 
# Matthewmorris.da@gmail.com
# dev2018

############################################################################### 
##             INTRO TO LIST [ ] TUPLES () DICTIONARIES{}                    ##
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
a[-1]       # returns 5 (last element)


## EXERCISE
'''
1. Bring back the first animal
2. Bring back the two middle animals
3. Bring back the last animal
'''
a = ['duck', 'goose', 'fox', 'ox']


#appending
a = [1, 2, 3, 4, 5] 
a[6] = 7       # error because you can't assign outside the existing range
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

family = {'dad':'Dr.Venture', 'mom':'Unknown', 'size':2}
family


# check the length
len(family) # returns 3 (number of key-value pairs)

# use the key to look up a value (fast operation regardless of dictionary size)
family['dad'] # returns 'Dr.Venture'

# add a new entry
family['pet'] = 'scamp'
family

# keys must be unique, so this edits an existing entry
family['pet'] = 'scamp ii'
family['pet']

# delete an entry
del family['pet']

# keys can be strings or numbers or tuples, values can be any type
family['kids'] = ['dean', 'hank'] # value can be a list
family

# useful methods
family.keys() # returns list: ['dad', 'kids', 'mom', 'size']
family.values() # returns list: ['Dr.Venture', ['hank', 'dean'], 'unknown', 2]
family.items() # returns list of tuples:
# [('dad', 'Dr.Venture'), ('kids', ['hank', 'dean']), ('mom', 'unknown'), ('size', 2)]

#1. Print the name of the mom.

#2. Change the size to 5.

#3. Add 'Hank2' to the list of kids. Note-In this tv series the kids are clones

#4. Fix 'hank' and 'dean' so that the first letter is capitalized.

#5 Add to the family dictionary bodygaurd 'Brock'



''' Project Exercise
Finally you can create a dictionary and list to store your skills and scores.
Something you can update and change. Review your project code and notes. How 
can you implement Data structures to help you with your studying?
As you try to write these lists or dictionaries to a file you may have difficulty
without loops...

'''
