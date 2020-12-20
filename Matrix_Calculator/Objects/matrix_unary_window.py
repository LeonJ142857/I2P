from MatrixWindow2 import MatrixWindow
from tkinter import Frame, FLAT, GROOVE
from root_window import root_window
from matrix_unops_configurations import configure_unops # circular

title = "Classic Calculator > Matrix Unary Calculator"
background = "gray87"
width = 43 + max(172, 57 * 3)
height = 300 + 60 * 3
matrix_unary_window = MatrixWindow(root_window, configure_unops, 1, bg=background, width=width, height=height)
matrix_unary_window.title(title)

# frame for unary operations buttons
frame_buttons_unary = Frame(matrix_unary_window, relief=FLAT, bd=3, bg="gray70")
# frame for matrix 1, upper section
frame1up = Frame(matrix_unary_window, relief=GROOVE, bd=3, bg="saddle brown")
# frame for matrix 1, lower section
frame1lower = Frame(matrix_unary_window, relief=GROOVE, bd=3, bg="saddle brown")


