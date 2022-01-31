from random import randint


# given number
given_number = 7
# 
print("Number of faces: " + str(given_number))
try:
    # select number of trials
    success_trials = 0
    total_trials = 0
    while True:
        value = int(input("Please enter a value between 1 and " + str(given_number) + ":"))
        # if value is not in the interval [1, given_number], ask again
        if value < 1 or value > given_number:
            continue
        # dice roll
        total_trials += 1
        dice_rolls = randint(1, given_number)
        print("Number of rolls: " + str(dice_rolls))
        if value == dice_rolls:
            success_trials += 1
            print("Good guess!" + str(success_trials) + "/" + str(total_trials))
finally:
    print("thanks!")

