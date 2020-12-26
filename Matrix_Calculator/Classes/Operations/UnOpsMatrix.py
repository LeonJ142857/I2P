import numpy as np
from scipy import linalg
from tkinter import INSERT, END, Text


class UnOpsMatrix:
	def __init__(self, output_space):
		self.__output_space = output_space

	@property
	def output_space(self):
		return self.__output_space

	def clear_insert(self, result):
		self.output_space.delete('1.0', END)
		self.output_space.insert('1.0', result)

	def determinant(self, entry_list):
		array = np.array([[eval(entry.get()) for entry in row]for row in entry_list])
		result = linalg.det(array)
		self.clear_insert(result)

	def eigen_value(self, entry_list):
		array = np.array([[float(entry.get()) for entry in row]for row in entry_list])
		results = linalg.eigvals(array)
		string = ''
		for result, i in zip(results, range(len(results))):
			string += f'eigen value {i+1}: {result}\n'
		print(string)
		self.clear_insert(string)

	# needs to be square matrix
	def inverse(self, entry_list):
		array = np.array([[eval(entry.get()) for entry in row]for row in entry_list])
		try:
			result = linalg.inv(array)
			string = ''
			for row in result:
				for num in row:
					string += str(num)+' '
				string += '\n'
			self.clear_insert(string)
		except np.linalg.LinAlgError:
			result = "The Inverse does not exist"
			self.clear_insert(result)

	def null_space(self, entry_list):
		array = np.array([[eval(entry.get()) for entry in row]for row in entry_list])
		result = linalg.null_space(array)
		string = ''
		for row in result:
			for num in row:
				string += str(num)+' '
			string += '\n'
		self.clear_insert(string)

	def rank(self, entry_list):
		array = np.array([[eval(entry.get()) for entry in row]for row in entry_list])
		result = np.linalg.matrix_rank(array)
		self.clear_insert(result)

	def trace(self, entry_list):
		array = np.array([[eval(entry.get()) for entry in row]for row in entry_list])
		result = np.trace(array)
		self.clear_insert(result)

	def transpose(self, entry_list):
		array = np.array([[eval(entry.get()) for entry in row]for row in entry_list])
		result = np.matrix.transpose(array)
		string = ''
		for row in result:
			for num in row:
				string += str(num)+' '
			string += '\n'
		self.clear_insert(string)
