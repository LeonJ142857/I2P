from base import io_space
from helper_functions.un_ops import clear

class BinOps():
    def _init_(self):
        self.__operation = ""
        self.f_num = 0
    def set_fnum_operation(self, num, string):
        self.f_num = num
        self.operation = string
    def add(self):
        self.set_fnum_operation(eval(io_space.get()), "addition")
        clear()
    def subtract(self):
        self.set_fnum_operation(eval(io_space.get()), "subtraction")
        clear()
    def multiply(self):
        self.set_fnum_operation(eval(io_space.get()), "multiplication")
        clear()
    def divide(self):
        self.set_fnum_operation(eval(io_space.get()), "division")
        clear()
    def modulo(self):
        self.set_fnum_operation(eval(io_space.get()), "modulo")
        clear()
    def a_pow_b(self):
        self.set_fnum_operation(eval(io_space.get()), "exponentiation")
        clear()
    def equal(self):
        s_num = eval(io_space.get())
        clear()
        if self.operation == "addition":
            io_space.insert(0, str(self.f_num + s_num))
        if self.operation == "subtraction":
            io_space.insert(0, str(self.f_num - s_num))
        if self.operation == "multiplication":
            io_space.insert(0, str(self.f_num * s_num))
        if self.operation == "division":
            io_space.insert(0, str(self.f_num / s_num))
        if self.operation == "modulo":
            io_space.insert(0, str(self.f_num % s_num))
        if self.operation == "exponentiation":
            io_space.insert(0, str(self.f_num ** s_num))

bin_ops = BinOps()
