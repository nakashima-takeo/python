    def select_word(self,event):
        # when you press left arrow key
        if event.keysym == "Left":
            self.select_word_number -= 1
            self.display_word(self.list_of_keys[self.select_word_number])
        # when you press right arrow key
        elif event.keysym == "Right":
            self.select_word_number += 1
            self.display_word(self.list_of_keys[self.select_word_number])
