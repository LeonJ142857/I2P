from customers import Customer
class Bank():
	def __init__(self, b_name):
		self.__bank_name = b_name
		self.__number_of_customers = 0
		self.__customers = []

	def add_customer(self, f, l):
		self.__customers.append(Customer(f, l))
		self.__number_of_customers += 1
		return self.__customers[len(self.__customers)-1]

	def get_bank_name(self):
		return self.__bank_name
	def get_num_of_customers(self):
		return self.__number_of_customers

	def get_customer(self, index):
		return self.__customers[index]

	def get_customers(self):
		return self.__customers
