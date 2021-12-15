from text_analysis_lib import analyze_text

from tkinter import Tk, Label, Entry, Button

if __name__=='__main__':

    # Create the elements
    root = Tk()
    root.title("Text Analysis GUI")

    # For text selection
    label_text = Label(root, text="File name:")
    entry_text = Entry(root)

    # For count selection
    label_count = Label(root, text="Threshold:")
    entry_count = Entry(root)
    
    # To display results
    label_result = Label(root, text="")

    # Function that computes and displays the results
    def analyze():
        # Use library to compute 
        try:
            result_dict = analyze_text(entry_text.get(), int(entry_count.get()))
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
        label_result["text"] = display_text

    # Define a button to start the computation
    button_go = Button(root, text="go", command=analyze)
    
    # Place the element in the window
    label_text.pack()
    entry_text.pack()

    label_count.pack()
    entry_count.pack()

    button_go.pack()

    label_result.pack()

    # Start the event loop
    root.mainloop()
