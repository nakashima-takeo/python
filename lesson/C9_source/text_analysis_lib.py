def analyze_text(file_name, threshold):
    #############################################
    # Open the file to read the text line by line
    # Create a list of words when reading the file
    ##############################################
    
    words_list = []
    with open(file_name, 'r', encoding='utf-8') as fd:
        for line in fd:
            words = line.rstrip('\n').lower().split(" ")
            words_list.extend(words)

    #############################################
    # Create a list of unique words
    # (remove duplicates)
    ##############################################

    words_set = set(words_list)
    # remove the empty word from the list
    words_set.remove('')

    #############################################
    # Task 3:
    # Count the number of time the words appear
    ##############################################
    words_dict = {}

    # iterate on the unique words
    for word in words_set:
        # Use the count() function on the total list of words
        # to get the count of each word
        word_count = words_list.count(word)

        # Only add to the dictionary if the count is larger than the threshold
        if word_count > threshold:
            words_dict[word] = word_count

    # Return the dictionary containing the results
    return words_dict

if __name__ == "__main__":
    # Test
    res_dict = analyze_text("book_chapter.txt", 30)

    print("Number selected words:", len(res_dict))

    print("Selected words count:")
    for word, count in res_dict.items():
        print(word, count)
