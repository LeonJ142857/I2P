from root_window import io_space
from UnOpsClassic import un_ops_classic


class BinOpsClassic():
    def __init__(self, io_space):
        self.__operation = ""
        self.__f_num = 0
        self.__io_space = io_space

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, operation):
        self.__operation = operation

    @property
    def f_num(self):
        return self.__f_num

    @f_num.setter
    def f_num(self, f_num):
        self.__f_num = f_num

    @property
    def io_space(self):
        return self.__io_space

    def set_fnum_operation(self, num, string):
        self.f_num = num
        self.operation = string

    def add(self):
        self.set_fnum_operation(eval(self.io_space.get()), "addition")
        un_ops_classic.clear()

    def subtract(self):
        self.set_fnum_operation(eval(self.io_space.get()), "subtraction")
        un_ops_classic.clear()

    def multiply(self):
        self.set_fnum_operation(eval(self.io_space.get()), "multiplication")
        un_ops_classic.clear()

    def divide(self):
        self.set_fnum_operation(eval(self.io_space.get()), "division")
        un_ops_classic.clear()

    def modulo(self):
        self.set_fnum_operation(eval(self.io_space.get()), "modulo")
        un_ops_classic.clear()

    def a_pow_b(self):
        self.set_fnum_operation(eval(self.io_space.get()), "exponentiation")
        un_ops_classic.clear()

    def equal(self):
        s_num = eval(self.io_space.get())
        un_ops_classic.clear()
        if self.operation == "addition":
            self.io_space.insert(0, str((self.f_num + s_num)**1.0))
        elif self.operation == "subtraction":
            self.io_space.insert(0, str((self.f_num - s_num)**1.0))
        elif self.operation == "multiplication":
            self.io_space.insert(0, str((self.f_num * s_num)**1.0))
        elif self.operation == "division":
            self.io_space.insert(0, str((self.f_num / s_num)**1.0))
        elif self.operation == "modulo":
            self.io_space.insert(0, str((self.f_num % s_num)**1.0))
        elif self.operation == "exponentiation":
            self.io_space.insert(0, str((self.f_num ** s_num)**1.0))


bin_ops_classic = BinOpsClassic(io_space)
