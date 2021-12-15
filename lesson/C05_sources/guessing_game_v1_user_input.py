# Guessing game
# guess a value between 1 and 9 (included)

value = int(input("Please enter a value between 1 and 9 (included):"))

guess = 1

number_trials = 1
while guess != value:
    guess = guess + 1
    number_trials = number_trials + 1

print("The value is: ", guess)
print("Number trials: ", number_trials)
