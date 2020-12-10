from person import *


class Student(Person):
	def __init__(self, name, address):
		super().__init__(name, address)
		self.__num_courses = 0
		self.__courses_grade = {}

	def add_course_grade(self, course, grade):
		self.__courses_grade[course] = grade
		self.__num_courses = len(self.__courses_grade)

	def print_grades(self):
		for course in self.__courses_grade:
			print(f"{course}: {self.__courses_grade[course]}")

	@property
	def average_grade(self):
		return sum(self.__courses_grade.values()) / self.__num_courses

	def __str__(self):
		return f"Student: {super().__str__()}"
