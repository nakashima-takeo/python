fruits_list = ['apple', 'lemon', 'banana', 'peach', 'grape']

cpt = 0
while cpt < len(fruits_list):
    print(fruits_list[cpt])
    if fruits_list[cpt] == 'banana':
        print("banana is in the list")
        break
    cpt = cpt + 1
