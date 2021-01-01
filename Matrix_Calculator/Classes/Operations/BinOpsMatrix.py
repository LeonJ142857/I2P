import numpy as np
from scipy import linalg
from tkinter import END

# class to wrap binary matrix operations
# because it needs to give output to output_space, a text widget


class BinOpsMatrix:
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

	# get the cross product of first matrix with second matrix(order matters)
	# first matrix and second matrix are represented by entry_list_1 and entry_list_2 respectively
	def cross(self, entry_list_1, entry_list_2):
		# convert entry_list_1 and entry_list_2 to numpy array with list comprehension
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		# store the value of calculation in result
		result = np.cross(array_1, array_2)
		# clear output_space and insert result
		self.clear_insert(result)
		
	# get the dot product of first matrix with second matrix(order matters)
	def dot(self, entry_list_1, entry_list_2):
		# convert entry_list_1 and entry_list_2 to numpy array with list comprehension
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		# store the value of calculation in result
		result = np.dot(array_1, array_2)
		# clear output_space and insert result
		self.clear_insert(result)
		
	# get the inner product of first matrix with second matrix(order matters)
	def inner(self, entry_list_1, entry_list_2):
		# convert entry_list_1 and entry_list_2 to numpy array with list comprehension
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		# store the value of calculation in result
		result = np.inner(array_1, array_2)
		# clear output_space and insert result
		self.clear_insert(result)
	
	# get the matrix with elements the sum of each element in the same index(order doesn't matter)
	def matrix_add(self, entry_list_1, entry_list_2):
		# convert entry_list_1 and entry_list_2 to numpy array with list comprehension
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		# store the value of calculation in result
		result = np.add(array_1, array_2)
		# clear output_space and insert result
		self.clear_insert(result)
		
	# get the matrix resulted from multiplying the first matrix with second matrix(order matters)
	def matrix_multiplication(self, entry_list_1, entry_list_2):
		# convert entry_list_1 and entry_list_2 to numpy array with list comprehension
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		# store the value of calculation in result
		result = np.matmul(array_1, array_2)
		# clear output_space and insert result
		self.clear_insert(result)
		
	# get the outer product of first matrix with second matrix(order matters)
	def outer(self, entry_list_1, entry_list_2):
		# convert entry_list_1 and entry_list_2 to numpy array with list comprehension
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		# store the value of calculation in result
		result = np.outer(array_1, array_2)
		# clear output_space and insert result
		self.clear_insert(result)
		
	# get matrix that results from multiplying each element by a number(order doesn't matter)
	def scalar_multiplication(self, entry_list_1, entry_list_2):
		# convert entry_list_1 and entry_list_2 to numpy array with list comprehension
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		# store the value of calculation in result
		result = np.outer(array_1, array_2)
		# clear output_space and insert result
		self.clear_insert(result)
		
	# solve system of linear equation (order matters)
	def solve(self, entry_list_1, entry_list_2):
		# convert entry_list_1 and entry_list_2 to numpy array with list comprehension
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		# store the value of calculation in result
		result = linalg.solve(array_1, array_2)
		# clear output_space and insert result
		self.clear_insert(result)
		
	# get the matrix with elements the result of each element in the first matrix
	# subtracted with each element in the second matrix in the same index (order doesn't matter)
	def subtract(self, entry_list_1, entry_list_2):
		# convert entry_list_1 and entry_list_2 to numpy array with list comprehension
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		# store the value of calculation in result
		result = np.subtract(array_1, array_2)
		# clear output_space and insert result
		self.clear_insert(result)
