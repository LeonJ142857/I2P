import numpy as np
from scipy import linalg
from tkinter import END


class BinOpsMatrix:
	def __init__(self, output_space):
		self.__output_space = output_space

	@property
	def output_space(self):
		return self.__output_space

	def clear_insert(self, result):
		self.output_space.delete('1.0', END)
		self.output_space.insert('1.0', result)

	def cross(self, entry_list_1, entry_list_2):
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		result = np.cross(array_1, array_2)
		self.clear_insert(result)
		
	def dot(self, entry_list_1, entry_list_2):
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		result = np.dot(array_1, array_2)
		self.clear_insert(result)
		
	def inner(self, entry_list_1, entry_list_2):
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		result = np.inner(array_1, array_2)
		self.clear_insert(result)
		
	def matrix_add(self, entry_list_1, entry_list_2):
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		result = np.add(array_1, array_2)
		self.clear_insert(result)
		
	def matrix_multiplication(self, entry_list_1, entry_list_2):
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		result = np.matmul(array_1, array_2)
		self.clear_insert(result)
		
	def outer(self, entry_list_1, entry_list_2):
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		result = np.outer(array_1, array_2)
		self.clear_insert(result)
		
	def scalar_multiplication(self, entry_list_1, entry_list_2):
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		result = np.outer(array_1, array_2)
		self.clear_insert(result)
		
	def solve(self, entry_list_1, entry_list_2):
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		result = linalg.solve(array_1, array_2)
		self.clear_insert(result)
		
	def subtract(self, entry_list_1, entry_list_2):
		array_1 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_1])
		array_2 = np.array([[eval(entry.get()) for entry in row]for row in entry_list_2])
		result = np.subtract(array_1, array_2)
		self.clear_insert(result)
