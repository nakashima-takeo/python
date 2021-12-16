def method_0():
    empty_tuple = ()
    empty_list = []
    for list_attribute in dir(empty_list):
        if list_attribute.startswith('__'):
            continue
        if not(hasattr(empty_tuple, list_attribute)):
            print("tuples do not have " + list_attribute)
        else:
            print("tuples have " + list_attribute)

def method_1():
    empty_tuple = ()
    empty_list = []
    flag = False
    for list_attribute in dir(empty_list):
        if list_attribute.startswith('__'):
            continue
        for tuple_attribute in dir(empty_tuple):
            if list_attribute == tuple_attribute:
                print("tuples have " + list_attribute)
                flag = True
                break
        if not flag:
            print("tuples do not have " + list_attribute)
        flag = False

method_flag = 1

if method_flag == 0:
    method_0()
else :
    method_1()




