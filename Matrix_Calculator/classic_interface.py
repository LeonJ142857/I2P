from classic_buttons_positioning import *
from button_objects_classic import *
from matrix_unops_configurations import configure_unops
from button_objects_classic import button_objects_classic
from objects_matrix_unary import objects_matrix_unary
from helper_functions import *

root_window.resizable(width=False, height=False)
root_window.protocol("WM_DELETE_WINDOW", lambda:on_closing_root(root_window))
classic_buttons_positioning(button_objects_classic)
configure_unops(grid_configure_weights, objects_matrix_unary)
root_window.mainloop()
