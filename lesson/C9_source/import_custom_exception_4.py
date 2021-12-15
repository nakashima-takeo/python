from my_exception import MyException as TestExeception

def main():
    try:
       raise TestExeception()
    except TestExeception as e:  
        print("Use Exception of type ", type(e))

if __name__ == "__main__":
    main()
