from classic_buttons_positioning import *
from grid_configure_weight import *
from button_objects_classic import *

root_window.minsize(350, 450)
grid_configures(root_window, 8, 5)
classic_buttons_positioning(b1, b2, b3, b4, b5, b6, b7, b8, b9, b0, pi, e, unary, binary, CE, backspace,
								add, subtract, multiply, divide, modulo, equal, abs, a_pow_2,  a_pow_b,
								comma, exp, fact, log, ln, one_over_a, plus_min, sq_root, ten_pow_a)
root_window.mainloop()