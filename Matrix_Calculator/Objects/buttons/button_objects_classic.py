from root_window import root_window
from un_ops_classic import *
from bin_ops_classic import bin_ops
from HoverButton import HoverButton
from matrix_unary_window import matrix_unary_window
# input number
b1 = HoverButton(root_window, text="1", padx=25, pady=15, command=lambda: ins_val(1), bg="white", activebackground='gray87')
b2 = HoverButton(root_window, text="2", padx=25, pady=15, command=lambda: ins_val(2), bg="white", activebackground='gray87')
b3 = HoverButton(root_window, text="3", padx=25, pady=15, command=lambda: ins_val(3), bg="white", activebackground='gray87')
b4 = HoverButton(root_window, text="4", padx=25, pady=15, command=lambda: ins_val(4), bg="white", activebackground='gray87')
b5 = HoverButton(root_window, text="5", padx=25, pady=15, command=lambda: ins_val(5), bg="white", activebackground='gray87')
b6 = HoverButton(root_window, text="6", padx=25, pady=15, command=lambda: ins_val(6), bg="white", activebackground='gray87')
b7 = HoverButton(root_window, text="7", padx=25, pady=15, command=lambda: ins_val(7), bg="white", activebackground='gray87')
b8 = HoverButton(root_window, text="8", padx=25, pady=15, command=lambda: ins_val(8), bg="white", activebackground='gray87')
b9 = HoverButton(root_window, text="9", padx=25, pady=15, command=lambda: ins_val(9), bg="white", activebackground='gray87')
b0 = HoverButton(root_window, text="0", padx=25, pady=15, command=lambda: ins_val(0), bg="white", activebackground='gray87')
e = HoverButton(root_window, text="e", padx=26, pady=15, command=lambda: clear_insert(Euler), bg="white", activebackground='gray87')
pi = HoverButton(root_window, text="pi", padx=23, pady=15, command=lambda: clear_insert(PI), bg="white", activebackground='gray87')

# other functionality
unary = HoverButton(root_window, text="M UnOps", padx=0, pady=15, command=matrix_unary_window.change_state, bg='tan1', activebackground='tan2')
binary = HoverButton(root_window, text="M BinOps", padx=0, pady=15, bg='tan1', activebackground='tan2')
CE = HoverButton(root_window, text="CE", padx=21, pady=15, command=clear, bg="ivory3", activebackground='cornsilk4')
backspace = HoverButton(root_window, text="X", padx=25, pady=15, command=backspace, bg="ivory3", activebackground='cornsilk4')

# basic operations
add = HoverButton(root_window, text="+", padx=25, pady=15, command=bin_ops.add, bg='light goldenrod yellow', activebackground='yellow3')
subtract = HoverButton(root_window, text="-", padx=27, pady=15, command=bin_ops.subtract, bg='light goldenrod yellow', activebackground='yellow3')
multiply = HoverButton(root_window, text="*", padx=27, pady=15, command=bin_ops.multiply, bg='light goldenrod yellow', activebackground='yellow3')
divide = HoverButton(root_window, text="/", padx=27, pady=15, command=bin_ops.divide, bg='light goldenrod yellow', activebackground='yellow3')
modulo = HoverButton(root_window, text="mod", padx=17, pady=15, command=bin_ops.modulo, bg='light goldenrod yellow', activebackground='yellow3')
equal = HoverButton(root_window, text="=", padx=25, pady=15, command=bin_ops.equal, bg="light blue", activebackground='dodger blue')

# advanced operations
abs = HoverButton(root_window, text="abs", padx=19, pady=15, command=absolute, activebackground='pale goldenrod')
a_pow_2 = HoverButton(root_window, text="a^2", padx=21, pady=15, command=square, activebackground='pale goldenrod')
a_pow_b = HoverButton(root_window, text="a^b", padx=20, pady=15, command=bin_ops.a_pow_b, activebackground='pale goldenrod')
comma = HoverButton(root_window, text=".", padx=27, pady=15, command=lambda: ins_val('.'), activebackground='gray87')
exp = HoverButton(root_window, text="exp", padx=19, pady=15, command=clear, activebackground='pale goldenrod') ################################
fact = HoverButton(root_window, text="n!", padx=23, pady=15, command=factorial, activebackground='pale goldenrod')
log = HoverButton(root_window, text="log", padx=22, pady=15, command=log10, activebackground='pale goldenrod')
ln = HoverButton(root_window, text="ln", padx=25, pady=15, command=log_e, activebackground='pale goldenrod')
one_over_a = HoverButton(root_window, text="1/a", padx=20, pady=15, command=one_over_a, activebackground='pale goldenrod')
plus_min = HoverButton(root_window, text="+/-", padx=19, pady=15, command=plus_min, activebackground='gray87')
sq_root = HoverButton(root_window, text="sqrt", padx=20, pady=15, command=sqrt, activebackground='pale goldenrod')
ten_pow_a = HoverButton(root_window, text="10^a", padx=17, pady=15, command=ten_pow_a, activebackground='pale goldenrod')


