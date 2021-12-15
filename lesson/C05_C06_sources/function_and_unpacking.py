# The function we want to use 
def display_user_info(name, age, city, user_id):
    print("{} ({}) living in {} has id {}".format(name, age, city, user_id))

# Our data packed in a tuple
data = ("John", 32, "Kyoto", 1234)

# To use the function on the tuple data:

# 1 - get the values from the tuple
display_user_info(data[0], data[1], data[2], data[3])

# or

# 2 - unpack the tuple using the operator *
display_user_info(*data)

# Python understands it has to set one value of the tuple to each argument of the function
# The tuple size should match the number of arguments

# It is also possible to define a function that accepts a tuple as a single argument
def display_user_info_tuple(data_tuple):
    print("{} ({}) living in {} has id {} (using tuple)".format(data_tuple[0], data_tuple[1], data_tuple[2], data_tuple[3]))

display_user_info_tuple(data) # Note that there is no * operator this time


# Side note
# The following statement will make an error
# display_user_info_tuple("John", 32, "Kyoto", 1234)
# Python thinks that "John", 32, "Kyoto", 1234 are four function arguments
# The tuple syntax with parenthesis is necessary for that case
display_user_info_tuple(("John", 32, "Kyoto", 1234)) # This works


