
import sys # to get the command line arguments

def main(file_name, threshold):
    pass # remove this statement and write your code 

    #############################################
    # Task 1:
    # Open the file to read the text line by line
    # Create a list of words when reading the file
    ##############################################

    # Step by step

    # create an empty list of words

    # read the text line by line

    # Use string operations to convert the line to words
    # hints: 
    # use split to cut into words
    # use lower to remove upper case
    # use rstrip to remove the '\n'
    # you can chain the string operations
    # optional: deal with the punctuation 

    # Use extend() to add the words to the list of words

    # report the total number of words

    #############################################
    # Task 2:
    # Create a list of unique words
    # (remove duplicates)
    ##############################################

    # hint: use set

    # optional: remove the empty word from the list

    # report the number of different words

    #############################################
    # Task 3:
    # Count the number of time the words appear
    ##############################################

    # hint use a dictionary to store the count of the words

    # Create an empty dictionary

    # iterate on the unique words

    # Use the count() function on the total list of words
    # to get the count of each word

    # Only add to the dictionary if the count is larger than the threshold

    # Display these words and their count

    #############################################
    # Task 4:
    # Write the results to file
    ##############################################
    
    # use a file names count.txt

    # iterate on the dictionary to write the file line by line

if __name__ == "__main__":

    # Hard coded values
    file_name = 'book_chapter.txt'
    threshold = 10
    main(file_name, threshold)

    # Todo:
    # Replace the hard coded values by command line arguments 
    
    # Optional: use a if else structure to accept argument entered using input()
    # when there is no command line arguments
