from grid_configure_weight import *
from tkinter import *
from objects_matrix_unary import * #circular


def configure_unops(matrix_unary_window, m, n, **kwargs):
	row_count_root = max(4, n + 1)
	col_count_root = m + 3

	# Top level grid settings
	grid_configures(matrix_unary_window, row_count_root, col_count_root)

	# frame_buttons_unary settings
	kwargs['frame_buttons_unary'].grid(row=0, column=0, rowspan=4, columnspan=3, sticky="NSEW")

	# set weights for rows and columns in frame_buttons_unary
	row_count_frame_buttons_unary = 4
	col_count_frame_buttons_unary = 3
	grid_configures(frame_buttons_unary, row_count_frame_buttons_unary, col_count_frame_buttons_unary)

	# output space
	output_space = Entry(frame_buttons_unary, width=20, borderwidth=3)
	output_space.grid(row=0, column=0, columnspan=3, sticky="NSEW")

	# unary operations buttons grid settings
	determinant.grid(row=1, column=0, sticky="NSEW")
	eigen_value.grid (row=1, column=1, sticky="NSEW")
	inverse.grid    (row=1, column=2, sticky="NSEW")
	nullspace.grid  (row=2, column=0, sticky="NSEW")
	rank.grid	   (row=2, column=1, sticky="NSEW")
	trace.grid      (row=2, column=2, sticky="NSEW")
	transpose.grid  (row=3, column=1, sticky="NSEW")

	# frame for matrix 1 upper position
	frame1up.grid(row=0, column=3, columnspan=n, sticky="NSEW")
	row_count_frame1up = 2
	col_count_frame1up = 2
	grid_configures(frame1up, row_count_frame1up, col_count_frame1up)

	# a static text "matrix_size:(default='3x3')"
	text_matrix = Label(frame1up, anchor=CENTER, bd=3, text="matrix_size:")
	text_matrix.grid(row=0, column=0, sticky="NSEW")

	# input box for matrix size
	size_entry = Entry(frame1up, width=7, borderwidth=3, justify=CENTER)
	size_entry.insert(INSERT, "3 x 3")
	size_entry.grid(row=0, column=1, sticky="NSEW")

	# button for creating matrix with size m x n
	button_create_matrix = HoverButton(frame1up, text="create m x n matrix", padx=0, pady=5, bg="white",
									   fg="midnight blue", activebackground="gray87")
	button_create_matrix.grid(row=1, column=1, sticky="NSEW")
	frame1lower.grid(row=1, column=3, rowspan=m, columnspan=n, sticky="NSEW")
	grid_configures(frame1lower, m, n)

	# entry list for all the entry box of which each is for a number
	entry_list1 = []

	# creating m x n entry boxes inside frame 1 lower section
	for i in range(m):
		row = []
		for j in range(n):
			entry = Entry(frame1lower, width=4, borderwidth=2, font="Helvetica 10", justify="center")
			entry.grid(row=i, column=j, ipadx=15, ipady=15, sticky="NSEW")
			row.append(entry)
		entry_list1.append(row)
