from tkinter import Entry


class Matrix:
	def __init__(self, frame_lower, row_count=3, column_count=3):
		self.__frame_lower = frame_lower
		self.__entry_list = []
		self.__row_count = row_count
		self.__column_count = column_count
		self.create_matrix(row_count, column_count)

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

	@property
	def entry_list(self):
		return self.__entry_list

	def create_matrix(self, row_count, column_count):
		if len(self.entry_list) > 0:
			for row in self.entry_list:
				for entry in row:
					entry.destroy()
			self.entry_list.clear()
		for i in range(row_count):
			row = []
			for j in range(column_count):
				entry = Entry(self.__frame_lower, width=4, borderwidth=2, font="Helvetica 10", justify="center")
				entry.grid(row=i, column=j, ipadx=15, ipady=15, sticky="NSEW")
				entry.grid_propagate(False)
				row.append(entry)
			self.entry_list.append(row)
		self.row_count = row_count
		self.column_count = column_count
