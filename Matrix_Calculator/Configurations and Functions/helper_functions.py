def create_matrix(matrix_unary_window, frame1up, frame1lower, matrix, size_entry):
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
		frame1up.grid(row=0, column=3, columnspan=n, sticky="NSEW")
		frame1lower.grid(row=1, column=3, rowspan=m, columnspan=n, sticky="NSEW")


def on_closing_root(root):
	from tkinter import messagebox
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		root.destroy()


def grid_configure_weights(object_name, row_count, col_count):
	for i in range(row_count):
		object_name.rowconfigure(i, weight=1)
	for i in range(col_count):
		object_name.columnconfigure(i, weight=1)
