from person import *


class Teacher(Person):
	def __init__(self, name, address):
		super().__init__(name, address)
		self.__num_courses = 0
		self.__courses = []

	def add_course(self, course):
		if course not in self.__courses:
			self.__courses.append(course)
			return True
		return False

	def remove_course(self, course):
		if course in self.__courses:
			self.__courses.remove(course)
			return True
		return False

	@property
	def courses(self):
		return self.__courses

	def __str__(self):
		return f"Teacher: {super().__str__()}"
