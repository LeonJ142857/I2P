from HoverButton import HoverButton
from tkinter import *
from MatrixWindow import MatrixWindow
from root_window import root_window
from Matrix import Matrix
from helper_functions import create_matrix
from BinOpsMatrix import BinOpsMatrix

matrix_binary_window = MatrixWindow(root_window, bg='gray87')
# frame for unary operations buttons
frame_buttons_binary = Frame(matrix_binary_window, relief=FLAT, bd=3, bg="gray70")
# frame for matrix 1 and 2, upper section
frame_1_up = Frame(matrix_binary_window, relief=GROOVE, bd=3, bg="gray70")
frame_2_up = Frame(matrix_binary_window, relief=GROOVE, bd=3, bg="gray70")
# frame for matrix 1 and 2, lower section
frame_1_lower = Frame(matrix_binary_window, relief=GROOVE, bd=3, bg="saddle brown")
frame_2_lower = Frame(matrix_binary_window, relief=GROOVE, bd=3, bg="saddle brown")
# instance of custom-made matrix class
matrix_binary_1 = Matrix(frame_1_lower)
matrix_binary_2 = Matrix(frame_2_lower)
# a static text "matrix_size:"
text_matrix_1 = Label(frame_1_up, anchor=CENTER, bd=3, text="matrix_size:")
text_matrix_2 = Label(frame_2_up, anchor=CENTER, bd=3, text="matrix_size:")
# input box for matrix size
size_entry_1 = Entry(frame_1_up, width=7, borderwidth=3, justify=CENTER)
size_entry_2 = Entry(frame_2_up, width=7, borderwidth=3, justify=CENTER)

# buttons for creating matrix 1 and matrix2 with size m x n
button_create_matrix_1 = \
	HoverButton(
		frame_1_up, text="create m x n matrix", padx=0,
		pady=5, bg="white", fg="midnight blue",
		command=lambda: create_matrix(
			matrix_binary_window, frame_1_up, frame_1_lower,
			matrix_binary_1, size_entry_1
		), activebackground="gray87"
	)

button_create_matrix_2 = \
	HoverButton(
		frame_2_up, text="create m x n matrix", padx=0,
		pady=5, bg="white", fg="midnight blue",
		command=lambda: create_matrix(
			matrix_binary_window, frame_1_up, frame_1_lower,
			matrix_binary_1, size_entry_1
		),
		activebackground="gray87"
	)


# binary operations buttons
matrix_add = HoverButton(matrix_binary_window, text="+", padx=25, pady=15, bg="white",
						 fg="midnight blue", activebackground="gray87")
cross = HoverButton(matrix_binary_window, text="CROSS(X)", padx=25, pady=15, bg="white",
						   fg="midnight blue", activebackground="gray87")
dot = HoverButton(matrix_binary_window, text="DOT(.)", padx=25, pady=15, bg="white",
						 fg="midnight blue", activebackground="gray87")
inner = HoverButton(matrix_binary_window, text="INNER", padx=25, pady=15, bg="white",
						   fg="midnight blue", activebackground="gray87")
matrix_multiplication = HoverButton(matrix_binary_window, text="*", padx=25, pady=15, bg="white",
										fg="midnight blue", activebackground="gray87")
norm = HoverButton(matrix_binary_window, text="NORM", padx=25, pady=15, bg="white",
						  fg="midnight blue", activebackground="gray87")
outer = HoverButton(matrix_binary_window, text="OUTER", padx=25, pady=15, bg="white",
						   fg="midnight blue", activebackground="gray87")
scalar_multiplication = HoverButton(matrix_binary_window, text="SCALE", padx=25, pady=15, bg="white",
										   fg="midnight blue", activebackground="gray87")
solve = HoverButton(matrix_binary_window, text="SOLVE", padx=25, pady=15, bg="white",
						   fg="midnight blue", activebackground="gray87")
subtract = HoverButton(matrix_binary_window, text="-", padx=25, pady=15, bg="white",
							  fg="midnight blue", activebackground="gray87")
tensor_product = HoverButton(matrix_binary_window, text="T_PRODUCT", padx=25, pady=15, bg="white",
									fg="midnight blue", activebackground="gray87")
