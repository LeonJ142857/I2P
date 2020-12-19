def grid_configures(object_name, row_count, col_count):
	from tkinter import Grid
	for i in range(row_count):
		Grid.rowconfigure(object_name, i, weight=1)
	for i in range(col_count):
		Grid.columnconfigure(object_name, i, weight=1)
