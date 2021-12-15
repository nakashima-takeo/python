import my_exception as me

def main():
    try:
       raise me.MyException()
    except me.MyException as e:  
        print("Use Exception of type ", type(e))

if __name__ == "__main__":
    main()
