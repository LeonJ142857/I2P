from shapes import Shapes
from math import pi


class Circle(Shapes):
	def __init__(self, radius=1.0, color="green", filled=True):
		super().__init__(color, filled)
		self.__radius = radius

	@property
	def radius(self):
		return self.__radius

	@radius.setter
	def radius(self, radius):
		self.__radius = radius

	@property
	def area(self):
		return pi * (self.radius ** 2)

	@property
	def perimeter(self):
		return 2 * pi * self.radius

	def __str__(self):
		return f"A circle with radius={self.radius}, which is a subclass of {super().__str__()}"
