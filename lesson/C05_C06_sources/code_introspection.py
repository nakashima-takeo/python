# Python has some functions to get information about the code
l = list(range(5))
l_ref=l
l_copy=l.copy()

# We already saw type() 
# type() returns a string 
# containing the type
print(type(l))

# dir() gives a list of attributes
# list of strings 
# attributes of the form __<name>__ are "private"
# we should use the other ones
# you can recognize the functions we saw
print(dir(l)) 

# id gives the "unique id" of an object
print(id(l))
print(id(l_ref)) # reference to same object = same id
print(id(l_copy)) # reference to a different object = different id

# hasattr() checks if an attribute exists
print(hasattr(l, 'sort')) # a list has a function sort

t = 3, 2, 7
print(hasattr(t, 'sort')) # a tuple does not have a function sort

# help() show an extensive help
help(t)
help(id)

