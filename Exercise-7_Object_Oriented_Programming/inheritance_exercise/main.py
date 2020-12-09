from classes.circle import *
from classes.square import *
from classes.rectangle import *

#objects initialization
shape1 = Shapes()
shape2 = Shapes("silver")
shape3 = Shapes("gold", False)
circle1 = Circle()
circle2 = Circle(2.5)
circle3 = Circle(2.9, "purple")
circle4 = Circle(3.9, "grey", False)
square1 = Square()
square2 = Square(3.5)
square3 = Square(3.7, "red")
square4 = Square(4.5, "yellow", True)
rectangle1 = Rectangle()
rectangle2 = Rectangle(4.7, 4.9)
rectangle3 = Rectangle(3.5, 5.7, "black")
rectangle4 = Rectangle(2.7, 9.3, "brown", False)

#testing for shapes
print("shape1 before:\n", shape1, '\n', shape1.color, shape1.filled, '\n')
shape1.color = "red"
shape1.filled = False
print("shape1 after:\n", shape1, '\n', shape1.color, shape1.filled, '\n')
print(shape2, '\n', shape2.color, shape2.filled, '\n')
print(shape3, '\n', shape3.color, shape3.filled, '\n\n')

#testing for circles
print("circle1 before:\n", circle1, '\n', circle1.radius, circle1.area,
	  circle1.perimeter, circle1.color, circle1.filled, '\n')
circle1.radius = 1.5
circle1.color = "silver"
circle1.filled = False
print("circle1 after:\n", circle1, '\n', circle1.radius, circle1.area,
	  circle1.perimeter, circle1.color, circle1.filled, '\n')
print(circle2, '\n', circle2.radius, circle2.area, circle2.perimeter, circle2.color, circle2.filled, '\n')
print(circle3, '\n', circle3.radius, circle3.area, circle3.perimeter, circle3.color, circle3.filled, '\n')
print(circle4, '\n', circle4.radius, circle4.area, circle4.perimeter, circle4.color, circle4.filled, '\n\n')

#testing for rectangles
print("rectangle1 before:\n", rectangle1, '\n', rectangle1.width, rectangle1.length,
	  rectangle1.area, rectangle1.perimeter, rectangle1.color, rectangle1.filled, '\n')
rectangle1.width = 3.2
rectangle1.length = 3.5
rectangle1.color = "black"
rectangle1.filled = False
print("rectangle1 after:\n", rectangle1, '\n', rectangle1.width, rectangle1.length,
	  rectangle1.area, rectangle1.perimeter, rectangle1.color, rectangle1.filled, '\n')
print(rectangle2, '\n', rectangle2.width, rectangle2.length, rectangle2.area,
	  rectangle2.perimeter, rectangle2.color, rectangle2.filled, '\n')
print(rectangle3, '\n', rectangle3.width, rectangle3.length, rectangle3.area,
	  rectangle3.perimeter, rectangle3.color, rectangle3.filled, '\n')
print(rectangle4, '\n', rectangle4.width, rectangle4.length, rectangle4.area,
	  rectangle4.perimeter, rectangle4.color, rectangle4.filled, '\n\n')

#testing for squares
print("square1 before:\n", square1, '\n', square1.side, square1.length, square1.width,
	  square1.area, square1.perimeter, square1.color, square1.filled, '\n')
square1.side = 2.5
square1.set_width(2.1)
square1.set_length(2.7)
square1.color = "grey"
square1.filled = False
print("square1 after:\n", square1, '\n', square1.side, square1.length, square1.width,
	  square1.area, square1.perimeter, square1.color, square1.filled, '\n')
print(square2, '\n', square2.side, square2.length, square2.width,
	  square2.area, square2.perimeter, square2.color, square2.filled, '\n')
print(square3, '\n', square3.side, square3.length, square3.width,
	  square3.area, square3.perimeter, square3.color, square3.filled, '\n')
print(square4, '\n', square4.side, square4.length, square4.width,
	  square4.area, square4.perimeter, square3.color, square3.filled, '\n')
