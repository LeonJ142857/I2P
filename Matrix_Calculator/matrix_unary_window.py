from tkinter import *
m = 3
n = 3
x = 4
y = 5

# Top level settings
matrix_unary_window = Tk()
matrix_unary_window.title("Simple Calculator > Matrix Unary Calculator")
matrix_unary_window.minsize(300 + 60 * m, 43 + max(172, n * 57))
matrix_unary_window.configure(bg="gray87")
