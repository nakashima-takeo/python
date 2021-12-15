def main():
    value = int(input("Enter value: "))
    print("10 / value = ", 10 / value)

if __name__ == "__main__":
    try:
        main()
    except (ValueError, ZeroDivisionError):
        print("Wrong input")