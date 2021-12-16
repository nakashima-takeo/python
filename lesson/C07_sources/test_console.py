import sys # Tell Python we want to use functions from the sys package

# The script get a list from the system
# This is the list of "command line arguments"
# The argument given to the script when running it
print('List of command line arguments:', sys.argv)

# The first element is the name of the script
script_name = sys.argv[0]
print('script name:', script_name)

# Then there are optional elements
# Try running the script by typing
# as usual (no arguments)
#   python test_console.py
# Then by typing (3 arguments)
#   python test_console.py 1.0 test 3 

# Deal with additional arguments if any
if len(sys.argv)>2:  # check if any
    # iterate through the list
    for i, a  in enumerate(sys.argv[1:]):
        print('arg[{}] = {} (type: {})'.format(i, a, type(a)))

    # Note that the arguments are in order and all of them are strings
    
    # Let say that the first argument should be a float
    # We can convert a string to a float
    f = float(sys.argv[1])

    # But what happen if the script is run with
    #   python test_console.py test 3 1.0
    # We get a ValueError!
    # because 'test' cannot be converted to a float

    # what can we do?
    
    # Tell the user to always write a first argument that can be converted to float?
    
    # but what if the user make a mistake?
    
    # We have to check that the value is valid 

    # It is important to check the user input

    # More on that later...
else:
    # There is no arguments
    # ask the user to input some value
    user_input = input('Enter a number:')
    # This function displays the string and wait for a user to input a value in the console
    # type 1.0 for a test

    print('The user inputed: {} (type {})'.format(user_input, type(user_input)) )
    # Note that this is a string
    
    # Again, we can convert that string to a float
    f = float(user_input)

    # And again if user_input cannot be converted to a string
    # the program ends with a ValueError

    # We must also check that input value

# Use the float
print("The square of {} is {}".format(f, f**2))

