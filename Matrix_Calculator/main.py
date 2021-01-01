from classic_buttons_positioning import *
from button_objects_classic import *
from matrix_unops_configurations import configure_unops
from matrix_binops_configurations import configure_binops
from button_objects_classic import button_objects_classic
from objects_matrix_unary import objects_matrix_unary, matrix_unary
from objects_matrix_binary import objects_matrix_binary, matrix_binary_1, matrix_binary_2
from helper_functions import *

# set the root window to be unresizeable
root_window.resizable(width=False, height=False)
# set the close button at the top right of root window to create a popup asking "do you want to quit?"
root_window.protocol("WM_DELETE_WINDOW", lambda: on_closing_root(root_window))
root_window_width = 390
root_window_height = 415
root_init_x = 50
root_init_y = 50
# set the root window size and initial position
root_window.geometry(f'{root_window_width}x{root_window_height}+{root_init_x}+{root_init_y}')
# call function to position the buttons in root window correctly
classic_buttons_positioning(button_objects_classic)
# call function to configure the objects of matrix unary window
configure_unops(objects_matrix_unary, matrix_unary)
# call function to configure the objects of matrix binary window
configure_binops(objects_matrix_binary, matrix_binary_1, matrix_binary_2)
# mainloop to keep the root window and the child widgets to keep displaying as long as the user don't close the root window.
root_window.mainloop()


