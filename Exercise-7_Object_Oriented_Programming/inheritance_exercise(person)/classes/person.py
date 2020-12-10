class Person:
	def __init__(self, name, address):
		self.__name = name
		self.__address = address

	@property
	def name(self):
		return self.__name

	@property
	def address(self):
		return self.__address

	@address.setter
	def address(self, address):
		self.__address = address

	def __str__(self):
		return f"{self.name}({self.address})"
