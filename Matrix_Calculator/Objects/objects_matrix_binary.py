from HoverButton import HoverButton
from tkinter import *
from MatrixWindow import MatrixWindow
from root_window import root_window
from Matrix import Matrix
from helper_functions import create_matrix_binary
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
		command=lambda: create_matrix_binary(
			matrix_binary_window, frame_1_up, frame_2_up, frame_1_lower,
			frame_2_lower, matrix_binary_1, matrix_binary_2, size_entry_1
		), activebackground="gray87"
	)

button_create_matrix_2 = \
	HoverButton(
		frame_2_up, text="create m x n matrix", padx=0,
		pady=5, bg="white", fg="midnight blue",
		command=lambda: create_matrix_binary(
			matrix_binary_window, frame_2_up, frame_1_up, frame_2_lower,
			frame_1_lower, matrix_binary_2, matrix_binary_1, size_entry_2
		),
		activebackground="gray87"
	)

# output space
output_space = Text(frame_buttons_binary, height=3, bd=3, width=27, wrap=NONE)
# instance of custom-made matrix unary operations class
bin_ops_matrix = BinOpsMatrix(output_space)

# binary operations buttons

# button to get cross product of first matrix with second matrix
cross = \
	HoverButton(
		matrix_binary_window, text="CROSS(X)", padx=6, pady=15, bg="white",
		command=lambda: bin_ops_matrix.cross(
			matrix_binary_1.entry_list, matrix_binary_2.entry_list
		), fg="midnight blue", activebackground="gray87"
	)

# button to get dot product of first matrix with second matrix
dot = \
	HoverButton(
		matrix_binary_window, text="DOT(.)", padx=0, pady=15, bg="white",
		command=lambda: bin_ops_matrix.dot(
			matrix_binary_1.entry_list, matrix_binary_2.entry_list
		), fg="midnight blue", activebackground="gray87"
	)

# button to get inner product of first matrix with second matrix
inner = \
	HoverButton(
		matrix_binary_window, text="INNER", padx=0, pady=15, bg="white",
		command=lambda: bin_ops_matrix.inner(
			matrix_binary_1.entry_list, matrix_binary_2.entry_list
		), fg="midnight blue", activebackground="gray87"
	)

# button to get the matrix with elements the sum of each element in the same index(order doesn't matter)
matrix_add = \
	HoverButton(
		matrix_binary_window, text="ADD", padx=0, pady=15, bg="white",
		command=lambda: bin_ops_matrix.matrix_add(
			matrix_binary_1.entry_list, matrix_binary_2.entry_list
		), fg="midnight blue", activebackground="gray87"
	)

# button to get matrix that result from first matrix multiplied with second matrix
matrix_multiplication = \
	HoverButton(
		matrix_binary_window, text="MULT", padx=0, pady=15, bg="white",
		command=lambda: bin_ops_matrix.matrix_multiplication(
			matrix_binary_1.entry_list, matrix_binary_2.entry_list
		), fg="midnight blue", activebackground="gray87"
	)

# button to get outer product of first matrix with second matrix
outer = \
	HoverButton(
		matrix_binary_window, text="OUTER", padx=0, pady=15, bg="white",
		command=lambda: bin_ops_matrix.outer(
			matrix_binary_1.entry_list, matrix_binary_2.entry_list
		), fg="midnight blue", activebackground="gray87"
	)

# button to get matrix that results from multiplying each element by a number
scalar_multiplication = \
	HoverButton(
		matrix_binary_window, text="SCALE", padx=0, pady=15, bg="white",
		command=lambda: bin_ops_matrix.scalar_multiplication(
			matrix_binary_1.entry_list, matrix_binary_2.entry_list
		), fg="midnight blue", activebackground="gray87"
	)

# button to solve system of linear equation (order matters)
solve = \
	HoverButton(
		matrix_binary_window, text="SOLVE", padx=15, pady=15, bg="white",
		command=lambda: bin_ops_matrix.solve(
			matrix_binary_1.entry_list, matrix_binary_2.entry_list
		), fg="midnight blue", activebackground="gray87"
	)

# button to get the matrix with elements the result of each element in the first matrix
# subtracted with each element in the second matrix in the same index (order doesn't matter)
subtract = \
	HoverButton(
		matrix_binary_window, text="SUBTRACT", padx=4, pady=15, bg="white",
		command=lambda: bin_ops_matrix.subtract(
			matrix_binary_1.entry_list, matrix_binary_2.entry_list
		), fg="midnight blue", activebackground="gray87"
	)

# dictionary full of widgets for matrix binary operations to make it easier to be passed to a function
objects_matrix_binary = {
	'matrix_binary_window': matrix_binary_window, 'text_matrix_1': text_matrix_1,
	'cross': cross, 'dot': dot, 'inner': inner, 'matrix_add': matrix_add,
	'matrix_multiplication': matrix_multiplication, 'outer': outer,
	'scalar_multiplication': scalar_multiplication, 'solve': solve, 'subtract': subtract,
	'text_matrix_2': text_matrix_2, 'size_entry_1': size_entry_1,
	'size_entry_2': size_entry_2, 'button_create_matrix_1': button_create_matrix_1,
	'button_create_matrix_2': button_create_matrix_2, 'frame_buttons_binary': frame_buttons_binary,
	'frame_1_up': frame_1_up, 'frame_2_up': frame_2_up, 'frame_1_lower': frame_1_lower,
	'frame_2_lower': frame_2_lower, 'output_space': output_space,
}
