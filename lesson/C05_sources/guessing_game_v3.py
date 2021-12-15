# Guessing game 
# guess a value between 1 and 9 (included)

value = 7


interval_top = 10
interval_bottom = 0
guess = (interval_top + interval_bottom) // 2

number_trials = 1
while not guess == value:
    if guess > value:
        interval_top = guess
    else:
        interval_bottom = guess    
    guess = (interval_top + interval_bottom) // 2
    number_trials = number_trials + 1

print("The value is: ", guess)
print("Number trials: ", number_trials)
