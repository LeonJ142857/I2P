from banking_menu_driven_program.bank_menu import *
from pickle import load
from os.path import getsize
from bank import Bank
banks = {}
bank_names = open("bank_data/bank_names.txt")
for bank_name in bank_names:
	name = bank_name.strip()
	filesize = getsize(f"bank_data/{name}.pkl")
	bank_data = open(f"bank_data/{name}.pkl", "rb")
	banks[name] = load(bank_data) if filesize > 0 else Bank(name)
	bank_data.close()
bank_names.close()
print("Welcome to a simple program to add account, deposit money, withdraw money, and inquire about your balance.")
first_level_option(banks)

