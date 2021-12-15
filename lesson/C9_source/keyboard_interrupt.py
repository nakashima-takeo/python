import time # To use the sleep function

def main():
    print("Start endless loop. Use Ctrl-c to break")
    try:
        while True:
            time.sleep(1) # sleeps for 1 s
    except KeyboardInterrupt:  
        print("User pressed Ctrl-c")

if __name__ == "__main__":
    main()
