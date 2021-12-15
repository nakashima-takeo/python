from my_exception import MyException

def main():
    try:
       raise MyException()
    except MyException as e:  
        print("Use Exception of type ", type(e))

if __name__ == "__main__":
    main()
