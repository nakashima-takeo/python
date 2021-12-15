###########################################################
# Read text from  a file

# File name
document_file = './book_chapter.txt' # this is in the source

# Create a file descriptor to access the file
fd = open(document_file, 'r', encoding='utf-8')
# 'r' for read mode
# encoding is not always necessary

# Use the file descriptor to read the text line by line
# for iterates on each lines until the end
# keep the lines in a list
lines_list = [] # empty list
for line in fd:
    lines_list.append(line) # add to list

# close the file descriptor when done
fd.close()

# Show the first 5 lines
for i in range(5):
    print('line {}: {}'.format(i, lines_list[i]))

###########################################################
# Write a file containing these lines and the line numbers

# file name
output_file = './five_lines.txt'

# create a file descriptor for writing
fd_out = open(output_file, 'w',  encoding='utf-8')
# 'w' for writing
# encoding not always necessary

# write the lines
for i in range(5):
    fd_out.write('line {}: {}'.format(i, lines_list[i]))

# close the file
fd_out.close()

###########################################################
# Check the writing by reading the created file

fd_check = open(output_file, 'r',  encoding='utf-8')

print('Read from file:')
for line in fd_check:
    print(line)

fd_check.close()

