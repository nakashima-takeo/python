print("Using while:")
cpt=0
while cpt < 10:
    print("counter = ", cpt)
    cpt = cpt + 1

print("Using for:")
for cpt in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("counter = ", cpt)

print("Using for & range:")
for cpt in range(10):
    print("counter = ", cpt)