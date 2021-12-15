class MyException(Exception):
    """Version with an optional message"""
    pass

if __name__ == "__main__":
    print("my_exception module is the main unit")
    try:
        raise MyException()
    except MyException as e:
        print("This is a test for:", type(e))
else:
    print("my_exception module Imported as", __name__)