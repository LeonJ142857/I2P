from classic_buttons_positioning import *
from grid_configure_weight import *
from button_objects_classic import *
from matrix_unops_configurations import configure_unops
from button_objects_classic import button_objects_classic
from matrix_unary_window import matrix_unary_window
from objects_matrix_unary import objects_matrix_unary
root_window.minsize(350, 450)
grid_configures(root_window, 8, 5)
classic_buttons_positioning(button_objects_classic)
configure_unops(matrix_unary_window, matrix_unary_window.row_count,
				matrix_unary_window.column_count, objects_matrix_unary)
root_window.mainloop()
