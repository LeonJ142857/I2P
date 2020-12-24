from tkinter import *


def configure_unops(objects_matrix_unary, matrix_unary):
	# renaming for easier access
	button_create_matrix = objects_matrix_unary['button_create_matrix']
	determinant = objects_matrix_unary['determinant']
	eigen_value = objects_matrix_unary['eigen_value']
	frame_buttons_unary = objects_matrix_unary['frame_buttons_unary']
	frame1up = objects_matrix_unary['frame1up']
	frame1lower = objects_matrix_unary['frame1lower']
	inverse = objects_matrix_unary['inverse']
	matrix_unary_window = objects_matrix_unary['matrix_unary_window']
	m = matrix_unary.row_count
	n = matrix_unary.column_count
	null_space = objects_matrix_unary['null_space']
	output_space = objects_matrix_unary['output_space']
	rank = objects_matrix_unary['rank']
	size_entry = objects_matrix_unary['size_entry']
	trace = objects_matrix_unary['trace']
	transpose = objects_matrix_unary['transpose']
	text_matrix = objects_matrix_unary['text_matrix']
	buttons = [button_create_matrix, determinant, eigen_value, inverse, null_space,
			   output_space, rank, size_entry, trace, transpose, text_matrix]

	for widget in buttons:
		widget.grid_propagate(False)

	matrix_unary_window.title("Classic Calculator > Matrix Unary Calculator")
	matrix_unary_window.protocol("WM_DELETE_WINDOW", matrix_unary_window.withdraw)
	unary_window_width = 240 + 60 * 3
	unary_window_height = 43 + max(100, 60 * 3)
	unary_init_x = 50 + 390
	unary_init_y = 50
	matrix_unary_window.geometry(f'{unary_window_width}x{unary_window_height}+{unary_init_x}+{unary_init_y}')
	matrix_unary_window.resizable(width=False, height=False)

	# creating m x n entry boxes inside frame 1 lower section
	matrix_unary.create_matrix(m, n)

	# unary operations objects positioning
	frame_buttons_unary.grid(row=0, column=0, rowspan=4, columnspan=3, sticky="NSEW")
	frame1up.grid(row=0, column=3, columnspan=3, sticky="NSEW")
	frame1lower.grid(row=1, column=3, rowspan=3, columnspan=3, sticky="NSEW")
	determinant.grid(row=1, column=0, sticky="NSEW")
	eigen_value.grid(row=1, column=1, sticky="NSEW")
	inverse.grid    (row=1, column=2, sticky="NSEW")
	null_space.grid (row=2, column=0, sticky="NSEW")
	rank.grid	    (row=2, column=1, sticky="NSEW")
	trace.grid      (row=2, column=2, sticky="NSEW")
	transpose.grid  (row=3, column=1, sticky="NSEW")
	button_create_matrix.grid(row=1, column=1, sticky="NSEW")
	size_entry.grid(row=0, column=1, sticky="NSEW")
	text_matrix.grid(row=0, column=0, sticky="NSEW")
	output_space.grid(row=0, column=0, columnspan=3, ipady=2, sticky="NSEW")

	size_entry.insert(INSERT, "3 x 3")
