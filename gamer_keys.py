from tkinter import *

# CONSTANTS ->
# background and display colors
BG = "pink"
DISPLAY_FG = "black"
DISPLAY_BG = "white"

# button letter color
B_W = 'red'
B_A = 'orange'
B_S = 'blue'
B_D = 'green'


# ---------------------------------------

# METHODS ->
def w():
    # change display text to "GO FORWARD"
    display_label.config(text="GO FORWARD")


def a():
    # change display text to "GO LEFT"
    display_label.config(text="GO LEFT")


def s():
    # change display text to "GO BACKWARD"
    display_label.config(text="GO BACKWARD")


def d():
    # change display text to "GO RIGHT"
    display_label.config(text="GO RIGHT")


def action(event):
    """
    call function associated with the keyboard key
    :param event: event happened in keyboard
    :return: None
    """
    key = event.keysym

    w() if key in ["W", "w"] else None
    a() if key in ["A", "a"] else None
    s() if key in ["S", "s"] else None
    d() if key in ["D", "d"] else None


# -----------------------------------------------

# GUI
window = Tk()
window.resizable(False, False)
window.title("Game's")

frame = Frame(window, bg=BG, bd=5, relief=SUNKEN)
frame.pack(expand=True)

Button(frame, text="W", font=("Arial", 20, "bold"), width=3, command=w,
       relief=RAISED, bd=5, foreground=B_W).pack(side=TOP)
Button(frame, text="A", font=("Arial", 20, "bold"), width=3, command=a,
       relief=RAISED, bd=5, foreground=B_A).pack(side=LEFT)
Button(frame, text="S", font=("Arial", 20, "bold"), width=3, command=s,
       relief=RAISED, bd=5, foreground=B_S).pack(side=LEFT)
Button(frame, text="D", font=("Arial", 20, "bold"), width=3, command=d,
       relief=RAISED, bd=5, foreground=B_D).pack(side=LEFT)

# checks if any event happened in keyboard if yes action function is called
window.bind('<Key>', action)

# label to show happening events
display_label = Label(window, font=("Arial", 18, "bold"), width=13, relief=RAISED,
                      bd=5, foreground=DISPLAY_FG, background=DISPLAY_BG)
display_label.pack(side=BOTTOM)

window.mainloop()

# -------------------------------------------------------------------------------
# copyright 2022 malik-l0l
