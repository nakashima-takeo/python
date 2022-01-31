from text_analysis_lib import analyze_text

from tkinter import Tk, Label, Entry, Button

class TextAnalysisGUI():
    def __init__(self, master):
        self.master = master
        master.title("Text Analysis GUI")

        # For text selection
        label_text = Label(master, text="File name:")
        self.entry_text = Entry(master)

        # For count selection
        label_count = Label(master, text="Threshold:")
        self.entry_count = Entry(master)

        # Define a button to start the computation
        button_go = Button(master, text="go", command=self.analyze)

        # To display results
        self.label_result = Label(master, text="")

        # Place the element in the window
        label_text.pack()
        self.entry_text.pack()
        label_count.pack()
        self.entry_count.pack()
        button_go.pack()
        self.label_result.pack()

    # Function that computes and displays the results
    def analyze(self):
        # Use library to compute 
        try:
            result_dict = analyze_text(self.entry_text.get(), int(self.entry_count.get()))
        except ValueError:
            display_text =  "The threshold must be a positive integer"            
        except FileNotFoundError:
            display_text =  "You must provide a valid filename"            
        except:
            display_text = "Unexpected error"            
        else:    
            # Create the display string
            display_text = "Results:\n"
            for word, count in result_dict.items():
                display_text += "{0: <10} {1: >4}\n".format(word, count) 

        # Set the display string for display
        self.label_result["text"] = display_text

if __name__=='__main__':

    # Create the window
    root = Tk()

    # Create our object
    text_analysis_gui = TextAnalysisGUI(root)

    # Start the event loop
    root.mainloop()
