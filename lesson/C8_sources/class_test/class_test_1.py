##############################################
# Class definition

class MyClass():
    """A simple class example"""
    # define a class variable
    value = 5            

    # Define a function
    def hello(self):
        print("Hello!") 

##############################################
# Use the class

# Access class variable
print("MyClass.value = ", MyClass.value)

# Create an instance of MyClass
a = MyClass()

# Access the class variable
# from the instance
print("a.value = ", a.value)

# Use the functions
MyClass.hello(a)
a.hello()

##############################################
# Introspection:

# MyClass is a class object
print("type(MyClass) = ", type(MyClass))

# The attribute of the class object
print("dir(MyClass) = ", dir(MyClass))

# The instance is an object 
print("type(a) = ", type(a))

# The attribute of the instance
#
print("dir(a) = ", dir(a))

# Class function & method are of different type
print("type(MyClass.hello) =", type(MyClass.hello))
print("type(a.hello) =", type(a.hello))

# It is possible to call a method later
later_call = a.hello
later_call()

