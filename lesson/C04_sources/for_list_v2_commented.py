# Define a list of fruits
fruits_list = ['apple', 'lemon', 'banana', 'peach', 'grape']

"""
Check if the list of fruits contains 'banana'
Stop iterating through the list if 'banana' is found
"""
for fruit in fruits_list:
    print(fruit)
    if fruit == 'banana': 
        print("banana is in the list") # report the finding
        break 