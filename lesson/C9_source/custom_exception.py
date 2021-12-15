class MyException(Exception):
    """Version with an optional message"""
    pass

class MyExceptionMsg(Exception):
    """Version that requires a message"""
    def __init__(self, message):
        self.message = message


def main():
    try:
       raise MyException()
       #raise MyException("Test message") 
       #raise MyExceptionMsg()
       #raise MyExceptionMsg("Test message")
    except Exception as e:  
        print("Exception of type ", type(e), " value:", e)

if __name__ == "__main__":
    main()
