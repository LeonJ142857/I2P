class Shapes:
	def __init__(self, color="green", filled=True):
		self.__color = color
		self.__filled = filled

	@property
	def color(self):
		return self.__color

	@color.setter
	def color(self, color):
		self.__color = color

	@property
	def filled(self):
		return self.__filled

	@filled.setter
	def filled(self, filled):
		self.__filled = filled

	def __str__(self):
		filled = "filled"
		unfilled = "Not filled"
		return f"A shape with color of {self.color} and {filled if self.filled else unfilled}"
