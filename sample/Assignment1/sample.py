l = list(range(5))
l_ref=l
l_copy=l.copy()

print(type(l))
print(dir(l)) 
print(id(l))
print(id(l_ref)) # reference to same object = same id
print(id(l_copy)) # reference to a different object = different id
t = 3, 2, 7
print(hasattr(t, 'sort')) # a tuple does not have a function sort
