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

data = datafile.readlines()
three_floats = [line.split(' ') for line in data]
for line in three_floats:
    x = float(line[0])
    y = float(line[1])
    r = float(line[2].rstrip('\n'))
    e = (math.cos(x) + y - r) ** 2
    if e > 0.001:
        errors += 1
        r = math.cos(x) + y
        line[2] = str(r) + '\n'
    line[0] = line[0] + ' '
    line[1] = line[1] + ' '
    new_datafile.writelines(line)
print(errors)