def filter_dict(words_dict, threshold):
    filtered_dic = {}
    for word, count in words_dict.items():
        if count >= threshold:
            filtered_dic[word] = count
    return filtered_dic

def create_word_dict(words_list):
    words_dict = {}
    for word in words_list:
        word_count = words_list.count(word)
        words_dict[word] = word_count
    return words_dict

def create_list_of_words(file_name):
    words_list = []
    with open(file_name, 'r', encoding='utf-8') as fd:
        for line in fd:
            words = line.rstrip('\n').lower().split(" ")
            words_list.extend(words)
    # remove the empty word from the list
    words_list.remove('')
    return words_list

word_list = create_list_of_words("book_chapter.txt")
print(len(word_list))
word_dict = create_word_dict(word_list)
filtered_dict = filter_dict(word_dict, 20)
[print(word, count) for word, count in filtered_dict.items()]

#[print(word) for word in word_list]