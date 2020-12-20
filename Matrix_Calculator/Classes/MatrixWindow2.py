from tkinter import Toplevel
# Top level settings


class MatrixWindow(Toplevel):
	# initialize the window
	def __init__(self, master, configure, mode, **kw):
		# initialize the super class 'Toplevel'
		super().__init__(master=master, **kw)
		# default row and columns for the matrix
		self.__row_count1 = 3
		self.__col_count1 = 3
		self.__row_count2 = 3
		self.__col_count2 = 3
		super().withdraw()
		if mode == 1:
			configure(super(), self.__row_count1, self.__col_count1)
			super().update()
			super().minsize(super().winfo_width(), super().winfo_height())
		elif mode == 2:
			configure(super(), self.__row_count1, self.__col_count1, self.__row_count2, self.__col_count2)

	def change_state(self):
		if super().state == 'withdrawn':
			super().deiconify()
		else:
			super().withdraw()
