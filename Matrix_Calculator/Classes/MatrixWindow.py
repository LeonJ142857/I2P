from tkinter import Toplevel
# Top level settings


class MatrixWindow():
	# initialize the window
	def __init__(self, root, title, bg, configure_unops, row_count_matrix=3, col_count_matrix=3):
		self.__window = Toplevel(root)
		self.__title = title
		self.__width = 43 + max(172, 57 * col_count_matrix)
		self.__height = 300 + 60 * row_count_matrix
		self.__window_bg = bg
		self.__row_count = row_count_matrix
		self.__col_count = col_count_matrix
		self.__window.withdraw()
		self.configure_window(self.__window, self.__title, self.__height, self.__width, self.__window_bg)
		configure_unops(self.__window, self.__row_count, self.__col_count)
	def change_state(self):
		if self.window.state == 'withdrawn':
			self.window.deiconify()
		else:
			self.window.withdraw()

	def configure_window(self, window, title, height, width, bg):
		window.title(title)
		window.minsize(height, width)
		window.configure(bg=bg)

	@property
	def window(self):
		return self.__window

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, height):
		self.__height = height

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, width):
		self.__width = width
