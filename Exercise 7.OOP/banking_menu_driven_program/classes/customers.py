from account import *
class Customer:
	def __init__(self, f, l):
		self.__first_name = f
		self.__last_name = l

	def get_first_name(self):
		return self.__first_name

	def get_last_name(self):
		return self.__last_name

	def get_account(self):
		return self.__account

	def set_account(self, username, password, balance):
		self.__account = Account(username, password, balance)
