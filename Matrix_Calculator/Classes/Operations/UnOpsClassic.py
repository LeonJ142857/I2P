from root_window import io_space, Euler, PI
from tkinter import END
import math


class UnOpsClassic:
	# class to handle all classical calculator's unary operations
	def __init__(self, io_space):
		# initialize the object with io_space entry widget as attribute
		self.__io_space = io_space

	@property
	def io_space(self):
		return self.__io_space

	def clear(self):
		# shortcut for the built-in delete method of entry widget
		self.io_space.delete(0, END)

	def clear_insert(self, inputstring):
		# clear entry widget then insert value
		self.clear()
		io_space.insert(0, inputstring)

	def ins_val(self, number):
		# append a digit to entry widget
		curr = self.io_space.get()
		self.clear()
		special = curr == Euler or curr == PI
		io_space.insert(0, str(number) if special else curr + str(number))

	def comma(self):
		# insert comma ('.')
		curr = eval(io_space.get())
		if not isinstance(curr, float):
			self.clear_insert(str(curr) + '.')

	def plus_min(self):
		# give +/- sign
		curr = self.io_space.get()
		if len(curr) == 0:
			self.io_space.insert(0, '-')
		else:
			self.clear_insert(curr[1:len(curr)] if curr[0] == '-' else '-' + curr[:len(curr)])

	def backspace(self):
		# delete the last digit
		curr = self.io_space.get()
		self.clear_insert(curr[:len(curr)-1])

	def one_over_a(self):
		# 1 / a number
		curr = eval(self.io_space.get())
		self.clear_insert(str(1 / curr))

	def sqrt(self):
		# square root of a number
		curr = eval(self.io_space.get())
		self.clear_insert(str(curr ** 0.5))

	def square(self):
		# square of a number
		curr = eval(self.io_space.get())
		self.clear_insert(str(curr ** 2.0))

	def absolute(self):
		# absolute value of a number
		curr = eval(self.io_space.get())
		self.clear_insert(str(abs(curr)))

	def ten_pow_a(self):
		# 10 ^ a number
		curr = eval(self.io_space.get())
		self.clear_insert(str(10.0 ** curr))

	def factorial(self):
		# factorial of a number
		curr = eval(self.io_space.get())
		fact = str(math.gamma(curr + 1))
		self.clear_insert(fact)

	def log10(self):
		# logarithm base 10 of a number
		curr = eval(self.io_space.get())
		self.clear_insert(str(math.log10(curr)))

	def log_e(self):
		# logarithm base e, i.e. ln or logarithm natural
		curr = eval(self.io_space.get())
		self.clear_insert(str(math.log(curr)))


un_ops_classic = UnOpsClassic(io_space)
