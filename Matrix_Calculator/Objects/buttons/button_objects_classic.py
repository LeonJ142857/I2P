from base import root
from helper_functions.un_ops import *
from bin_ops import bin_ops
from HoverButton import HoverButton

b1 = HoverButton(root, text="1", padx=25, pady=15, command=lambda: ins_val(1), bg="white", activebackground='gray87')
b2 = HoverButton(root, text="2", padx=25, pady=15, command=lambda: ins_val(2), bg="white", activebackground='gray87')
b3 = HoverButton(root, text="3", padx=25, pady=15, command=lambda: ins_val(3), bg="white", activebackground='gray87')
b4 = HoverButton(root, text="4", padx=25, pady=15, command=lambda: ins_val(4), bg="white", activebackground='gray87')
b5 = HoverButton(root, text="5", padx=25, pady=15, command=lambda: ins_val(5), bg="white", activebackground='gray87')
b6 = HoverButton(root, text="6", padx=25, pady=15, command=lambda: ins_val(6), bg="white", activebackground='gray87')
b7 = HoverButton(root, text="7", padx=25, pady=15, command=lambda: ins_val(7), bg="white", activebackground='gray87')
b8 = HoverButton(root, text="8", padx=25, pady=15, command=lambda: ins_val(8), bg="white", activebackground='gray87')
b9 = HoverButton(root, text="9", padx=25, pady=15, command=lambda: ins_val(9), bg="white", activebackground='gray87')
b0 = HoverButton(root, text="0", padx=25, pady=15, command=lambda: ins_val(0), bg="white", activebackground='gray87')
e = HoverButton(root, text="e", padx=26, pady=15, command=lambda: clear_insert(Euler), bg="white", activebackground='gray87')
pi = HoverButton(root, text="pi", padx=23, pady=15, command=lambda: clear_insert(PI), bg="white", activebackground='gray87')



###
unary = HoverButton(root, text="M UnOps", padx=0, pady=15, bg='tan1', activebackground='tan2')
binary = HoverButton(root, text="M BinOps", padx=0, pady=15, bg='tan1', activebackground='tan2')
CE = HoverButton(root, text="CE", padx=21, pady=15, command=clear, bg="ivory3", activebackground='cornsilk4')
backspace = HoverButton(root, text="X", padx=25, pady=15, command=backspace, bg="ivory3", activebackground='cornsilk4')

add = HoverButton(root, text="+", padx=25, pady=15, command=bin_ops.add, bg='light goldenrod yellow', activebackground='yellow3')
subtract = HoverButton(root, text="-", padx=27, pady=15, command=bin_ops.subtract, bg='light goldenrod yellow', activebackground='yellow3')
multiply = HoverButton(root, text="*", padx=27, pady=15, command=bin_ops.multiply, bg='light goldenrod yellow', activebackground='yellow3')
divide = HoverButton(root, text="/", padx=27, pady=15, command=bin_ops.divide, bg='light goldenrod yellow', activebackground='yellow3')
modulo = HoverButton(root, text="mod", padx=17, pady=15, command=bin_ops.modulo, bg='light goldenrod yellow', activebackground='yellow3')
equal = HoverButton(root, text="=", padx=25, pady=15, command=bin_ops.equal, bg="light blue", activebackground='dodger blue')
###

abs = HoverButton(root, text="abs", padx=19, pady=15, command=absolute, activebackground='pale goldenrod')
a_pow_2 = HoverButton(root, text="a^2", padx=21, pady=15, command=square, activebackground='pale goldenrod')
a_pow_b = HoverButton(root, text="a^b", padx=20, pady=15, command=bin_ops.a_pow_b, activebackground='pale goldenrod')
comma = HoverButton(root, text=".", padx=27, pady=15, command=lambda: ins_val('.'), activebackground='gray87')
exp = HoverButton(root, text="exp", padx=19, pady=15, command=clear, activebackground='pale goldenrod') ################################
fact = HoverButton(root, text="n!", padx=23, pady=15, command=factorial, activebackground='pale goldenrod')
log = HoverButton(root, text="log", padx=22, pady=15, command=log10, activebackground='pale goldenrod')
ln = HoverButton(root, text="ln", padx=25, pady=15, command=log_e, activebackground='pale goldenrod')
one_over_a = HoverButton(root, text="1/a", padx=20, pady=15, command=one_over_a, activebackground='pale goldenrod')
plus_min = HoverButton(root, text="+/-", padx=19, pady=15, command=plus_min, activebackground='gray87')
sq_root = HoverButton(root, text="sqrt", padx=20, pady=15, command=sqrt, activebackground='pale goldenrod')
ten_pow_a = HoverButton(root, text="10^a", padx=17, pady=15, command=ten_pow_a, activebackground='pale goldenrod')


