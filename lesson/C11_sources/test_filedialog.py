from tkinter import Tk, Frame, Label, Button, filedialog

# json file
# To dump (write) a dictionary in json format in a string
# To load (read) a dictionary from a string in json format
import json

def load_json():
    global data_dict
    # Opens a dialog to select a file to open
    # filetypes controls the possible file types that can be accessed
    # returns the full path
    path = filedialog.askopenfilename(initialdir="/", title="Select json file",
        filetypes=(("json files", "*.json"),("all files", "*.*")))

    try:
        with open(path, "r") as fd:
            raw_data = fd.read() # read a json string

        # json string to dictionary
        data_dict = json.loads(raw_data)
    except FileNotFoundError:
        # If the user cancels the selection
        label["text"] = "Info: No file selected"
    except Exception:
        # If the user select a non valid json file or other error
        # For example: use all files and select an image
        label["text"] = "Info: Not a valid json file?"
    else:
        label["text"] = "Info: Loaded data from file"

def save_json():
    global data_dict
    if data_dict == None:
        label["text"] = "Info: No data to save yet"
        return
    else:
        # Opens a dialog to select a file to save to
        # ask confirmation if already exists
        # filetypes controls the possible file types that can be accessed
        # returns the full path
        path = filedialog.asksaveasfilename(initialdir="/",
        title="Save json file",
        filetypes=(("json files", "*.json"),))

        try:
            with open(path, "w") as fd:
                raw_data = json.dumps(data_dict)# dictionary to string
                fd.write(raw_data) # write string in file
        except FileNotFoundError:
            # If the user cancels the selection
            label["text"] = "Info: No file selected"
        except Exception:
            # If some data from the dict cannot be saved in json
            # unlikely in this script
            label["text"] = "Info: Not a valid json data?"
        else:
            label["text"] = "Info: Data saved to file"

data_dict = None

root = Tk()

root.title("Test filedialog")

frame = Frame(root)
frame.pack()

label = Label(frame, text = "Info:", width=30)
label.pack()

Button(frame, text="load json", command = load_json).pack()
Button(frame, text="save json", command = save_json).pack()

root.mainloop()

