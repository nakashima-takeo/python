# Script showing several list comprehension examples

l1 = list(range(5))
print(l1)

l2 = []
for x in l1:
    l2.append(x**2)
print(l2)

l3 = [x**2 for x in l1]
print(l3)

# use tuple to have multiple outputs
l4 = [(x, x**2) for x in l1]
print(l4)

# use several for
l5 = [x*y for x in l1 for y in l1]
print(l5)

# use several for and if
l6 = [x*y for x in l1 for y in l1 if x > y]
print(l6)

l7 = [x*y for x in l1 if x > 2 for y in l1 if y < 3]
print(l7)

# The following 3 examples are explained in the lecture

l8 = [(x, y, x*y) for x in l1 for y in l1 if x > 2 if y < 3]
print(l8)


# Put a list of list l3 into a list l9
l1 = [1.0, 3.0]
l2 = [-5.0, 4.0, 7.0]
l3 = [l1, l2]
print(l3)

l9 = [e for l in l3 for e in l]
print(l9)

# Nested list comprehension
l10 = [[(i, j, i+j) for j in range(2)] for i in range(3)]
print(l10)

