from account import Account
def input_username(accounts):
	username = input("Please enter your username:")
	if username not in list(accounts.keys()):
		print("Username is valid.")
		return username
	else:
		print("Username is already taken, please use another.")
		return input_username(accounts)

def input_password(accounts):
	from secrets import token_hex
	s_pass = token_hex(8)
	suggested = input(f"suggested password: {s_pass}\nGo with suggested?(Y/N)")
	if suggested == "Y":
		print(f"creating account with password '{s_pass}'")
		return s_pass
	elif suggested == "N":
		password = input("Please enter your password:")
		if password in [accounts[acc].get_password() for acc in accounts]:
			print("Password is already taken, please use another.")
			return input_password(accounts)
		else:
			print(f"Your password '{password}' is valid.")
			return password
	else:
		print("Invalid answer.")
		return input_password(accounts)


def input_balance(accounts, username):
	balance = eval(input(f"Please enter initial balance to deposit to this account (minimum amount is ${Account.minimum}):"))
	if isinstance(balance, (int, float)) and balance >= Account.minimum:
		return balance
	else:
		print("Balance Invalid")
		return input_balance(accounts, username)
