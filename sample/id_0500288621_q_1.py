days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
start = 18
sharp_symbol = "#"
weeklength = 0
# First, select the longest one from days and add 2 to it as the string length.
for day in days:
    if weeklength < len(day) + 2:
        weeklength = len(day) + 2
# sharp_symbol
print(sharp_symbol * (7 + weeklength))

# Print the days of the week and numbers.
for day in days:
    weekprint = sharp_symbol + " " + day + " " * (weeklength - len(day) - 1) + sharp_symbol
    # "There is a space on each side of the numbers" is written, but it is not beautiful.
    # so I will change it.
    dayprint = " " * int(2 / len(str(start))) + str(start) + " " + sharp_symbol
    print(weekprint + dayprint)
    start = (start + 1) % 32
    if start == 0:
        start += 1

# sharp_symbol
print(sharp_symbol * (7 + weeklength))