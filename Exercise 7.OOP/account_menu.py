from options import *
from pickle import load

accounts = {}
usernames_in = open("account_names.txt")
input_file = open("account_data.pkl", "rb")
for user_name in usernames_in:
	accounts[user_name.strip()] = load(input_file)
usernames_in.close()
input_file.close()
print("Welcome to a simple program to add account, deposit money, withdraw money, and inquire about your balance.")
first_level_option(accounts)

