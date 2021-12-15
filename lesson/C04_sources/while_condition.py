print('Use an integer as condition:')

a = 10
while a:
    print(a)
    a = a - 1

print()
print('Use a string as condition:')

sentence = 'This is used as condition'
while sentence:
    print(sentence[-1])
    sentence = sentence[:-1]

print()
print('Use a list as condition:')

condition_list = [1, 0.3, 'test', 5, 10.2, 'end']
while condition_list:
    print(condition_list[0])
    condition_list = condition_list[1:]