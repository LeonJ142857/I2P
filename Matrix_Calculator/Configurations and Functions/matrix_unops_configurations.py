from tkinter import *


def configure_unops(grid_configures, objects_matrix_unary):
	# renaming for easier access
	button_create_matrix = objects_matrix_unary['button_create_matrix']
	determinant = objects_matrix_unary['determinant']
	eigen_value = objects_matrix_unary['eigen_value']
	frame_buttons_unary = objects_matrix_unary['frame_buttons_unary']
	frame1up = objects_matrix_unary['frame1up']
	frame1lower = objects_matrix_unary['frame1lower']
	inverse = objects_matrix_unary['inverse']
	matrix_unary_window = objects_matrix_unary['matrix_unary_window']
	matrix_unary = objects_matrix_unary['matrix_unary']
	m = matrix_unary.row_count
	n = matrix_unary.column_count
	null_space = objects_matrix_unary['null_space']
	output_space = objects_matrix_unary['output_space']
	rank = objects_matrix_unary['rank']
	size_entry = objects_matrix_unary['size_entry']
	trace = objects_matrix_unary['trace']
	transpose = objects_matrix_unary['transpose']
	text_matrix = objects_matrix_unary['text_matrix']

	# matrix unary window settings
	window_width = 300 + 100 * n
	window_height = 43 + max(100, 120 * m)
	matrix_unary_window.minsize(window_width, window_height)
	matrix_unary_window.maxsize(window_width, window_height)
	matrix_unary_window.title("Classic Calculator > Matrix Unary Calculator")
	matrix_unary_window.protocol("WM_DELETE_WINDOW", matrix_unary_window.withdraw)
	row_count_window = max(4, m + 1)
	col_count_window = n + 3

	# set weights for rows and columns in matrix_unary_window
	grid_configures(matrix_unary_window, row_count_window, col_count_window)


	# set weights for rows and columns in frame_buttons_unary
	row_count_frame_buttons_unary = 4
	col_count_frame_buttons_unary = 3
	grid_configures(frame_buttons_unary, row_count_frame_buttons_unary, col_count_frame_buttons_unary)


	# unary operations buttons grid settings
	# frame_buttons_unary settings
	frame_buttons_unary.grid(row=0, column=0, rowspan=4, columnspan=3, sticky="NSEW")
	frame1up.grid(row=0, column=3, columnspan=n, sticky="NSEW")
	frame1lower.grid(row=1, column=3, rowspan=m, columnspan=n, sticky="NSEW")
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
	output_space.grid(row=0, column=0, columnspan=3, sticky="NSEW")


	# frame for matrix 1 upper position
	row_count_frame1up = 2
	col_count_frame1up = 2
	grid_configures(frame1up, row_count_frame1up, col_count_frame1up)


	size_entry.insert(INSERT, "3 x 3")

	grid_configures(frame1lower, m, n)

	# creating m x n entry boxes inside frame 1 lower section
	matrix_unary.create_matrix(m, n)
