from root_window import io_space, Euler, PI
from tkinter import END
from numpy import math


def clear():
    io_space.delete(0, END)

def clear_insert(inputstring):
    clear()
    io_space.insert(0, inputstring)

def ins_val(number):
    curr = io_space.get()
    clear()
    special = curr == Euler or curr == PI
    io_space.insert(0, str(number) if special else curr + str(number))

def plus_min():
    curr = io_space.get()
    if len(curr) == 0:
        io_space.insert(0, '-')
    else:
        clear_insert(curr[1:len(curr)] if curr[0] == '-' else '-' + curr[:len(curr)])

def backspace():
    curr = io_space.get()
    clear_insert(curr[:len(curr)-1])

def one_over_a():
    curr = eval(io_space.get())
    clear_insert(str(1 / curr))
def sqrt():
    curr = eval(io_space.get())
    clear_insert(str(curr ** 0.5))
def square():
    curr = eval(io_space.get())
    clear_insert(str(curr ** 2))

def absolute():
    curr = eval(io_space.get())
    clear_insert(str(abs(curr)))

def ten_pow_a():
    curr = eval(io_space.get())
    clear_insert(str(10 ** curr))

def factorial():
    curr = eval(io_space.get())
    fact1 = str(math.factorial(curr))
    fact2 = str(((2 * float(PI) * curr) ** 0.5) * (curr / float(Euler)) ** curr)
    clear_insert(fact1 if type(curr) == int else fact2)

def log10():
    curr = eval(io_space.get())
    clear_insert(str(math.log10(curr)))

def log_e():
    curr = eval(io_space.get())
    clear_insert(str(math.log(curr)))

