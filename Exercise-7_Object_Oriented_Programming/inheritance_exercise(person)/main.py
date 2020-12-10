from classes.student import *
from classes.teacher import *


if __name__ == "__main__":
	person = Person("Leon", "Semarang")
	print(person)
	person.address = "Jakarta"
	print(person)
	student = Student("Alex", "America")
	student.add_course_grade("Math", 100)
	student.add_course_grade("Physics", 80)
	print(student)
	student.print_grades()
	print(student.average_grade)
	student.address = "Japan"
	print(student)
	teacher = Teacher("Koro-sensei", "Japan")
	teacher.add_course("Math")
	teacher.add_course("Programming")
	print(teacher, '\n', teacher.courses)
	teacher.address = "Antarctica"
	teacher.remove_course("Math")
	print(teacher, '\n', teacher.courses)

