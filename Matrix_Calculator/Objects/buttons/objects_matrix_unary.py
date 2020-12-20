from HoverButton import HoverButton
from matrix_unary_window import * # circular

# unary operations buttons
determinant = HoverButton(frame_buttons_unary, text="DET", padx=15, pady=15, bg="white",
						  fg="midnight blue", activebackground="gray87")
eigen_value = HoverButton(frame_buttons_unary, text="EIGVAL", padx=10, pady=15, bg="white",
						  fg="midnight blue", activebackground="gray87")
inverse = HoverButton(frame_buttons_unary, text="INVERSE", padx=10, pady=15, bg="white",
					  fg="midnight blue", activebackground="gray87")
nullspace = HoverButton(frame_buttons_unary, text="NULL", padx=15, pady=15, bg="white",
						fg="midnight blue", activebackground="gray87")
rank = HoverButton(frame_buttons_unary, text="RANK", padx=5, pady=15, bg="white",
				   fg="midnight blue", activebackground="gray87")
trace = HoverButton(frame_buttons_unary, text="TRACE", padx=5, pady=15, bg="white",
					fg="midnight blue", activebackground="gray87")
transpose = HoverButton(frame_buttons_unary, text="TRANSPOSE", padx=0, pady=15, bg="white",
						fg="midnight blue", activebackground="gray87")
