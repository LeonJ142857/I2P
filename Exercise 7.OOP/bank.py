from customers import Customer
class Bank:
	__number_of_customers: int
	__customers: []

	def _init__(self, b_name):
		self.__bank_name = b_name

	def add_customer(self, f, l):
		self.__customers.append(Customer(f, l))
		self.__number_of_customers += 1

	def get_num_of_customers(self):
		return self.__number_of_customers

	def get_customer(self, index):
		return self.__customers[index]
