class Person:
	def __init__(self, name, address):
		self.__name = name
		self.__address = address

	def get_name(self):
		return self.__name

	def get_address(self):
		return self.__address

	def set_address(self, address):
		self.__address = address

	def to_string(self):
		return f"{self.get_name()}({self.get_address()})"


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

	def get_average_grade(self):
		return sum(self.__courses_grade.values()) / self.__num_courses

	def to_string(self):
		return f"Student: {super().to_string()}"


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

	def to_string(self):
		return f"Teacher: {super().to_string()}"
