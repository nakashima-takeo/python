print("""
##############################################################
# Create a dictionary 
##############################################################
""")

# Use curly braces
# key : value
d1 = {'name' : 'John', 'age' : 32, 'city' : 'Kyoto', 'user_id' : 125}
print('d1 : ', d1)

print()

# Use the dict() constructor
# Note the keys and values may mix different types
# keys are immutable
d2 = dict([(1, 24), ('a number', 7), (2, 'test'), ((0,1), 32)])
print('d2 : ', d2)

print()

# dictionary comprehension
# notice the curly brace {} and the column : 
# the column : separate the key and value
d3 = {x : 1 + x + 0.5 * x**2 for x in range(10)}
print('d3 : ', d3)

print()

# Empty dictionary
# This is why you have to use set() to create an empty set and not {}
d_empty_1 = {}
d_empty_2 = dict()
print('d_empty_1 : ', d_empty_1)
print('d_empty_2 : ', d_empty_2)

print("""
##############################################################
# Access values
##############################################################
""")

# Access by key
print("User {}: {} ({}) living in {}".format(d1['user_id'], d1['name'], d1['age'], d1['city']))

print()

# Modify a value using the key
# Entries can be modified
d1['city'] = 'Tokyo'
print("User {}: {} ({}) living in {}".format(d1['user_id'], d1['name'], d1['age'], d1['city']))

print()

# Add a pair key value
d1['job'] = 'driver'
print('d1 : ', d1)

print()

# Remove an element
del d1['age']
print('d1 : ', d1)

print()

# get the size of a dictionary
print('size of d1:', len(d1))


print("""
##############################################################
# Working with dictionaries
##############################################################
""")

print('d1=', d1)

print()

# Check for a key
print('is age in d1', 'age' in d1)
print('is user_id in d1', 'user_id' in d1)

print()

# Update a value if the key exists
print('user_id=', d1['user_id'])
if 'user_id' in d1:
    d1['user_id'] += 1 # This is equivalent to d1['user_id'] = d1['user_id'] + 1
                       # += , *=, -= and /= also exists
else:
    print('key unknown')
print('user_id=', d1['user_id'])

print("""
# Get a list of the keys of d1
# use the list() function
# iterate on the keys and display the values
""")
keys_list = list(d1)
print('keys_list:', keys_list)

print()

for k in keys_list:
    print('{} <=> {}'.format(k, d1[k]))

print("""
# Dictionary are not ordered
# but you can order the list before iterating
""")
sorted_keys_list = sorted(list(d1)) # create a sorted list
print('sorted_keys_list:', sorted_keys_list)
print()

for k in sorted_keys_list:
    print('{} <=> {}'.format(k, d1[k]))

print("""
# Python dictionaries have a function to get the key value pairs
""")
for k,v in d1.items():
    print('{} <=> {}'.format(k, v))

print()

####################################
# Optional: More advanced topic

# Can we order a dictionary according to the values when iterating ?

# Imagine we want to display the following dictionary by increasing age
d_age = {'John' : 35, 'Albert' : 27, 'Claire' : 31, 'Zak' : 2}

# We use items() to create a list of tuples (key, value)
print(d_age.items()) 

# The sorted function sort the tuples using the first element of the tuples first
print(sorted(d_age.items()))


# This is not what we want...

# The sorted function has a key argument
# This argument expect a function
# That function computes for each element, the value used for sorting
# Here it will get a tuple (name, age)

# We can create a function that gets such tuple and returns the age
def sorting_help(t):
    return t[1]

# And use it in sorted
# note that we don't call the function but just give its name
# there are no parenthesis
print(sorted(d_age.items(), key=sorting_help))

# This works but we have to prepare a full function definition
# The statement is not self explanatory anymore

# In python it is possible to define "small functions"
# with a convenenient syntax for such cases
# lambda x : <expression (using x)>
# lambda is a new keyword
# Here we can define the function for the key this way
# given x it returns x[1] 
print(sorted(d_age.items(), key=lambda x : x[1]))

# We can put that together to iterate on the dictionary 
# in increasing age
for k,v in sorted(d_age.items(), key=lambda x : x[1]):
    print(k, v)


