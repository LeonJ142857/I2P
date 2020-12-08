from shapes import Shapes
from math import pi

class Circle(Shapes):
	__radius: float

	def __init__(self, radius=1.0, color="green", filled=True):
		super().__init__(color, filled)
		self.__radius = radius

	def get_radius(self):
		return self.__radius

	def set_radius(self, radius):
		self.__radius = radius

	def get_area(self):
		return pi * (self.get_radius() ** 2)

	def get_perimeter(self):
		return 2 * pi * self.get_radius()

	def to_string(self):
		return f"A circle with radius={self.get_radius()}, which is a subclass of {super().to_string()}"
