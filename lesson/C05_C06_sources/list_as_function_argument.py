def modify_last_elements_1(input_list):
    input_list[-1] = 0
    print("from function 1:", input_list)

def modify_last_elements_2(input_list):
    modified_list = input_list[:-1] 
    modified_list.append(0)
    input_list = modified_list
    print("from function 2:", input_list)

print("Use function 1")
l = [1, 5, 7]
print(l)

modify_last_elements_1(l)
print(l)

print()

print("Use function 2")
l = [1, 5, 7]
print(l)

modify_last_elements_2(l)
print(l)
