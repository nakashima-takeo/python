
from tkinter import StringVar, Tk, Frame, Label, IntVar
import re


def create_list_of_words(file_name):
    words_list = []
    with open(file_name, 'r', encoding='utf-8') as fd:
        for line in fd:
            words = line.lower().split(" ")
            words = [re.sub(r"[^a-z0-9]","",word) for word in words]
            words = [word for word in words if word != '']
            words_list.extend(words)
    return words_list

word_list = create_list_of_words("book_chapter.txt")
#print(len(word_list))

def create_word_dict(words_list):
    words_dict = {}
    for word in words_list:
        word_count = words_list.count(word)
        words_dict[word] = word_count
    return words_dict

word_dict = create_word_dict(word_list)

def filter_dict(words_dict, threshold):
    filtered_words_dict = {}
    for word, count in words_dict.items():
        if count >= threshold:
            filtered_words_dict[word] = count
    return filtered_words_dict

filtered_words_dict = filter_dict(word_dict, 20)
#[print(word, count) for word, count in filtered_words_dict.items()]

# subclass of Frame
class GUI(Frame):
    def __init__(self,dict):
        Frame.__init__(self)
        self.word_dict = dict
        # list of keys
        self.list_of_keys = list(self.word_dict.keys())
        # selected word number
        self.select_word_number = 0
        self.label = None
        self.word = StringVar()
        self.count = IntVar()
        self.label = Label(self, textvariable = self.word)
        self.label.pack(side = "left")
        self.label = Label(self, text = ":")
        self.label.pack(side = "left")
        self.label = Label(self, textvariable = self.count)
        self.label.pack(side = "left")
        self.pack()
        self.set_word(self.list_of_keys[self.select_word_number])
        self.bind_all("<KeyPress>", self.select_word)

    def set_word(self,word = "the"):
        self.word.set(word)
        self.count.set(self.word_dict[word])

    def select_word(self,event):
        # when you press left arrow key
        if event.keysym == "Left":
            if self.select_word_number > 0:
                self.select_word_number -= 1
                self.set_word(self.list_of_keys[self.select_word_number])
        # when you press right arrow key
        elif event.keysym == "Right":
            if self.select_word_number < len(self.list_of_keys) - 1:
                self.select_word_number += 1
                self.set_word(self.list_of_keys[self.select_word_number])

root = Tk()

gui = GUI(word_dict)
root.mainloop()