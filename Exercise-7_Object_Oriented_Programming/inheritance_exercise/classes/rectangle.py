from shapes import Shapes


class Rectangle(Shapes):
	__width: float
	__length: float

	def __init__(self, width=1.0, length=1.0, color="green", filled=True):
		super().__init__(color, filled)
		self.__width = width
		self.__length = length

	def get_width(self):
		return self.__width

	def set_width(self, width):
		self.__width = width

	def get_length(self):
		return self.__length

	def set_length(self, length):
		self.__length = length

	def get_area(self):
		return self.get_width() * self.get_length()

	def get_perimeter(self):
		return 2 * (self.get_width() + self.get_length())

	def to_string(self):
		return f"A Rectangle with width={self.get_width()} and length={self.get_length()}, which is a subclass of {super().to_string()}"
