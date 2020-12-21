from MatrixWindow import MatrixWindow


class MatrixUnaryWindow(MatrixWindow):
	def __init__(self, master, matrix, **kw):
		super().__init__(master=master, **kw)
		self.__matrix = matrix
		m = self.__matrix.row_count
		n = self.__matrix.column_count
		self.__row_count = max(m + 1, 4)
		self.__column_count = n + 3
		self.__min_width = 300 + 60 * n


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

	def update_row_col(self, matrix):
		self.row_count = max(matrix.row_count + 1, 4)
		self.column_count = matrix.column_count + 3
