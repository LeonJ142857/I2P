from base import root
from helper_functions.un_ops import *
from Classes.bin_ops import bin_ops
from button_objects.button_objects_matrix import button_list_matrix
from Classes.HoverButton import HoverButton

button_1 = HoverButton(root, text="1", padx=25, pady=15, command=lambda: ins_val(1), bg="white", activebackground='gray87')
button_2 = HoverButton(root, text="2", padx=25, pady=15, command=lambda: ins_val(2), bg="white", activebackground='gray87')
button_3 = HoverButton(root, text="3", padx=25, pady=15, command=lambda: ins_val(3), bg="white", activebackground='gray87')
button_4 = HoverButton(root, text="4", padx=25, pady=15, command=lambda: ins_val(4), bg="white", activebackground='gray87')
button_5 = HoverButton(root, text="5", padx=25, pady=15, command=lambda: ins_val(5), bg="white", activebackground='gray87')
button_6 = HoverButton(root, text="6", padx=25, pady=15, command=lambda: ins_val(6), bg="white", activebackground='gray87')
button_7 = HoverButton(root, text="7", padx=25, pady=15, command=lambda: ins_val(7), bg="white", activebackground='gray87')
button_8 = HoverButton(root, text="8", padx=25, pady=15, command=lambda: ins_val(8), bg="white", activebackground='gray87')
button_9 = HoverButton(root, text="9", padx=25, pady=15, command=lambda: ins_val(9), bg="white", activebackground='gray87')
button_0 = HoverButton(root, text="0", padx=25, pady=15, command=lambda: ins_val(0), bg="white", activebackground='gray87')
button_comma = HoverButton(root, text=".", padx=27, pady=15, command=lambda: ins_val('.'), activebackground='gray87')
button_plus_min = HoverButton(root, text="+/-", padx=19, pady=15, command=plus_min, activebackground='gray87')


###
button_clear_entry = HoverButton(root, text="CE", padx=21, pady=15, command=clear, bg="ivory3", activebackground='cornsilk4')
button_backspace = HoverButton(root, text="X", padx=25, pady=15, command=backspace, bg="ivory3", activebackground='cornsilk4')
button_add = HoverButton(root, text="+", padx=25, pady=15, command=bin_ops.add, bg='light goldenrod yellow', activebackground='yellow3')
button_subtract = HoverButton(root, text="-", padx=27, pady=15, command=bin_ops.subtract, bg='light goldenrod yellow', activebackground='yellow3')
button_multiply = HoverButton(root, text="*", padx=27, pady=15, command=bin_ops.multiply, bg='light goldenrod yellow', activebackground='yellow3')
button_divide = HoverButton(root, text="/", padx=27, pady=15, command=bin_ops.divide, bg='light goldenrod yellow', activebackground='yellow3')
button_modulo = HoverButton(root, text="mod", padx=17, pady=15, command=bin_ops.modulo, bg='light goldenrod yellow', activebackground='yellow3')
button_equal = HoverButton(root, text="=", padx=25, pady=15, command=bin_ops.equal, bg="light blue", activebackground='dodger blue')
###

button_apowb = HoverButton(root, text="a^b", padx=20, pady=15, command=bin_ops.a_pow_b, activebackground='pale goldenrod')
button_10powa = HoverButton(root, text="10^a", padx=17, pady=15, command=ten_pow_a, activebackground='pale goldenrod')
button_log = HoverButton(root, text="log", padx=22, pady=15, command=log10, activebackground='pale goldenrod')
button_ln = HoverButton(root, text="ln", padx=25, pady=15, command=log_e, activebackground='pale goldenrod')
button_root = HoverButton(root, text="sqrt", padx=20, pady=15, command=sqrt, activebackground='pale goldenrod')
button_factorial = HoverButton(root, text="n!", padx=23, pady=15, command=factorial, activebackground='pale goldenrod')
button_exp = HoverButton(root, text="exp", padx=19, pady=15, command=clear, activebackground='pale goldenrod') ################################
button_abs = HoverButton(root, text="abs", padx=19, pady=15, command=absolute, activebackground='pale goldenrod')
button_e = HoverButton(root, text="e", padx=26, pady=15, command=lambda: clear_insert(Euler), bg="white", activebackground='gray87')
button_pi = HoverButton(root, text="pi", padx=23, pady=15, command=lambda: clear_insert(PI), bg="white", activebackground='gray87')
button_apow2 = HoverButton(root, text="a^2", padx=21, pady=15, command=square, activebackground='pale goldenrod')
button_1_a = HoverButton(root, text="1/a", padx=20, pady=15, command=one_over_a, activebackground='pale goldenrod')

button_matrix = HoverButton(root, text="Matrix", padx=10, pady=15, command=lambda: forget_classic(button_list_classic), bg='tan1', activebackground='tan2')

button_list_classic = [button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8,
		button_9, button_pi, button_e, button_matrix, button_clear_entry, button_backspace, button_add,
		button_subtract, button_multiply, button_divide, button_modulo, button_equal, button_apow2,
		button_abs, button_exp, button_factorial, button_root, button_apowb, button_10powa, button_log,
		button_ln, button_1_a, button_plus_min, button_comma]
