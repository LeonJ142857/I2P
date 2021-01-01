import numpy as np
from scipy import linalg
from tkinter import END

# class to wrap unary matrix operations
# because it needs to give output to output_space, a text widget


class UnOpsMatrix:
	def __init__(self, output_space):
		self.__output_space = output_space

	# shortcut for easier access
	@property
	def output_space(self):
		return self.__output_space

	# shortcut for clearing output_space then inserting a string
	def clear_insert(self, result):
		self.output_space.delete('1.0', END)
		self.output_space.insert('1.0', result)

	# get the determinant of the matrix represented by the entry_list
	def determinant(self, entry_list):
		# convert entry_list to numpy array with list comprehension
		array = np.array([[eval(entry.get()) for entry in row]for row in entry_list])
		# store the value of calculation in result
		result = linalg.det(array)
		# clear output_space and insert result
		self.clear_insert(result)

	# get the eigen_value of the matrix
	def eigen_value(self, entry_list):
		# convert entry_list to numpy array with list comprehension
		array = np.array([[float(entry.get()) for entry in row]for row in entry_list])
		# store the value of calculation in result
		results = linalg.eigvals(array)
		string = ''
		# formatting the result to be more neat and easy to read
		for result, i in zip(results, range(len(results))):
			string += f'eigen value {i+1}: {result}\n'
		self.clear_insert(string)

	# gives inverse of a matrix, note: needs to be square matrix, even so, not all square matrices have inverses
	def inverse(self, entry_list):
		# convert entry_list to numpy array with list comprehension
		array = np.array([[eval(entry.get()) for entry in row]for row in entry_list])
		# check for errors, if error then insert error message to output space
		try:
			# store the value of calculation in result
			result = linalg.inv(array)
			string = ''
			# formatting the result to be more neat and easy to read
			for row in result:
				for num in row:
					string += str(num)+' '
				string += '\n'
			self.clear_insert(string)
		except np.linalg.LinAlgError:
			result = "The Inverse does not exist"
			self.clear_insert(result)

	# gives the basis column vectors of a null space of a matrix
	def null_space(self, entry_list):
		# convert entry_list to numpy array with list comprehension
		array = np.array([[eval(entry.get()) for entry in row]for row in entry_list])
		# store the value of calculation in result
		result = linalg.null_space(array)
		string = ''
		# formatting the result to be more neat and easy to read
		for row in result:
			for num in row:
				string += str(num)+' '
			string += '\n'
		self.clear_insert(string)

	# gives the length of a vector
	def norm(self, entry_list):
		# convert entry_list to numpy array with list comprehension
		array = np.array([[eval(entry.get()) for entry in row]for row in entry_list])
		# store the value of calculation in result
		result = linalg.norm(array)
		self.clear_insert(result)

	# gives the rank of a matrix
	def rank(self, entry_list):
		# convert entry_list to numpy array with list comprehension
		array = np.array([[eval(entry.get()) for entry in row]for row in entry_list])
		# store the value of calculation in result
		result = np.linalg.matrix_rank(array)
		self.clear_insert(result)

	# gives the trace of a matrix
	def trace(self, entry_list):
		# convert entry_list to numpy array with list comprehension
		array = np.array([[eval(entry.get()) for entry in row]for row in entry_list])
		# store the value of calculation in result
		result = np.trace(array)
		self.clear_insert(result)

	# gives the transpose of a matrix
	def transpose(self, entry_list):
		# convert entry_list to numpy array with list comprehension
		array = np.array([[eval(entry.get()) for entry in row]for row in entry_list])
		# store the value of calculation in result
		result = np.matrix.transpose(array)
		string = ''
		# formatting the result to be more neat and easy to read
		for row in result:
			for num in row:
				string += str(num)+' '
			string += '\n'
		self.clear_insert(string)
