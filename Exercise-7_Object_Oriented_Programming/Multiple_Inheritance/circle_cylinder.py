import math

class Circle:
	def __init__(self, radius: float = 1.0, color: str = "red"):
		self.__radius: float = radius
		self.__color: str = color

	def get_radius(self):
		return self.__radius

	def get_color(self):
		return self.__color

	def set_radius(self, radius):
		self.__radius = radius

	def set_color(self, color):
		self.__color = color

	def get_area(self):
		return math.pi * self.get_radius() ** 2

	def to_string(self):
		return f"radius:{self.get_radius()}, color:{self.get_color()}"


class Cylinder(Circle):
	def __init__(self, height=1.0, rad: float = 1.0, col: str = "red"):
		super().__init__(rad, col)
		self.__height = height

	def get_height(self):
		return self.__height

	def set_height(self, height):
		self.__height = height

	def get_volume(self):
		return super().get_area() * self.get_height()

	def to_string(self):
		return f"height:{self.__height}, {super().to_string()}"
