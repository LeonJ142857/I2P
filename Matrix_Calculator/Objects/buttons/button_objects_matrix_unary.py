from Classes.HoverButton import *
from frames import frame_buttons_unary
# unary operations buttons
button_determinant = HoverButton(frame_buttons_unary, text="DET", padx=15, pady=15, bg="white",
								 fg="midnight blue", activebackground="gray87")
button_eigen_value = HoverButton(frame_buttons_unary, text="EIGVAL", padx=10, pady=15, bg="white",
								 fg="midnight blue", activebackground="gray87")
button_inverse = HoverButton(frame_buttons_unary, text="INVERSE", padx=10, pady=15, bg="white",
							 fg="midnight blue", activebackground="gray87")
button_nullspace = HoverButton(frame_buttons_unary, text="NULL", padx=15, pady=15, bg="white",
							   fg="midnight blue", activebackground="gray87")
button_rank = HoverButton(frame_buttons_unary, text="RANK", padx=5, pady=15, bg="white",
						  fg="midnight blue", activebackground="gray87")
button_trace = HoverButton(frame_buttons_unary, text="TRACE", padx=5, pady=15, bg="white",
						   fg="midnight blue", activebackground="gray87")
button_transpose = HoverButton(frame_buttons_unary, text="TRANSPOSE", padx=0, pady=15, bg="white",
							   fg="midnight blue", activebackground="gray87")
