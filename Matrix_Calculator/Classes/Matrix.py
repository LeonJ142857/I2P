from tkinter import Entry


class Matrix:
	def __init__(self, frame_lower, m, n):
		self.__frame_lower = frame_lower
		self.__entry_list = []
		self.__m = m
		self.__n = n
		self.create_matrix(m, n)

	@property
	def entry_list(self):
		return self.__entry_list

	def create_matrix(self, m, n):
		if len(self.entry_list) > 0:
			for row in self.entry_list:
				for entry in row:
					entry.destroy()
		for i in range(m):
			row = []
			for j in range(n):
				entry = Entry(self.__frame_lower, width=4, borderwidth=2, font="Helvetica 10", justify="center")
				entry.grid(row=i, column=j, ipadx=15, ipady=15, sticky="NSEW")
				row.append(entry)
			self.entry_list.append(row)
		self.__m = m
		self.__n = n

