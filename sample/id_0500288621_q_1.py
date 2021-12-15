days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
start = 20
sharp_symbol = "#"
weeklength = 0
# まず、daysから最長の物を選択して、それに2を追加したものを文字列長とする。
for day in days:
    if weeklength < len(day) + 2:
        weeklength = len(day) + 2

# 

print(sharp_symbol * (7 + weeklength))

for day in days:
    weekprint = sharp_symbol + " " + day + " " * (weeklength - len(day) - 1) + sharp_symbol
    dayprint = " " * int(2 / len(str(start))) + str(start) + " " + sharp_symbol
    print(weekprint + dayprint)
    start = (start + 1) % 32
    if start == 0:
        start += 1
print(sharp_symbol * (7 + weeklength))