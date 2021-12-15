
# Create a list with multiple elements
l = [0.3, 1.2, 6.1]
print("l = ",l)
print("l is a", type(l))
print()

# create a list with a single element
l = [0.3]
print("l = ",l)
print("l is a", type(l))
print()

# create an empty list 
l = []
print("l = ",l)
print("l is a", type(l))
print()

# Create a list with different type of elements
l = [1.0, "test", [1.0, -5.0], 12, (4,2), "previous element is a tuple", 3.0]
print("l = ",l)
print("l is a", type(l))
print("l has", len(l), "elements") 
print()

# Some list indexing
print("l[0]=", l[0]) # access first element
print("l[1:3]=", l[1:3]) # slice of elements from 1st (included) to 3rd (excluded)
print("l[:4]=", l[:4]) # elements up to 4th (excluded)
print("l[2:]=", l[2:]) # from 2nd to end
print("l[-1]=", l[-1]) # last from end
print("l[-2:]=", l[-2:]) # from second last from end to end
print("l[:-2]=", l[:-2]) # from start to second last from end (not included) 
print()

print("l[2][0]=", l[2][0]) # access the element 2 that is a list then the element 0 of that list
print("l[4][1]=", l[4][1]) # access the element 4 that is a tuple then the element 1 of that tuple
print("l[1][-1]=", l[1][-1]) # access the element 1 that is a string then the last character of that string
print()