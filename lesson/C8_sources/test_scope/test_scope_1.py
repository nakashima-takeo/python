
def test_function1():
    # local variables
    a = 1
    print("test_function1 : a=", a)

def test_function2():
    global a
    a = 1
    print("test_function2 : a=", a)

# Define global variable a
a = 5
print("a=", a)

# Use the function1
test_function1()

# show again a
print("a=", a)

# Use the function2
test_function2()

# show again a
print("a=", a)