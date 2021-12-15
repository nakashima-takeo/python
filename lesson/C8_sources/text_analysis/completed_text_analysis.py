
import sys # to get the command line arguments

def main(file_name, threshold):
    #commented out
    #pass # remove this statement and write your code 

    #############################################
    # Task 1:
    # Open the file to read the text line by line
    # Create a list of words when reading the file
    ##############################################

    # Step by step

    # create an empty list of words
    words_list = []

    # read the text line by line
    fd = open(file_name, 'r', encoding='utf-8')
    for line in fd:
        # Use string operations to convert the line to words
        # hints: 
        # use split to cut into words
        # use lower to remove upper case
        # use rstrip to remove the '\n'
        # you can chain the string operations
        words = line.rstrip('\n').lower().split(" ")

        # optional: deal with the punctuation 
        # use rstrip lstrip or strip to remove the punctuation
        # add the words one by one
        # you should remove the extend statement
        #for word in words:
        #    words_list.append(word.strip('.,?!:;"\n '))

        # Use extend() to add the words to the list of words
        words_list.extend(words)

    # close the file descriptor when done
    fd.close()

    # report the total number of words
    print("Total words:", len(words_list))

    #############################################
    # Task 2:
    # Create a list of unique words
    # (remove duplicates)
    ##############################################

    # hint: use set
    words_set = set(words_list)

    # optional: remove the empty word from the list
    words_set.remove('')

    # report the number of different words
    print("Different words:", len(words_set))

    #############################################
    # Task 3:
    # Count the number of time the words appear
    ##############################################

    # hint use a dictionary to store the count of the words

    # Create an empty dictionary
    words_dict = {}

    # iterate on the unique words
    for word in words_set:
        # Use the count() function on the total list of words
        # to get the count of each word
        word_count = words_list.count(word)

        # Only add to the dictionary if the count is larger than the threshold
        if word_count > threshold:
            words_dict[word] = word_count

    # Display these words and their count
    print("Frequent words:")
    for word, word_count in words_dict.items():
        print("Word '{}' appeared {} times".format(word, word_count))

    #############################################
    # Task 4:
    # Write the results to file
    ##############################################
    
    # use a file names count.txt
    output_file = './count.txt'
    fd_out = open(output_file, 'w',  encoding='utf-8')

    # iterate on the dictionary to write the file line by line
    fd_out.write('Word Count\n') # Header

    for word, word_count in words_dict.items():
        # One line per word
        fd_out.write('{} {}\n'.format(word, word_count))

    # close the file
    fd_out.close()

if __name__ == "__main__":

    # Hard coded values
    # Comment out the hard coded part
    #file_name = 'book_chapter.txt'
    #threshold = 10
    #main(file_name, threshold)

    # Todo:
    # Replace the hard coded values by command line arguments 
  
    # Optional: use a if else structure to accept argument entered using input()
    # when there is no command line arguments

    # Check command line arguments 
    if len(sys.argv) == 3:
        file_name = sys.argv[1]
        threshold = sys.argv[2]
    else:
        file_name = input('File name:')
        threshold = input('Threshold:')    

    # Convert the threshold to an int
    threshold = int(threshold)

    # We did not check the user's input
    # is threshold a string that can be converted to an int?
    # does the file pointed by file_name exits ?
    # What happen if the user enters "wrong" values ?

    # Call main function to do the job
    main(file_name, threshold)
