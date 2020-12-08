class Shapes:
	def __init__(self, color="green", filled=True):
		self.__color = color
		self.__filled = filled

	def get_color(self):
		return self.__color

	def set_color(self, color):
		self.__color = color

	def is_filled(self):
		return self.__filled

	def set_filled(self, filled):
		self.__filled = filled

	def to_string(self):
		return f"A shape with color of {self.get_color()} and {self.is_filled()}"
