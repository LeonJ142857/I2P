from HoverButton import HoverButton
from tkinter import *
from MatrixWindow import MatrixWindow
from root_window import root_window
from Matrix import Matrix
from helper_functions import create_matrix
from UnOpsMatrix import UnOpsMatrix


matrix_unary_window = MatrixWindow(root_window, bg='gray87')
# frame for unary operations buttons
frame_buttons_unary = Frame(matrix_unary_window, relief=FLAT, bd=3, bg="gray70")
# frame for matrix 1, upper section
frame1up = Frame(matrix_unary_window, relief=GROOVE, bd=3, bg="gray70")
# frame for matrix 1, lower section
frame1lower = Frame(matrix_unary_window, relief=GROOVE, bd=3, bg="saddle brown")
matrix_unary = Matrix(frame1lower)
# a static text "matrix_size:"
text_matrix = Label(frame1up, anchor=CENTER, bd=3, text="matrix_size:")

# input box for matrix size
size_entry = Entry(frame1up, width=7, borderwidth=3, justify=CENTER)

# button for creating matrix with size m x n
button_create_matrix = HoverButton(
	frame1up, text="create m x n matrix", padx=0, pady=5, bg="white", fg="midnight blue",
	command=lambda:create_matrix(matrix_unary_window, frame1up, frame1lower, matrix_unary, size_entry), activebackground="gray87")

# output space
output_space = Text(frame_buttons_unary, height=3, bd=3, width=20, wrap=NONE)

un_ops_matrix = UnOpsMatrix(output_space)

# unary operations buttons
determinant = \
	HoverButton(
		frame_buttons_unary, text="DET", padx=15, pady=15,
		command=lambda: un_ops_matrix.determinant(matrix_unary.entry_list),
		bg="white", fg="midnight blue", activebackground="gray87"
	)
eigen_value = \
	HoverButton(
		frame_buttons_unary, text="EIGVAL", padx=10, pady=15,
		command=lambda: un_ops_matrix.eigen_value(matrix_unary.entry_list),
		bg="white", fg="midnight blue", activebackground="gray87"
	)
inverse = \
	HoverButton(
		frame_buttons_unary, text="INVERSE", padx=10, pady=15,
		command=lambda: un_ops_matrix.inverse(matrix_unary.entry_list),
		bg="white", fg="midnight blue", activebackground="gray87"
	)
null_space = \
	HoverButton(
		frame_buttons_unary, text="NULL", padx=15, pady=15,
		command=lambda: un_ops_matrix.null_space(matrix_unary.entry_list),
		bg="white", fg="midnight blue", activebackground="gray87"
	)
rank = \
	HoverButton(
		frame_buttons_unary, text="RANK", padx=5, pady=15,
		command=lambda: un_ops_matrix.rank(matrix_unary.entry_list),
		bg="white", fg="midnight blue", activebackground="gray87"
	)
trace = \
	HoverButton(
		frame_buttons_unary, text="TRACE", padx=5, pady=15,
		command=lambda: un_ops_matrix.trace(matrix_unary.entry_list),
		bg="white", fg="midnight blue", activebackground="gray87"
	)
transpose = \
	HoverButton(
		frame_buttons_unary, text="TRANSPOSE", padx=0, pady=15,
		command=lambda: un_ops_matrix.transpose(matrix_unary.entry_list),
		bg="white", fg="midnight blue", activebackground="gray87"
	)

objects_matrix_unary = {
	'matrix_unary_window': matrix_unary_window, 'text_matrix': text_matrix, 'size_entry': size_entry,
	'button_create_matrix': button_create_matrix, 'frame_buttons_unary': frame_buttons_unary,
	'frame1up': frame1up, 'frame1lower': frame1lower, 'determinant': determinant, 'eigen_value': eigen_value,
	'output_space': output_space, 'inverse': inverse, 'null_space': null_space, 'rank': rank, 'trace': trace,
	'transpose': transpose
}
