from tkinter import *
from Classes.HoverButton import *

m = 3
n = 3
x = 4
y = 5

# Top level settings
matrix_unary_window = Tk()
matrix_unary_window.title("Simple Calculator > Matrix Unary Calculator")
matrix_unary_window.minsize(300 + 60 * m, 43 + max(172, n * 57))
matrix_unary_window.configure(bg="gray87")

row_count_root = max(4, n + 1)
col_count_root = m + 3

# Top level grid settings
for i in range(row_count_root):
	Grid.rowconfigure(matrix_unary_window, i, weight=1)
for i in range(col_count_root):
	Grid.columnconfigure(matrix_unary_window, i, weight=1)

# frame for unary operations buttons
frame_buttons_unary = Frame(matrix_unary_window, relief=FLAT, bd=3, bg="gray70")
frame_buttons_unary.config(highlightbackground="red")
frame_buttons_unary.grid(row=0, column=0, rowspan=4, columnspan=3, sticky="NSEW")

# set weights for rows and columns in frame_buttons_unary
for i in range(4):
	Grid.rowconfigure(frame_buttons_unary, i, weight=1)
for i in range(3):
	Grid.columnconfigure(frame_buttons_unary, i, weight=1)

# output space
output_space = Entry(frame_buttons_unary, width=20, borderwidth=3)
output_space.grid(row=0, column=0, columnspan=3, sticky="NSEW")


# unary operations buttons grid settings
button_determinant.grid(row=1, column=0, sticky="NSEW")
button_eigen_value.grid (row=1, column=1, sticky="NSEW")
button_inverse.grid    (row=1, column=2, sticky="NSEW")
button_nullspace.grid  (row=2, column=0, sticky="NSEW")
button_rank.grid	   (row=2, column=1, sticky="NSEW")
button_trace.grid      (row=2, column=2, sticky="NSEW")
button_transpose.grid  (row=3, column=1, sticky="NSEW")


# frame for matrix 1, upper section
frame1up = Frame(matrix_unary_window, relief=GROOVE, bd=3, bg="saddle brown")
frame1up.grid(row=0, column=3, columnspan=n, sticky="NSEW")

Grid.rowconfigure(frame1up, 0, weight=1)
Grid.rowconfigure(frame1up, 1, weight=1)
Grid.columnconfigure(frame1up, 0, weight=1)

# a static text "matrix_size:(default='3x3')"
text_matrix = Label(frame1up, anchor=CENTER, bd=3, text="matrix_size:(default='3x3')")
text_matrix.grid(row=0, column=0, columnspan=2, sticky="NSEW")

# input box for matrix size
size_entry = Entry(frame1up, width=7, borderwidth=3, justify=CENTER)
size_entry.insert(INSERT, "3 x 3")
size_entry.grid(row=0, column=2, sticky="NSEW")

# button for creating matrix with size m x n
button_create_matrix = HoverButton(matrix_unary_window, text="create m x n matrix", padx=25, pady=15, bg="white",
								   fg="midnight blue", activebackground="gray87")
button_create_matrix.grid(row=1, column=2, sticky="NSEW")


# frame for matrix 1, lower section
frame1lower = Frame(matrix_unary_window, relief=GROOVE, bd=3, bg="saddle brown")
frame1lower.grid(row=1, column=3, rowspan=m, columnspan=n, sticky="NSEW")

for i in range(m):
	Grid.rowconfigure(frame1lower, i, weight=1)
for i in range(n):
	Grid.columnconfigure(frame1lower, i, weight=1)

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

matrix_unary_window.mainloop()
