###############################
# This is a script about tuples
###############################

###############################
# 1 - Create tuples

###############################
# Multi element tuple:

# tuple literal syntax 1 
t = (4.0, 5.0, 10.0)
print("t:", t)
print("t is a", type(t))
# len() returns the length of a tuple
print("t has length ", len(t))
print()


# tuple literal syntax 2
t = 4.0, 5.0, 10.0
print("t:", t)
print("t is a", type(t))
print()

# Convert a list to a tuple
l = [4.0, 5.0, 10.0]
print("l:", l)
print("l is a", type(t))
t = tuple(l) 
print("t:", t)
print("t is a", type(t))
print()

###############################
# Single element tuple:

# the syntax 1 does not work
t = (4.0) # This is a float within parenthesis
print("t:", t)
print("t is a", type(t))

t = (4.0,) # This is a tuple
print("t:", t)
print("t is a", type(t))
print()

# the syntax 2 works fine
t = 4.0, 
print("t:", t)
print("t is a", type(t))
print()

###############################
# Create an empty tuple:
t = () 
print("t:", t)
print("t is a", type(t))
print()

t = tuple()
print("t:", t)
print("t is a", type(t))
print()

###############################
# 2 - Use tuples

###############################
# Tuples may contain elements of different types
t = (1.0, "test", [1.0, -5.0], 12, (4,2), "previous element is a tuple", 3.0)
print("t:", t)
print("t is a", type(t))
print()

###############################
# Element can be accessed with indexing

print("t[0]=", t[0]) # access first element
print("t[1:3]=", t[1:3]) # slice of elements from 1st (included) to 3rd (excluded)
print("t[:4]=", t[:4]) # elements up to 4th (excluded)
print("t[2:]=", t[2:]) # from 2nd to end
print("t[-1]=", t[-1]) # last from end
print("t[-2:]=", t[-2:]) # from second last from end to end
print("t[:-2]=", t[:-2]) # from start to second last from end (not included) 
print()


print("t[2][0]=", t[2][0]) # access the element 2 that is a list then the element 0 of that list
print("t[4][1]=", t[4][1]) # access the element 4 that is a tuple then the element 1 of that tuple
print("t[1][-1]=", t[1][-1]) # access the element 1 that is a string then the last character of that string
print()

###############################
# A tuple is immutable => cannot change an elmement 
l = [4.0, 5.0, 10.0]
t = tuple(l) 
print("l:", l)
l[1] = 0.0
print("l:", l)
print("t:", t)
t[1] = 0.0 # This will make an error and the script will stop
# The error message is: 
# TypeError: 'tuple' object does not support item assignment
print("t:", t) # this will not be executed
