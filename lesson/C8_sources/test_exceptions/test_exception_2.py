def main(value):
    try:
        print("10 / value = ", 10 / value)
    except ZeroDivisionError:
        print("Detected a division by 0")

if __name__ == "__main__":
    while True:
        try:
            value = int(input("Enter value: "))
            break
        except ValueError:
            print("This is not an int, try again")
    main(value)