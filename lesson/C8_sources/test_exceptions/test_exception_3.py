def main():
    value = int(input("Enter value: "))
    print("10 / value = ", 10 / value)

if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Must type an int")
    except ZeroDivisionError:
        print("Must not be zero")
    except:
        print("Unexpected error")
