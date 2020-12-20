from HoverButton import HoverButton
from tkinter import Frame, FLAT, GROOVE
from matrix_unary_window import matrix_unary_window

# frame for unary operations buttons
frame_buttons_unary = Frame(matrix_unary_window, relief=FLAT, bd=3, bg="gray70")
# frame for matrix 1, upper section
frame1up = Frame(matrix_unary_window, relief=GROOVE, bd=3, bg="saddle brown")
# frame for matrix 1, lower section
frame1lower = Frame(matrix_unary_window, relief=GROOVE, bd=3, bg="saddle brown")

# unary operations buttons
determinant = HoverButton(frame_buttons_unary, text="DET", padx=15, pady=15, bg="white",
						  fg="midnight blue", activebackground="gray87")
eigen_value = HoverButton(frame_buttons_unary, text="EIGVAL", padx=10, pady=15, bg="white",
						  fg="midnight blue", activebackground="gray87")
inverse = HoverButton(frame_buttons_unary, text="INVERSE", padx=10, pady=15, bg="white",
					  fg="midnight blue", activebackground="gray87")
null_space = HoverButton(frame_buttons_unary, text="NULL", padx=15, pady=15, bg="white",
						fg="midnight blue", activebackground="gray87")
rank = HoverButton(frame_buttons_unary, text="RANK", padx=5, pady=15, bg="white",
				   fg="midnight blue", activebackground="gray87")
trace = HoverButton(frame_buttons_unary, text="TRACE", padx=5, pady=15, bg="white",
					fg="midnight blue", activebackground="gray87")
transpose = HoverButton(frame_buttons_unary, text="TRANSPOSE", padx=0, pady=15, bg="white",
						fg="midnight blue", activebackground="gray87")

objects_matrix_unary = {'frame_buttons_unary': frame_buttons_unary, 'frame1up': frame1up, 'frame1lower': frame1lower,
						'determinant': determinant, 'eigen_value': eigen_value, 'inverse': inverse,
						'null_space': null_space, 'rank': rank, 'trace': trace, 'transpose': transpose}
