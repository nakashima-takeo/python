
#################################################################
# Iterate on one list showing value and index

# Example list
x_list = [1, 2, 3, 4, 5]
print('x_list =', x_list)

# Iterate through the list
# show the index of the element and the element
i = 0 # create a counter
for x in x_list:
    print(i, x)
    i += 1 # update the counter equivalent to i = i + 1

print()

# Use a range to create a list of indixes
# get the adequate range using len()
for i in range(len(x_list)): 
    print(i, x_list[i]) # access the elements

print()

# Use the enumerate function
# it give the index and the value
for i, x in enumerate(x_list):
    print(i, x)

print()

#################################################################
# Iterate on two lists

# example lists
items = ['pen', 'notebook', 'eraser']
prices = [5.0, 3.5, 1.5]
print('items =', items)
print('prices = ', prices)

print()

# iterate using a range on one list
for i in range(len(items)):
    print('{} costs {}'.format(items[i], prices[i])) # same index for both lists

print()

# Use the zip function to combine the lists
# get an element per list
for item, price in zip(items, prices):
        print('{} costs {}'.format(item, price))

print()

# Note that it looks a bit similar to an iteration on dict items()
#d1 = {'name' : 'John', 'age' : 32, 'city' : 'Kyoto', 'user_id' : 125}
#for k,v in d1.items():
#    print('{} <=> {}'.format(k, v))

print()

# Nested lists gives a different result
for item in items:
    for item in prices:
        print('{} costs {}'.format(item, price))

print()

# it shows all the pairs

# Using ranges and indices to iterate on the lists,
# we can add a test to show elements at the "same levels" in the list
# This has the same output as zip
# rather use zip
for i in range(len(items)):
    for j in range(len(prices)):
        if i == j:
            print('{} costs {}'.format(items[i], prices[j]))

print()

# Does zip works with more lists?

#################################################################
# Convert between sets, lists and tuples
l1 = [1, 2, 2, 7]
t1 = tuple(l1)
s1 = set(t1) 
t2 = tuple(s1)
l2 = list(t2)

# Note that list(), set() and tuple()
# are usefull for explicitely creating the objects

print('l1 =', l1)
print('t1 =', t1)
print('s1 =', s1)
print('t2 =', t2)
print('l2 =', l2)

# Why l2 is not the same as l1?

print()

#################################################################
# Combine two lists to keep only the elements appearing in both
l1 = [1, 21, 7, 11, 13, 5]
l2 = [7, 15, 31, 11, 12, 2]
print('l1 =', l1)
print('l2 =', l2)

l3 = []
for e1 in l1:
    for e2 in l2:
        if e1 == e2:
            l3.append(e1)
print('l3 =', l3)

# Use sets and conversions
l4 = list(set(l1).intersection(set(l2)))
print('l4 =', l4)
# create a set from each list: set(l1) and set(l2)
# get the sets intersection: set(l1).intersection(set(l2))
# create a list from the set intersection 

print()

#################################################################
# Filter a dictionary or a list
# keep only some values according to a condition

d1 = {'name' : 'John', 'age' : 32, 'city' : 'Kyoto', 'user_id' : 125}
print('d1 =', d1)

# create a dictionary with name and user_id
d2 = {}
for k,v in d1.items():
    if k == 'name' or k == 'user_id':
        d2[k] = v
print('d2 =', d2)

# The following code give a RuntimeError
# 
#for k,v in d1.items():
#    if k == 'name' or k == 'user_id':
#        del d1[k]

# For lists
# keep elements > 10
l1 = [1, 21, 7, 11, 13, 5]
print('l1 =', l1)
l2 = []
for e in l1:
    if e > 10:
        l2.append(e)
print('l2 =', l2)

# give an IndexError
#for i in range(len(l1)):
#    if l1[i] <= 10:
#        del l1[i]
#print('l1 =', l1)

# But 
for e in l1:
    if e <= 10:
        l1.remove(e)
print('l1 =', l1)
# works

# In any case, it is safer/cleaner 
# to create a new dict or list
# when filtering