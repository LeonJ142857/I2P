from root_window import io_space, Euler, PI
from tkinter import END
from numpy import math


class UnOpsClassic():
    def __init__(self, io_space):
        self.__io_space = io_space

    @property
    def io_space(self):
        return self.__io_space

    def clear(self):
        self.io_space.delete(0, END)

    def clear_insert(self, inputstring):
        self.clear()
        io_space.insert(0, inputstring)

    def ins_val(self, number):
        curr = self.io_space.get()
        self.clear()
        special = curr == Euler or curr == PI
        io_space.insert(0, str(number) if special else curr + str(number))

    def plus_min(self):
        curr = self.io_space.get()
        if len(curr) == 0:
            self.io_space.insert(0, '-')
        else:
            self.clear_insert(curr[1:len(curr)] if curr[0] == '-' else '-' + curr[:len(curr)])

    def backspace(self):
        curr = self.io_space.get()
        self.clear_insert(curr[:len(curr)-1])

    def one_over_a(self):
        curr = eval(self.io_space.get())
        self.clear_insert(str(1 / curr))

    def sqrt(self):
        curr = eval(self.io_space.get())
        self.clear_insert(str(curr ** 0.5))

    def square(self):
        curr = eval(self.io_space.get())
        self.clear_insert(str(curr ** 2))

    def absolute(self):
        curr = eval(self.io_space.get())
        self.clear_insert(str(abs(curr)))

    def ten_pow_a(self):
        curr = eval(self.io_space.get())
        self.clear_insert(str(10 ** curr))

    def factorial(self):
        curr = eval(self.io_space.get())
        fact1 = str(math.factorial(curr))
        fact2 = str(((2 * float(PI) * curr) ** 0.5) * (curr / float(Euler)) ** curr)
        self.clear_insert(fact1 if type(curr) == int else fact2)

    def log10(self):
        curr = eval(self.io_space.get())
        self.clear_insert(str(math.log10(curr)))

    def log_e(self):
        curr = eval(self.io_space.get())
        self.clear_insert(str(math.log(curr)))


un_ops_classic = UnOpsClassic(io_space)
