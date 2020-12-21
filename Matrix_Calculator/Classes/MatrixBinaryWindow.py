from MatrixWindow import MatrixWindow


class MatrixBinaryWindow(MatrixWindow):
	def __init__(self, master, **kw):
		super().__init__(master=master, **kw)
		self.__row_count1 = 3
		self.__column_count1 = 3
		self.__row_count2 = 3
		self.__column_count2 = 3

	@property
	def row_count1(self):
		return self.__row_count1

	@row_count1.setter
	def row_count1(self, row_count1):
		self.__row_count1 = row_count1

	@property
	def column_count1(self):
		return self.__column_count1

	@column_count1.setter
	def column_count1(self, column_count1):
		self.__column_count1 = column_count1
	
	@property
	def row_count2(self):
		return self.__row_count2

	@row_count2.setter
	def row_count2(self, row_count2):
		self.__row_count2 = row_count2

	@property
	def column_count2(self):
		return self.__column_count2

	@column_count2.setter
	def column_count2(self, column_count2):
		self.__column_count2 = column_count2
