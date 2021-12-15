from copy import deepcopy 
# The previous statement tells that
# we want to use the function deepcopy 
# from the package copy
# a package is a "container for code"
# We will see that later in details

# 1) Create two lists
l1 = [1.0, 3.0]
l2 = [-5.0, 4.0, 7.0]

# 2) Create a list of lists
l3 = [l1, l2]

print("The lists:")
print("l1 =", l1)
print("l2 =", l2)
print()

print("The list of lists: l3 =", l3)
print()

# "Create" 3 lists using different methods
l4 = l3.copy()
l5 = l3
l6 = deepcopy(l3)

# Display
print("The 3 copies:")
print("l4 = l3.copy() => l4 = ", l4) 
print("l5 = l3 => l5 = ", l5) 
print("l6 = deepcopy(l3) => l6 = ", l6) 
print()

# Modify an element in l1
l1[1] = 0.0
print("Modified l1 =", l1)
print()

print("Effect of modification on other lists:")
print("l2 = ", l2)
print("l3 = ", l3)
print("l4 = ", l4) 
print("l5 = ", l5)
print("l6 = ", l6) 
print()

# Modify an element of an element of l3
l3[1][0] = -10.0
print("Modify an element of an element of l3")
print("l3[1][0] = -10.0 =>  l3 =", l3)
print()

print("Effect of modification on other lists:")
print("l1 = ", l1)
print("l2 = ", l2)
print("l4 = ", l4) 
print("l5 = ", l5)
print("l6 = ", l6) 
print()

# Clear l3
l3.clear()
print("Effect of clearing l3 on other lists:")
print("l1 = ", l1)
print("l2 = ", l2)
print("l3 = ", l3)
print("l4 = ", l4) 
print("l5 = ", l5)
print("l6 = ", l6) 
