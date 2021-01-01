from tkinter import Tk, Entry

Euler = '2.7182818284590452353602874713527'
PI = '3.1415926535897932384626433832795'

# initialize root window
root_window = Tk()
# give title to root window
root_window.title("Classic Calculator")

# initialize entry widget for input output space for the classical calculator
io_space = Entry(root_window, width=40, borderwidth=3, font=("TimesNewRoman 12"))
# set the position of io_space for display
io_space.grid(row=0, column=0, columnspan=5, padx=10, ipady=5)

