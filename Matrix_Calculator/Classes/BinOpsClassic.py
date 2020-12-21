from root_window import io_space
from UnOpsClassic import un_ops_classic


class BinOpsClassic():
	# class to handle all classical calculator's binary operations
	def __init__(self, io_space):
		# initialize the object with io_space entry widget,
		# first number in the binary operation,
		# and the operation type as attribute
		self.__operation = ""
		self.__f_num = 0
		self.__io_space = io_space

	@property
	def operation(self):
		return self.__operation

	@operation.setter
	def operation(self, operation):
		# shortcut for setting the operation
		self.__operation = operation

	@property
	def f_num(self):
		return self.__f_num

	@f_num.setter
	def f_num(self, f_num):
		# shortcut for setting the first number
		self.__f_num = f_num

	@property
	def io_space(self):
		return self.__io_space

	def set_fnum_operation(self, num, string):
		# shortcut for setting the first number and the operation
		self.f_num = num
		self.operation = string

	def add(self):
		# set the first number and operation to value of io_space and 'addition' respectively,
		# then clear io_space (F_NUM addition)
		self.set_fnum_operation(eval(self.io_space.get()), "addition")
		un_ops_classic.clear()

	def subtract(self):
		# F_NUM subtraction
		self.set_fnum_operation(eval(self.io_space.get()), "subtraction")
		un_ops_classic.clear()

	def multiply(self):
		# F_NUM multiplication
		self.set_fnum_operation(eval(self.io_space.get()), "multiplication")
		un_ops_classic.clear()

	def divide(self):
		# F_NUM division
		self.set_fnum_operation(eval(self.io_space.get()), "division")
		un_ops_classic.clear()

	def modulo(self):
		# F_NUM modulo
		self.set_fnum_operation(eval(self.io_space.get()), "modulo")
		un_ops_classic.clear()

	def a_pow_b(self):
		# F_NUM exponentiation
		self.set_fnum_operation(eval(self.io_space.get()), "exponentiation")
		un_ops_classic.clear()

	def equal(self):
		# insert value to io_space depending on the operation applied
		s_num = eval(self.io_space.get())
		un_ops_classic.clear()
		if self.operation == "addition":
			self.io_space.insert(0, str((self.f_num + s_num) ** 1.0))
		elif self.operation == "subtraction":
			self.io_space.insert(0, str((self.f_num - s_num) ** 1.0))
		elif self.operation == "multiplication":
			self.io_space.insert(0, str((self.f_num * s_num) ** 1.0))
		elif self.operation == "division":
			self.io_space.insert(0, str((self.f_num / s_num) ** 1.0))
		elif self.operation == "modulo":
			self.io_space.insert(0, str((self.f_num % s_num) ** 1.0))
		elif self.operation == "exponentiation":
			self.io_space.insert(0, str((self.f_num ** s_num) ** 1.0))


bin_ops_classic = BinOpsClassic(io_space)
