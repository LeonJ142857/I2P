from MatrixWindow2 import MatrixWindow


class MatrixUnaryWindow(MatrixWindow):
	def __init__(self, master, **kw):
		super().__init__(master=master, **kw)
		self.__row_count = 3
		self.__column_count = 3

	@property
	def row_count(self):
		return self.__row_count

	@row_count.setter
	def row_count(self, row_count):
		self.__row_count = row_count

	@property
	def column_count(self):
		return self.__column_count

	@column_count.setter
	def column_count(self, column_count):
		self.__column_count = column_count
