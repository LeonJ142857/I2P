def deposit_amount():
	amt = eval(input("How much money do you want to deposit into this account ?"))
	if isinstance(amt, (int, float)) and amt > 0:
		return amt
	else:
		print("Invalid amount. Please try again.")
		return deposit_amount()

def withdraw_amount(accounts, username):
	amt = eval(input("How much money do you want to withdraw from this account ?"))
	if isinstance(amt, (int, float)) and 0 < amt <= accounts[username].get_balance():
		return amt
	else:
		print("Invalid amount. Please try again.")
		return withdraw_amount(accounts, username)
