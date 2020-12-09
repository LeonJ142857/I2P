from rectangle import Rectangle


class Square(Rectangle):
	def __init__(self, side=1.0, color="green", filled=True):
		super().__init__(side, side, color, filled)

	@property
	def side(self):
		return super().length

	@side.setter
	def side(self, side):
		super().set_width(side)
		super().set_length(side)

	def set_width(self, side):
		super().set_width(side)
		super().set_length(side)

	def set_length(self, side):
		super().set_width(side)
		super().set_length(side)

	def __str__(self):
		return f"A Square with side={self.side}, which is a subclass of {super().__str__()}"
