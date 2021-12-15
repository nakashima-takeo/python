class MyClass():
    """Another simple class example"""
    instances_count = 0

    def __init__(self, value):
        self.value = value
        MyClass.instances_count += 1

    # Define some functions
    def show_value(self):
        print("value = ", self.value) 

    def show_count(self):
        print("count = ", MyClass.instances_count) 

# Create an instance 
a = MyClass(5)
a.show_value()
a.show_count()
# Create another instance
b = MyClass('test')
b.show_value()
b.show_count()
# Create an instance variable
print("a.instances_count = ", a.instances_count)
a.instances_count = 0
print("a.instances_count = ", a.instances_count)
a.show_count()

# Note:
# The instance variable is accessed first
# Then in the show_count function definition:
# self.instances_count 
# rather than 
# MyClass.instances_count
# would work as long as 
# the instance variable instances_count
# is not defined
#
# In general there is a danger that adding an instance variable
# hides a class variable
# It is better to avoid adding instance variable
# use 
# <instance>.<data attribute> = value
# to modify an existing instance variable
# avoid using it to create a new instance variable
#
# If you need a new variable, explicitely define it in the __init__ 
