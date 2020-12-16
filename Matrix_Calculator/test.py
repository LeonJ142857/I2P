from tkinter import *
from Classes.HoverButton import *
m = 4
n = 4
x = 4
y = 5
root = Tk()
root.title("Simple Calculator > Matrix Unary Calculator")
root.minsize(240+60*m, 43 + max(172, n * 57))
io_space = Entry(root, width=20, borderwidth=3)
io_space.grid(row=0, column=0, columnspan=3, sticky="NSEW")

# UNARY OPERATIONS
button_determinant = HoverButton(root, text="DET", padx=15, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_eigenValue = HoverButton(root, text="EIGVAL", padx=10, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_inverse = HoverButton(root, text="INVERSE", padx=10, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_nullspace = HoverButton(root, text="NULL", padx=15, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_rank = HoverButton(root, text="RANK", padx=5, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_trace = HoverButton(root, text="TRACE", padx=5, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_transpose = HoverButton(root, text="TRANSPOSE", padx=0, pady=15, bg="white", fg="midnight blue", activebackground="gray87")

# BINARY OPERATIONS
button_add = HoverButton(root, text="+", padx=25, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_cross = HoverButton(root, text="CROSS(X)", padx=25, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_dot = HoverButton(root, text="DOT(.)", padx=25, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_eigenVector = HoverButton(root, text="EIGVEC", padx=25, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_inner = HoverButton(root, text="INNER", padx=25, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_matrix_multiplication = HoverButton(root, text="*", padx=25, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_norm = HoverButton(root, text="NORM", padx=25, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_outer = HoverButton(root, text="OUTER", padx=25, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_scalar_multiplication = HoverButton(root, text="SCALE", padx=25, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_solve = HoverButton(root, text="SOLVE", padx=25, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_subtract = HoverButton(root, text="-", padx=25, pady=15, bg="white", fg="midnight blue", activebackground="gray87")
button_tensor_product = HoverButton(root, text="T_PRODUCT", padx=25, pady=15, bg="white", fg="midnight blue", activebackground="gray87")

button_determinant.grid(row=1, column=0, sticky="NSEW")
button_eigenValue.grid (row=1, column=1, sticky="NSEW")
button_inverse.grid    (row=1, column=2, sticky="NSEW")
button_nullspace.grid  (row=2, column=0, sticky="NSEW")
button_rank.grid	   (row=2, column=1, sticky="NSEW")
button_trace.grid      (row=2, column=2, sticky="NSEW")
button_transpose.grid  (row=3, column=1, sticky="NSEW")


for i in range(4+m+1):
	Grid.rowconfigure(root, i, weight=1)
for i in range(3+n+1):
	Grid.columnconfigure(root, i, weight=1)


frame = Frame(root, relief=GROOVE, bd=3, bg="saddle brown")
frame.grid(row=0, column=4, columnspan=n, sticky="NSEW")
text_matrix = Label(frame, anchor=CENTER, bd=3, text="matrix_size:(default='3x3')")
text_matrix.grid(row=0, column=0, sticky="NSEW")
size_entry = Entry(frame, width=7, borderwidth=3, justify=CENTER)
size_entry.grid(row=1, column=0, sticky="NSEW")

Grid.rowconfigure(frame, 0, weight=1)
Grid.rowconfigure(frame, 1, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

entry_list1 = []
for i in range(m):
	row = []
	for j in range(n):
		entry = Entry(root, width=4, borderwidth=2, font="Helvetica 10", justify="center")
		entry.grid(row=i+1, column=j+4, ipadx=15, ipady=15, sticky="NSEW")
		row.append(entry)
	entry_list1.append(row)


root.mainloop()
