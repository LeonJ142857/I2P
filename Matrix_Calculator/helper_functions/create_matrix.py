from tkinter import Frame, Grid, Entry, Toplevel

def create_matrix(m, n):
	root2 = Toplevel()
	entry_list = []
	#root2.geometry()
	matrix_frame = Frame(root2, padx=n*30, pady=(m+1)*15)
	for i, j in zip(range(m), range(n)):
		Grid.rowconfigure(root2, i, weight=1)
		Grid.columnconfigure(root2, j, weight=1)
	for i in range(m):
		for j in range(n):
			entry_list.append(Entry(root2, width=20, borderwidth=3))
			entry_list[i*j].grid(row=i, column=j, padx=5, pady=5)






















