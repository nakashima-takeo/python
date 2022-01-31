from tkinter import Tk, Frame, Label, Button, Canvas, DISABLED, ACTIVE, X
from random import randint
from math import sqrt, pow

# Define the functions we will be using

def new_button_callback():
    """Start a new game:
        trial init
        new goal
        info update
        clean canvas (if necessary)
        set play flag
        disable the new_button
    """
    # Use global variables as we want to assign values
    # that can be accessed from other part of the script
    global goal, trial, is_playing
    trial = 0
    goal = randint(0, width), randint(0, height)
    new_button["state"] = DISABLED
    info_label["text"] = "Trial(s): {}/{}".format(trial, max_trials)
    canvas.delete("feedback")
    is_playing = True

def quit_button_callback():
    """Quit the game
    Call the destroy method of the tkinter main window
    """
    root.destroy()

def mouse_callback(event):
    """ React to user click in the canvas after the game is started.
    Check if the user clicked near enough of the goal => win game.
    Check if the user has used all trials => lose game.
    Give feedback otherwise => red dot getting brighter when closer to goal
    """
    # Use a global variable as we want to assign a value
    # that can be accessed from other part of the script
    global trial

    # We just check the value of is_playing
    # there is no local variable is_playing
    # the function will get the variable from the main unit
    if not is_playing:
        # Nothing happen if the game is not started
        return

    # Update the trial count to the current trial
    # trial is initialized at 0
    trial += 1
    info_label["text"] = "Trial(s): {}/{}".format(trial, max_trials)

    # Get the distance between the click location and the goal
    pos = event.x, event.y
    distance = distance_to_goal(pos)

    # check for the 2 ending conditions first
    # won or reached max_trials
    # We check for winning first as the player can win at the last trial

    # Check for a hit
    # close enough to the goal
    if distance < threshold:
        info_label["text"] = "Trial(s): {}/{} You win".format(trial,
         max_trials)
        end_game()

    # Check if we reached the maximum number of trials
    if trial == max_trials:
        info_label["text"] = "Trial(s): {}/{} You lost".format(trial
        , max_trials)
        end_game()

    # The game did not end
    # Give some feedback to the player
    # Draw a colored dot
    # Note that:
    # 1) the dot location is at the location of the mouse click
    # 2) the dot size is related to the threshold
    # 3) the dot color is related to the distance to the goal
    # 4) the tag "feedback" is set
    bbox = (pos[0] - threshold, pos[1] - threshold, pos[0] + threshold,
     pos[1] + threshold)
    canvas.create_oval(bbox, fill=get_color(distance), outline="",
     tags="feedback")

def distance_to_goal(pos):
    """ Compute the distance to the goal
    """
    # Here we do not assign any value to goal
    # there is no local variable goal in the function
    # no need to use a global modifier
    # the function gets the global goal in any case
    return sqrt(pow(pos[0] - goal[0], 2) + pow(pos[1] - goal[1], 2))

def get_color(d):
    """Returns a red color that is brighter as d is closer to 0
    """
    # Get a color value from the distance d to the goal
    # the distance is smaller than the diagonal of the canvas
    # d <= sqrt(pow(width, 2) + pow(height, 2)
    # v will be in [0, 255]
    # Note that we have v = 255 when d = 0
    # So the dot is brighter when closer to the goal
    v = 255 - int(255 * d / sqrt(pow(width, 2) + pow(height, 2)))
    return "#{:02x}0000".format(v)

def end_game():
    """End the game:
    set flag
    enabel new_button
    """
    # Use a global variable as we want to assign a value
    # that can be accessed from other part of the script
    global is_playing
    is_playing = False
    # enable the new_button for next game start
    new_button["state"] = ACTIVE

# From here we are in the main unit

# These variables will only be read from the functions
# we do not have to declare them as global in the functions
width = 400
height = 300

threshold = 10.0
max_trials = 10

# These 3 variables are modified by some of the functions
# they will be declared as global in the functions
trial = None
goal = None
is_playing = False

# Create the tkinter main window
# it root will be accessed by the quit button callback
root = Tk()

# Set up the GUI
frame = Frame(root)
frame.pack()

info_label = Label(frame, text = "Click new to start")
info_label.pack(fill=X)

canvas = Canvas(frame, width = width, height = height, bg = "#404040")
canvas.pack()

new_button = Button(frame, text = "New", command = new_button_callback)
new_button.pack()

Button(frame, text = "Quit", command = quit_button_callback).pack()

# Bind the mouse callback on the canvas
canvas.bind("<Button-1>", mouse_callback)

# Start the event loop
root.mainloop()