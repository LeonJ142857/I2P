from rectangle import Rectangle


class Square(Rectangle):
	def __init__(self, side=1.0, color="green", filled=True):
		super().__init__(side, side, color, filled)
		self.__side = side

	def get_side(self):
		return self.__side

	def set_side(self, side):
		self.__side = side

	def set_width(self, side):
		super().set_width(side)

	def set_length(self, side):
		super().set_length(side)

	def to_string(self):
		return f"A Square with side={self.get_side()}, which is a subclass of {super().to_string()}"
