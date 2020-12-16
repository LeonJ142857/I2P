from tkinter import Tk, Entry

Euler = '2.7182818284590452353602874713527'
PI = '3.1415926535897932384626433832795'

root = Tk()
root.title("Simple Calculator")
io_space = Entry(root, width=20, borderwidth=3)
io_space.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
