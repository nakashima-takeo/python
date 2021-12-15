# Pack elements in a tuple
# This is a convenient way to keep together 
# the information about John
data = ("John", 32, "Kyoto", 1234)

# Rather than accessing the element one by one by using an index
name = data[0]
age = data[1]
city = data[2]
user_id = data[3]

# You can unpack elements from a tuple:
(name, age, city, user_id) = data

########################
# Bonus string formating
# Preview of later topics...

# Formated output using format (python > 2.6)
# {} are placeholders 
print("{} ({}) living in {} has id {}".format(name, age, city, user_id))