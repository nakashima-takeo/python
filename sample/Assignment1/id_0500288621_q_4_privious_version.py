from os import read
import math

# file pass
document_file = 'C:\github\python\sample\data_q4.txt'
new_document_file = 'C:\github\python\sample\corrected_data_q4.txt'

# the number of errors
errors = 0
# file open/make
datafile = open(document_file, 'r', encoding='utf-8')
new_datafile = open(new_document_file, 'w', encoding='utf-8')

data = datafile.read()
datalist = data.split('\n')
datafile.close()
for line in datalist:
    if line == '':
        break
    number_set = line.split(' ')
    x = float(number_set[0])
    y = float(number_set[1])
    r = float(number_set[2])
    e = (math.cos(x) + y - r) ** 2
    if e > 0.001:
        errors += 1
        r = math.cos(x) + y
        number_set[2] = str(r)
    number_set[2] = number_set[2] + '\n'
    new_datafile.writelines(number_set)
print(errors)

