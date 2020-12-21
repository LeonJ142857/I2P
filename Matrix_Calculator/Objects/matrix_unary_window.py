from MatrixUnaryWindow import MatrixUnaryWindow
from root_window import root_window

title = "Classic Calculator > Matrix Unary Calculator"
background = "gray87"
width = 300 + 60 * 3
height = 43 + max(172, 57 * 3)
matrix_unary_window = MatrixUnaryWindow(root_window, bg=background)
matrix_unary_window.title(title)
matrix_unary_window.minsize(width, height)

