print("""
#####################################################
# Set creation
#####################################################
""")

# Use curly braces and comma
s1 = {1, 4, 6}
print('s1 =', s1)

# Use constructor
# from a list
# Notice that there is no duplicate in the set
s2 = set([1,3,5,5,6,7])
print('s2 =', s2)

# from a string
# Notice that there is no duplicate in the set
s3 = set('kyoto university')
print('s3 =', s3)
print('"kyoto university" contains {} different characters'.format(len(s3)))

# Use set comprehension
s4 = {x for x in range(5)}
print('s4 =', s4)

# empty set
# Warning: {} is not an empty set!
# more on that later
s_empty = set()

# Elements can have mixed types
s_mix = {1, 'a', 'test', 0.1, (0,5)}
print('s_mix =', s_mix)

# Can a list be an element?
# Can a tuple containing a list be an element?

print("""
#####################################################
# Set operations
#####################################################
""")
print('s1 =', s1)
print('s2 =', s2)

# what are the following operations doing ?
# functional notations using . are also given
print('s1 | s2 =', s1 | s2)  # s1.union(s2)
print('s1 & s2 =', s1 & s2)  # s1.intersection(s2)
print('s1 - s2 =', s1 - s2)  # s1.difference(s2)
print('s2 - s1 =', s2 - s1)  # s2.difference(s1)
print('s1 ^ s2 =', s1 ^ s2)  # s1.symmetric_difference(s2)

# inclusion
print('is 1 in s1:', 1 in s1)

# size of a set
print('s1 contains {} elements'.format(len(s1)))

# max and min
print('Largest element in s1:',max(s1))
print('Smallest element in s1:',min(s1))

# superset
# a set containing the element of another set
print('is s1 a superset of {1,4}', s1.issuperset({1,4}))

# subset
# a set contained in another set
print('is s1 a subset of s2', s1.issubset(s2))

s5 = {1,7}
print('s5 =', s5)
print('is s5 a subset of s2', s5.issubset(s2))

# There are more functions...
# You can find their name using dir()
# the members __<name>__ are private (ex: __rsub__)
# they are not intended to be used
# the functions are among the other members
# ex: isdisjoint

# Can you access the element of a set using indexing?

print("""
#####################################################
# Iterate on the elements of a set
#####################################################
""")
s6 = set([1,15,6,7,31,22])
print('s6 =', s6)
# We can iterate on a set using for
for e in s6:
    print(e)

# It is possible to iterate on sorted values
for e in sorted(s6):
    print(e)


# Note that sorted() does not modify the set
# it creates a list that is used for iteration 
print(type(sorted(s6)))


print("""
#####################################################
# Set quiz
#####################################################

# Using sets, find the letters 
# in common
# not in common 
# for the two follwoing words:
#  university
#  universality
""")




