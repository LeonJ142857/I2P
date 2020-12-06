from banking_menu_driven_program.helper_functions.input_functions import *
from banking_menu_driven_program.helper_functions.deposit_withdraw_amount import *

def login_status(accounts, username, password):
	for account in accounts:
		if account.get_username() == username and account.get_password() == password:
			return account, True
	return None, False

def login(banks):
	bank_name = input_bank_name(banks)
	username = input("Please enter your username:")
	password = input("Please enter your password:")
	accounts = [customer.get_account() for customer in banks[bank_name].get_customers()]
	account, status = login_status(accounts, username, password)
	if status:
		print("login successful.\n")
		second_level_option(account, banks)
	else:
		print("Wrong password or username, please check again.")
		login(banks)

def add_new_account(banks):
	bank_name = input_bank_name(banks)
	first_name, last_name = input_real_name(banks[bank_name])
	username = input_username(banks[bank_name])
	password = input_password()
	balance = input_balance()
	customer = banks[bank_name].add_customer(first_name, last_name)
	customer.set_account(username, password, balance)
	from pickle import dump, HIGHEST_PROTOCOL
	dump(banks[bank_name], open(f"bank_data/{bank_name}.pkl", "wb"), HIGHEST_PROTOCOL)
	first_level_option(banks)

def first_level_option(banks):
	print("Options:\n1. Add new account\n2. Login\n3. Quit\n")
	f_option = eval(input("Please choose an option by inputting the number:"))
	if f_option == 1:
		add_new_account(banks)
	elif f_option == 2:
		login(banks)
	elif f_option == 3:
		print("Thank you for using our service! We hope we can see you again soon.")
		from sys import exit
		exit()
	else:
		print("command not recognized, please input a number in range 1-3.")
		first_level_option(banks)


def second_level_option(account, banks):
	print("Options:\n1. Deposit money\n2. Withdraw money\n3. Inquire Balance\n4. Quit\n")
	s_option = eval(input("Please choose an option by inputting the number:"))
	if s_option == 1:
		amt = deposit_amount()
		account.deposit(amt)
		print(f"${amt} have been successfully deposited. Thank you for using our service!")
		second_level_option(account, banks)
	elif s_option == 2:
		amt = withdraw_amount(account)
		account.withdraw(amt)
		print(f"${amt} have been successfully withdrawn. Thank you for using our service!")
		second_level_option(account, banks)
	elif s_option == 3:
		amt = account.get_balance()
		print(f"Available Balance: ${amt}.\nThank you for using our service.")
		second_level_option(account, banks)
	if s_option == 4:
		first_level_option(banks)
	else:
		print("command not recognized, please input a number in range 1-4.")
		second_level_option(account, banks)
