from secrets import token_hex

class Account:
	minimum = 1000

	def __init__(self, username, password, balance):
		self.__username = username
		self.__password = password
		self.__account_number = token_hex(8)
		self.__balance = balance
		print(f"This is your account number: {self.__account_number}\nAccount has been set up successfully.")
		print("Never give the password to anybody you don't trust, we will never ask about your password.")

	def get_username(self):
		return self.__username

	def get_password(self):
		return self.__password

	def get_account_number(self):
		return self.__account_number

	def get_balance(self):
		return self.__balance

	def deposit(self, amt):
		self.__balance += amt

	def withdraw(self, amt):
		self.__balance -= amt
