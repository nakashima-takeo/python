#  two methods for checking
#  use code introspection functions dir and hasattr.
def method_0():
    empty_tuple = ()
    empty_list = []
    for list_attribute in dir(empty_list):
        if list_attribute.startswith('__'):
            continue
        if not(hasattr(empty_tuple, list_attribute)):
            print("tuples do not have " + list_attribute)

# use code introspection function dir and sets.
def method_1():
    empty_tuple = ()
    empty_list = []
    list_set = set(dir(empty_list))
    tuple_set = set(dir(empty_tuple))
    set1 = (list_set - tuple_set)
    for attribute in set1:
        if attribute.startswith('__'):
            continue
        print("tuples do not have " + attribute)

# swiching between methods
method_flag = 0

if method_flag == 0:
    method_0()
else:
    method_1()
