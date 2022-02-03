import re

def create_list_of_words(file_name):
    words_list = []
    with open(file_name, 'r', encoding='utf-8') as fd:
        for line in fd:
            # replace upper case to lower case and split by space
            words = line.lower().split(" ")
            # remove symbols
            words = [re.sub(r"[^a-z0-9]","",word) for word in words]
            # delete the empty word from the list
            words = [word for word in words if word != '']
            words_list.extend(words)
    return words_list

word_list = create_list_of_words("book_chapter.txt")
print(len(word_list))