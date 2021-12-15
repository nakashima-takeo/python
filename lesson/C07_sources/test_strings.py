
#######################################################
# A bit of introspection...
# what can we access from a string?
 
s = 'This is the test string'
print(s)

print()

# Show a list of string members
# filter out the ones starting with '__'
members_list = []  # create empty list for results
for m in dir(s):  # loop on all members given by dir()
    if m[:2] != '__':  # check the two first characters
        members_list.append(m) # add to the result list
print('String members:')
for m in members_list:
    print(m)

print()

#######################################################
# Let us try a few functions
#######################################################

# We already know format()
s = '{} lives in {}'.format('John', 'Kyoto')
print(s)
print()

#############
# find & replace
s = 'This is the test string'
print('Test string using repr():', repr(s))
print("find 'the':", repr(s.find('the')))
print("find 't':", repr(s.find('t')))
# gives the position of the first occurence
print("find 't':", repr(s.find('t', 9)))# give a start position to search from => skip start 

# rfind that search from end (right) also exists
print()

print("replace 'the' by '0':", repr(s.replace('the', '0')))
print("replace 't' by '0':", repr(s.replace('t', '0')))
# replaces all occurences
print("replace 't' by '0' (2 count):", repr(s.replace('t', '0', 2))) # limit to a number of occurences, here 2

print()

###############
# partition a string that has a separator
s = 'notebook::::1.50'
# '::::' is the separator
# a substring used to separate two fields
print('Test string:', s)
print("Partition using '::::':", s.partition('::::'))
# gives a tuple : (before the separator, separator, after the separator)

print()

###############
# partition a string that has many separators
s = 'notebook;pen;eraser;ruler'
# ';' is the separator
print('Test string:', s)
print('split string:', s.split(';'))
# returns a list containing the elements that were separated


s = 'This is the test string'
print('Test string:', s)
print('split string:', s.split())
# by default split using space
# useful to separate a sentence in words

# you can use it to iterate
for w in s.split():
    print(w)


print()

#############
# remove space or characters at the start or end
# (Create a new string)
# lstrip(<chars>) from start
# rstip(<chars>) from end

# This is the test string
s = '     This is the test string       \n'
print('test string:', s)
# Note that \n make a line break

# We can use the function repr() to show the string representation
# This is a useful function for code introspection
print('test string using repr():', repr(s))
# Then, we can see the spaces and \n

# Let see the results of some calls to lstrip and rstrip

# No arguments
print('New string using repr():', repr(s.lstrip()))
print('New string using repr():', repr(s.rstrip()))
# remove space and break line
# This is useful for removing end of line '\n'
# when reading text lines

# With arguments
print('New string using repr():', repr(s.lstrip('Tisht ')))
print('New string using repr():', repr(s.rstrip('gints\n ')))
# remove all combination of the characters from start or end

# Warning: The next command is not removing the space and prefix This
print('New string using repr():', repr(s.lstrip(' This')))
# it removes all combinaitions of these characters...
# '     This is ' is such a combination.

# Python 3.9 introduces
# removepreffix
# removesufix


# Change case
# Good to compare string without carring the case
print('New string using repr():', repr(s.lower()))
print('New string using repr():', repr(s.upper()))
# see also capitalize, casefold

# Expand tabs 
s = '\tThis is the test\tstring with tabs\n'
print('Test string using repr():', repr(s))
print('New string using repr():', repr(s.expandtabs(tabsize=4))) 
# change tabs \t to 4 spaces

# Check begining and end
s = 'This is the test string'
print('Test string using repr():', repr(s))
print("start with 'This is':", repr(s.startswith('This is'))) 
print("end with 'ing':", repr(s.endswith('ing'))) 
print("end with 'ting':", repr(s.endswith('ting'))) 

########################
# You can check more functions by yourself
# help(str) gives the long help for all members
# help() is another function useful for introspection
# you can access the help of the members of str by
# help(str.member_name)
# the '.' notation to access members

# For example let us check: zfill
# to access the documentation you type
help(str.zfill)

# The definition tells
# zfill(self, width, /)
# in the definition, the parameter 'self' stands for the string itself
# you do not have to write it the '.' notation does it for us
# More on why later...
# / indicates that all arguments before are positional arguments

# Then you can try the function
# to fill with zero up to width 5
print('18'.zfill(5))
# '18'.zfill(5) means that 'self' is '18' and width is 5

# You can check some other members by yourself
# for example: islower

# Googling for members and documentation is also perfectly fine
# str documentation is at https://docs.python.org/3/library/stdtypes.html
# Sites like stack overflow have many Q&A
# ex: https://stackoverflow.com/questions/19103052/python-string-formatting-columns-in-line
# shows how to align field in format
# It is important to know where you can find information
