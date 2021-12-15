# Optional information about module:
import importlib 
# A module is imported only one time 
# This is also true for the interactive shell
# When testing some modifications on a module in an interactive shell
# the importlib reload function is useful to reload the module after modification
# Without using it, the module is not reloaded
# and the modifications are not taken into account
# in the interactive shell

import my_exception

def main():
    importlib.reload(my_exception) # Force reload the module
    # This is just an example, it does not make much sense in a script like this.
    try:
       raise my_exception.MyException()
    except my_exception.MyException as e:  
        print("Use Exception of type ", type(e))

if __name__ == "__main__":
    import sys, math
    print(dir(sys))
    print(dir(math))
    print(dir(my_exception))

    main()
