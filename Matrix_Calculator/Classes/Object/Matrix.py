from tkinter import Entry

# Matrix class


class Matrix:
	def __init__(self, frame_lower, row_count=3, column_count=3):
		# lower frame which contains all the entries of a matrix
		self.__frame_lower = frame_lower
		# list of entry widgets
		self.__entry_list = []
		# row and column count of the matrix
		self.__row_count = row_count
		self.__column_count = column_count
		# call create_matrix defined in this class
		self.create_matrix(row_count, column_count)

	# shortcuts for easier calling without double underscore
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

	# function to create new matrix or replace matrix with another with different size
	def create_matrix(self, row_count, column_count):
		# if entry_list is not empty
		if len(self.entry_list) > 0:
			# destroy all objects inside so it doesn't get displayed anymore
			for row in self.entry_list:
				for entry in row:
					entry.destroy()
			# clear the list to remove the objects
			self.entry_list.clear()
		# create new matrix
		for i in range(row_count):
			row = []
			for j in range(column_count):
				# initialize entry widget, set it so that user input aligned to center with a font Helvetica size 10
				# parent widget is self.__frame_lower, width is 4 characters and borderwidth is 2 pixels
				entry = Entry(self.__frame_lower, width=4, borderwidth=2, font="Helvetica 10", justify="center")
				# position the newly initialized entry widget
				entry.grid(row=i, column=j, ipadx=15, ipady=15, sticky="NSEW")
				# make entry widget size fixed
				entry.grid_propagate(False)
				# append entry to row
				row.append(entry)
			# append row to entry_list
			self.entry_list.append(row)
		# set old row count to new row count
		self.row_count = row_count
		# set old column count to new column count
		self.column_count = column_count
