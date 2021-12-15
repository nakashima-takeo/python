# Guessing game 
# guess a value between 1 and 9 (included)

value = 7


guess = 5
number_trials = 1

while not guess == value:
    if guess > value:
        guess = guess - 1
    else:
        guess = guess + 1
    
    number_trials = number_trials + 1

print("The value is: ", guess)
print("Number trials: ", number_trials)
