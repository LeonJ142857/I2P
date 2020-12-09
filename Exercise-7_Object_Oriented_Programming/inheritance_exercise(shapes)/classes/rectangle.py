from shapes import Shapes


class Rectangle(Shapes):
	def __init__(self, width=1.0, length=1.0, color="green", filled=True):
		super().__init__(color, filled)
		self.__width = width
		self.__length = length

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, width):
		self.__width = width

	def set_width(self, width):
		self.__width = width

	@property
	def length(self):
		return self.__length

	@length.setter
	def length(self, length):
		self.__length = length

	def set_length(self, length):
		self.__length = length
	@property
	def area(self):
		return self.width * self.length

	@property
	def perimeter(self):
		return 2 * (self.width + self.length)

	def __str__(self):
		return f"A Rectangle with width={self.width} and length={self.length}, which is a subclass of {super().__str__()}"
