from classic_buttons_positioning import *
from button_objects_classic import *
from matrix_unops_configurations import configure_unops
from button_objects_classic import button_objects_classic
from objects_matrix_unary import objects_matrix_unary, matrix_unary
from helper_functions import *

root_window.resizable(width=False, height=False)
root_window.protocol("WM_DELETE_WINDOW", lambda: on_closing_root(root_window))
root_window_width = 390
root_window_height = 415
root_init_x = 50
root_init_y = 50
root_window.geometry(f'{root_window_width}x{root_window_height}+{root_init_x}+{root_init_y}')
classic_buttons_positioning(button_objects_classic)
configure_unops(objects_matrix_unary, matrix_unary)
root_window.mainloop()


