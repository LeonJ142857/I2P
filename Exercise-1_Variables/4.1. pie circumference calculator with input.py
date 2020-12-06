print("Hello, welcome to a simple program to calculate the circumference of a pie given its diameter")
pi = 3.14
pie_diameter = float(input("Please enter the diameter of the pie:"))
pie_radius = pie_diameter / 2
circumference = 2 * pi * pie_radius
circumference_msg = "Jimmy's pie has a circumference: "
print(circumference_msg, circumference)
