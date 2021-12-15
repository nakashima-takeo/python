print("""
 This script shows the operations that can be applied to sequences
 It is illustrated using lists (mutable sequence)
 Many operations are also supported by tuples (immutable sequences) 
""")

# Create example lists
l1 = [1.0, 3.0, 2.0]
l2 = [5.0, 2.0]

print("l1 = ", l1)
print("l2 = ", l2)

print("""
############################
 Common operations
 Lists and Tuples 

 Indexing =>  see previous scripts
 len() => see previous scripts
""")

# Test if element is in the list or not
# New keyword "in"
print("3.0 in l1 =>", 3.0 in l1)
print("3.0 not in l1 =>", 3.0 not in l1)

# Concatenate list 
print("l1 + l2 =>", l1 + l2)

# concatenate with self
print("3 * l1 =>", 3 * l1)
print("l1 * 3 =>", l1 * 3)

# Create a longer example list
l3 = l1 + l2
print("Longer list => l3 = ", l3)

# Step indexing => not in previous scripts
# start:end:step
# Try on some list to understand what it does.
print("l3[1:5:2] = ", l3[1:5:2])

# Extrema
# these functions are used like len()
print("min(l3) = ", min(l3))
print("max(l3) = ", max(l3))

# Find the first occurence of a value
# This is a function provided with the dot syntax
# <variable_name>.<function_name>(<arguments>)
print("l3.index(2.0) = ", l3.index(2.0))
# same but within a range
# value, start, end
print("l3.index(2.0, 3, 5) = ", l3.index(2.0, 3, 5))

# Counts the occurence of an element
print("l3.count(2.0) = ", l3.count(2.0))

# Sort the elements
# it creates a new sorted sequence
# it does not modify the original sequence
l4 = sorted(l3)
print("l4 = sorted(l3) = ", l4)

print("""
############################
 Operation for mutable sequences only
 Lists have them
 Tuples do not have them
""")

# Example list
print("Example list => l3 = ", l3)

# assign a value  
# Only for lists as tuples are immutable
l3[0] = 5.0
print("Set element 0 to 5.0 => l3 = ", l3)

# assign a slice of values
l3[3:5] = (1.0, -1.0)
print("change elements 3 and 4 =>  l3 = ", l3)

# delete a slice of values
# del is a new keyword
del l3[1:3]        # same as l3[1:3] = []
print("delete element 1 and 2 => l3 = ", l3)

# Add an element at the end
l3.append(7.0)
print("append 7.0 at the end => l3 = ", l3)

# Add the content of another sequence type at the end
# it can be a list
l3.extend([3.0, 5.0, -7.0])
print("append list l3 = ", l3)
# it can be a tuple
l3.extend((3.0, 5.0, -7.0))
print("append tuple l3 = ", l3)

# insert an element at a given index
l3.insert(4, 0.0) # same as l3[4:4]=0.0
print("insert element 0.0 at 4 => l3 = ", l3)

# Retrieve an element by index and remove it
# by dfault remove the last one [-1] if no argument is given
removed_element = l3.pop(2)
print("Remove element 2 => l3 = ", l3)
print("removed_element = ", removed_element)

# Remove the first occurence of that element
l3.remove(7.0)
print("Remove the first 7.0 => l3 = ", l3)

# Change the order "in place" 
# "in place" means that no new list is created
# the actual list is modified
l3.reverse()
print("Reverse the list => l3 = ", l3)

# Shallow copy
# copy the content
# see lecture
l4 = l3.copy()  # same as l4 = l3[:]
print("shallow copy of l3 => l4 = ", l4)

# copy
# just "copy the reference"
# see lecture
l5 = l3
print("copy of l3 => l5 = ", l5)

# clear content
l3.clear()
print("clear the content of l3 => l3 = ", l3)

# See how copy and shallow copy behaves
# see lecture
print("Look at shallow copy of l3 after clearing l3 => l4 = ", l4) 
print("Look at copy of l3 after clearing l3 => l5 = ", l5) 

print("""
#####################################################
 In addition lists have an (in place) sort function
""")
l4.sort()
print("sort => l4 = ", l4)

l4.sort(reverse=True)
print("sort with reverse=True => l4 = ", l4)

print("""
#####################################################
 We can build a list from any sequence 
""")
t = 1, 5, 7, 8
l1 = list(t) # from a tuple 
l2 = list(l1) # from a list
print("tuple: t =", t)
print("l1 = list(t): l1 =", l1)
print("l2 = list(l1): l2 =", l2)


print("""
#####################################################
 Scoop: ranges are also immutable sequences
 ranges have some additional restrictions compared to tuples
 Some sequence functions do not work for ranges... you can try to find which ones
""")
r = range(5)
print("r =", r)
print("type(r) =", type(r))

# We can create a list from a range too
l3 = list(r) # from a range
print("l3 = list(r): l3 =", l3)

print("""
#####################################################
 for loops work for all sequences
""")
for e in l3:
    print("element from list l3:", e)
print()

for e in t:
    print("element from tuple t:", e)
print()

for e in r:
    print("element from range r:", e)
print()