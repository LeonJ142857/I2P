from input_username_password_balance import *
from deposit_withdraw_amount import *


def login(accounts):
	username = input("Please enter your name:")
	password = input("Please enter your password:")
	login_status = username in accounts.keys() and accounts[username].get_password() == password
	if login_status:
		print("login accepted")
		second_level_option(accounts, username)
	else:
		print("Wrong password or username, please check again.")
		login(accounts)


def first_level_option(accounts):
	print("Options:\n1. Add new account\n2. Login\n3. Quit")
	f_option = eval(input("Please choose an option by inputting the number:"))
	if f_option == 1:
		username = input_username(accounts)
		password = input_password(accounts)
		balance = input_balance(accounts, username)
		accounts[username] = Account(password, balance)
		from pickle import dump
		dump(accounts[username], open("account_data.pkl", "ab"))
		print(username, file=open("account_names.txt", "a"))
		first_level_option(accounts)
	elif f_option == 2:
		login(accounts)
	elif f_option == 3:
		print("Thank you for using our service! We hope we can see you again soon.")
		return
	else:
		print("command not recognized, please input a number in range 1-3.")
		first_level_option(accounts)


def second_level_option(accounts, username):
	print("Options:\n1. Deposit money\n2. Withdraw money\n3. Inquire Balance\n4. Quit")
	s_option = eval(input("Please choose an option by inputting the number:"))
	if s_option == 1:
		amt = deposit_amount()
		accounts[username].deposit(amt)
		print(f"${amt} have been successfully deposited. Thank you for using our service!")
		second_level_option(accounts, username)
	elif s_option == 2:
		amt = withdraw_amount(accounts, username)
		accounts[username].withdraw(amt)
		print(f"${amt} have been successfully withdrawn. Thank you for using our service!")
		second_level_option(accounts, username)
	elif s_option == 3:
		amt = accounts[username].get_balance()
		print(f"Available Balance: ${amt}.\nThank you for using our service.")
		second_level_option(accounts, username)
	if s_option == 4:
		first_level_option(accounts)
	else:
		print("command not recognized, please input a number in range 1-4.")
		second_level_option(accounts)
