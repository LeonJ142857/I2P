def create_matrix_unary(matrix_unary_window, frame_up, frame_lower, matrix, size_entry):
	m = size_entry.get()[0]
	n = size_entry.get()[4]
	cond1 = isinstance(eval(m), (int, float))
	cond2 = isinstance(eval(n), (int, float))
	cond3 = size_entry.get()[2] == 'x'
	if cond1 and cond2 and cond3:
		m = eval(m)
		n = eval(n)
		matrix.create_matrix(m, n)
		window_width = max(int(225 + 64 * n), int(225 + 64 * 3))
		window_height = max(int(65 + max(120, 52.5 * m)), int(65 + 52.5 * 3))
		matrix_unary_window.geometry(f'{window_width}x{window_height}')
		matrix_unary_window.resizable(width=False, height=False)
		frame_up.grid(row=0, column=3, columnspan=n, sticky="NSEW")
		frame_lower.grid(row=1, column=3, rowspan=m, columnspan=n, sticky="NSEW")



def create_matrix_binary(matrix_binary_window, frame_up_new,
		frame_up_old, frame_lower_new, frame_lower_old,
		matrix_binary_new, matrix_binary_old, size_entry_new
	):
	def cmb_util(opt1, opt2):
		return 3 if opt1 < opt2 else opt2
	m = size_entry_new.get()[0]
	n = size_entry_new.get()[4]
	x = matrix_binary_old.row_count
	y = matrix_binary_old.column_count
	new_column = frame_up_new.grid_info()['column']
	old_column = frame_up_old.grid_info()['column']
	old_rowspan = frame_lower_old.grid_info()['rowspan']
	old_colspan = frame_lower_old.grid_info()['columnspan']
	print(f'new matrix row count:{m}, new matrix column count:{n}')
	print(f'old matrix row count:{x}, old matrix column count:{y}')
	print(f'new frame column position:{new_column}, old frame column position:{old_column}')
	print(f'old frame rowspan:{old_rowspan}, old frame columnspan:{old_colspan}')
	cond1 = isinstance(eval(m), (int, float))
	cond2 = isinstance(eval(n), (int, float))
	cond3 = size_entry_new.get()[2] == 'x'
	newisframe1 = new_column < old_column
	newisframe2 = old_column < new_column
	if cond1 and cond2 and cond3:
		m = eval(m)
		n = eval(n)
		matrix_binary_new.create_matrix(m, n)
		window_width = max(int(225 + 64 * n + 64 * x), int(225 + 64 * 3 + 64 * 3))
		window_height = max(int(65 + max(120, 52.5 * m, 52.5 * x)), int(65 + 52.5 * 3))
		matrix_binary_window.geometry(f'{window_width}x{window_height}')
		matrix_binary_window.resizable(width=False, height=False)
		frame_up_new.grid(
			row=0, column=3 if newisframe1 else old_column+3,
			columnspan=n, sticky="NSEW"
		)
		print(frame_up_new.grid_info()['column'])
		frame_up_old.grid(
			row=0, column=3 if newisframe2 else new_column+3,
			columnspan=old_colspan, sticky="NSEW"
		)
		print(frame_up_old.grid_info()['column'])
		frame_lower_new.grid(
			row=1, column=3 if newisframe1 else old_column+3,
			rowspan=m, columnspan=n, sticky="NSEW"
		)
		print(frame_lower_new.grid_info()['column'])
		frame_lower_old.grid(
			row=1, column=3 if newisframe2 else new_column+3,
			rowspan=old_rowspan, columnspan=old_colspan, sticky="NSEW"
		)
		print(frame_lower_old.grid_info()['column'])



def on_closing_root(root):
	from tkinter import messagebox
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		root.destroy()


def grid_configure_weights(object_name, row_count, col_count):
	for i in range(row_count):
		object_name.rowconfigure(i, weight=1)
	for i in range(col_count):
		object_name.columnconfigure(i, weight=1)
