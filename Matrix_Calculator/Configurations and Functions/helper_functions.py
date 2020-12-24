def create_matrix(matrix, size_entry):
	m = size_entry.get()[0]
	n = size_entry.get()[4]
	cond1 = isinstance(eval(m), (int, float))
	cond2 = isinstance(eval(n), (int, float))
	cond3 = size_entry.get()[2]
	if cond1 and cond2 and cond3:
		matrix.create_matrix(eval(m), eval(n))


def on_closing_root(root):
	from tkinter import messagebox
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		root.destroy()


def grid_configure_weights(object_name, row_count, col_count):
	for i in range(row_count):
		object_name.rowconfigure(i, weight=1)
	for i in range(col_count):
		object_name.columnconfigure(i, weight=1)
