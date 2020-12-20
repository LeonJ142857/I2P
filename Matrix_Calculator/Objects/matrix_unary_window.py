from MatrixWindow import MatrixWindow
from root_window import root_window
from matrix_unops_configurations import configure_unops
title = "Classic Calculator > Matrix Unary Calculator"
background = "gray87"
matrix_unary_window = MatrixWindow(root_window, title, background, configure_unops)
