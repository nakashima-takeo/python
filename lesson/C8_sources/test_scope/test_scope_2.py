
def outer_function1():
    # local variables
    a = 1 
    print("outer_function : a=", a)
    def inner_function():
        a = 8
        print("inner_function : a=", a)
    inner_function()
    print("outer_function : a=", a)

def outer_function2():
    # local variables
    a = 1 
    print("outer_function : a=", a)
    def inner_function():
        nonlocal a
        a = 8
        print("inner_function : a=", a)
    inner_function()
    print("outer_function : a=", a)

# Define global variables a
a = 5
print("a=", a)

# Use the function
outer_function1()

# show again a
print("a=", a)

# Use the function
outer_function2()

# show again a
print("a=", a)