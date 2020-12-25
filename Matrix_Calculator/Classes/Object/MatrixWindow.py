from tkinter import Toplevel
# Top level settings


class MatrixWindow(Toplevel):
	# initialize the window
	def __init__(self, master, **kw):
		# initialize the super class 'Toplevel'
		super().__init__(master=master, **kw)
		# default row and columns for the matrix
		super().withdraw()

	def change_state(self):
		if super().state() == 'withdrawn':
			super().deiconify()
		else:
			super().withdraw()
