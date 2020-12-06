from account import Account
#####################
def input_bank_name(banks):
	print("List of currently supported banks:")
	for index, bank in zip(range(len(banks)), banks):
		print(bank, end=', ' if index < len(banks)-1 else '\n')
	name = input(f"Please enter the name of the bank: ")
	if name in banks:
		print("Bank is valid.")
		return name
	else:
		print("Bank is currently not supported or wrong name.\n")
		return input_bank_name(banks)

def check_real_name(f, l, customers):
	for customer in customers:
		if customer.get_first_name() == f and customer.get_last_name() == l:
			return True
	return False
#######################
def input_real_name(bank):
	f = input("Please enter your real first name:")
	l = input("Please enter your real last name:")
	customers = bank.get_customers()
	used = check_real_name(f, l, customers)
	if used:
		print("first name and last name pair is already in use. Please use another. Or login if this is you.")
		return input_real_name(bank)

	else:
		print("first name and last name is valid.")
		return f, l
###############################
def input_username(bank):
	usernames = [customer.get_account().get_username for customer in bank.get_customers()]
	username = input("Please enter your username:")
	if username not in usernames:
		print("Username is valid.")
		return username
	else:
		print("Username is already taken, please use another.")
		return input_username(bank)

############################
def input_password():
	from secrets import token_hex
	s_pass = token_hex(4)
	suggested = input(f"suggested password: '{s_pass}'\nGo with suggested?(Y/N)")
	if suggested == "Y":
		print(f"creating account with password '{s_pass}'\n")
		return s_pass
	elif suggested == "N":
		password = input("Please enter your password:")
		print(f"Your password '{password}' is valid.\n")
		return password
	else:
		print("Invalid answer.\n")
		return input_password()

######################
def input_balance():
	balance = eval(input(f"Please enter initial balance to deposit to this account (minimum amount is ${Account.minimum}):"))
	if isinstance(balance, (int, float)) and balance >= Account.minimum:
		return balance
	else:
		print("Invalid input\n")
		return input_balance()

