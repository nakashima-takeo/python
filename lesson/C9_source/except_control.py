class TestException(Exception):
    pass
def main():
    print("Block 1:")
    try:
        print("Raise an exception") 
        raise TestException
    except TestException: 
        print("Test exception happened")
    else:
        print("No exception")
    finally:
        print("Done in any case")       

    print("Block 2:")
    try:
        print("Do not raise an exception") 
        pass
    except TestException: 
        print("Test exception happened")
    else:
        print("No exception")   
    finally:
        print("Done in any case")

if __name__ == "__main__":
    main()
