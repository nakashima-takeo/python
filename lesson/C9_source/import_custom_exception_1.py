import my_exception

def main():
    try:
       raise my_exception.MyException()
    except my_exception.MyException as e:  
        print("Use Exception of type ", type(e))

if __name__ == "__main__":
    main()
