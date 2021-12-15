def display_info_1(input_list):
    modified_list = input_list
    modified_list[1] = modified_list[1] * (1.0 + modified_list[2])
    print("A {} costs {} with {} tax".format(*modified_list))# unpacking using *

def display_info_2(input_list):
    modified_list = input_list.copy() 
    modified_list[1] = modified_list[1] * (1.0 + modified_list[2])
    print("A {} costs {} with {} tax".format(*modified_list))# unpacking using *

print("Use function 1")
# item, price without tax, tax ratio
l = ["pen", 5.0, 0.05]
print(l)

display_info_1(l)
print(l)

print()

print("Use function 2")
l = ["pen", 5.0, 0.05]
print(l)

display_info_2(l)
print(l)
