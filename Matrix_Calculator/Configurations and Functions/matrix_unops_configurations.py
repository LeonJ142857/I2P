from tkinter import *


def configure_unops(objects_matrix_unary, matrix_unary):
	# renaming for easier access
	button_create_matrix = objects_matrix_unary['button_create_matrix']
	determinant = objects_matrix_unary['determinant']
	eigen = objects_matrix_unary['eigen']
	frame_buttons_unary = objects_matrix_unary['frame_buttons_unary']
	frame1up = objects_matrix_unary['frame1up']
	frame1lower = objects_matrix_unary['frame1lower']
	inverse = objects_matrix_unary['inverse']
	matrix_unary_window = objects_matrix_unary['matrix_unary_window']
	null_space = objects_matrix_unary['null_space']
	output_space = objects_matrix_unary['output_space']
	rank = objects_matrix_unary['rank']
	size_entry = objects_matrix_unary['size_entry']
	trace = objects_matrix_unary['trace']
	transpose = objects_matrix_unary['transpose']
	text_matrix = objects_matrix_unary['text_matrix']
	buttons = [button_create_matrix, determinant, eigen, inverse, null_space,
			   output_space, rank, size_entry, trace, transpose, text_matrix]

	for widget in buttons:
		widget.grid_propagate(False)

	matrix_unary_window.title("Classic Calculator > Matrix Unary Calculator")
	matrix_unary_window.protocol("WM_DELETE_WINDOW", matrix_unary_window.withdraw)
	unary_window_width = 240 + 60 * 3
	unary_window_height = 65 + max(100, 53 * 3)
	unary_init_x = 50 + 390
	unary_init_y = 50
	matrix_unary_window.geometry(f'{unary_window_width}x{unary_window_height}+{unary_init_x}+{unary_init_y}')
	matrix_unary_window.resizable(width=False, height=False)

	# unary operations objects positioning
	frame_buttons_unary.grid (row=0, column=0, rowspan=4, columnspan=3)
	frame1up.grid			 (row=0, column=3, 			  columnspan=3)
	frame1lower.grid		 (row=1, column=3, rowspan=3, columnspan=3)
	determinant.grid		 (row=1, column=0)
	eigen.grid				 (row=1, column=1)
	inverse.grid    		 (row=1, column=2)
	null_space.grid 		 (row=2, column=0)
	rank.grid	    		 (row=2, column=1)
	trace.grid      		 (row=2, column=2)
	transpose.grid  		 (row=3, column=1)
	button_create_matrix.grid(row=1, column=1)
	size_entry.grid			 (row=0, column=1)
	text_matrix.grid		 (row=0, column=0)
	output_space.grid		 (row=0, column=0, 			  columnspan=3, ipady=2)

	size_entry.insert(INSERT, "3 x 3")
	output_space.insert(INSERT, "This is where you will see the output.")
