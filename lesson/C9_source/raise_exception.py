# Two functions that raise a specific exception
def raise_IOError():
    raise IOError

def raise_IOErrorMsg():
    raise IOError("Error with message")

# The main function containinng the try/except block
def main():
    try:
        # Try both functions to see the difference
        raise_IOError() 
        #raise_IOErrorMsg() 
    except Exception as e:  # Note this constuction using "as"
        # In this block of code the variable e contains the exception
        print("Exception of type ", type(e), " value:", e)
if __name__ == "__main__":
    main()
