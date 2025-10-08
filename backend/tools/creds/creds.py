#*************************************************
#	Module:		backend.tools.creds.creds (PocketA)	*
#	Author:		Scavenger4208					*
#	Version:	0,0,1							*
#*************************************************

#=== Imports

import string
import random
import re

#=== defs and classes

class Creds:
	"""
	Creds handles all kinds of credentials for websites. Credentials are combinations of username and/or email address and a password with salt and pepper.
	"""

	# list alphabet (lowercase)
	l_alpha = list(string.ascii_lowercase)

	# list capitalized alphabet (uppercase)
	l_cap_alpha = list(string.ascii_uppercase)

	# list digits 
	l_digits = list(string.digits)

	# list symbols 
	l_symbols = list(string.punctuation)
	
	# list_types
	l_types = ['alpha','cap_alpha','digit','symbol']

	
	def type_in_password(self, password: str, type:['alpha', 'cap_alpha', 'digit', 'symbol']) -> bool:
		"""
		Checks, if password contains uncapitalized character.
		:param password: str
		:param type: str ["alpha","cap_alpha","digit","symbol")
		:return :boolean
		"""
		if type == "alpha":
			_list = self.l_alpha
		elif type == "cap_alpha":
			_list = self.l_cap_alpha
		elif type == "digit":
			_list = self.l_digits
		elif type == "symbol":
			_list = self.l_symbols

		for char in password:
			for item in _list:
				if item == char:
					return True
		return False
	
	def length_of_password(self, password: str, min_length: int = 12) -> bool:
		"""
		Checks the length of the password.
		A secure password needs at least 12 characters.
		:param password: str
		:param min_lengths: int = 12
		:return bool
		"""
		if len(password) > 11:
			return True
		return False
	
	
	def check_valid_password(self,
						  password: str,
						  min_length :int = 12):
		"""
		Checks, if a password is valid and contains
			- uncapitalized character
			- capitalized character
			- digit
			- symbol
			- length >= min_length

		:param password: str
		:param min_length: int = 12
		:return : d_result[b_valid, l_msg: list]: dict
		"""
		d_result = {'b_valid': False, 'l_msg': []}
		l_msg = []
		b_valid = True
		b_check = False

		if password:
			if not self.type_in_password(password, 'alpha'):
				l_msg.append('Error: No uncapitalized character in password!')
				b_valid = False
			if not self.type_in_password(password, 'cap_alpha'):
				l_msg.append('Error: No capitalized character in password!')
				b_valid = False
			if not self.type_in_password(password, 'digit'):
				l_msg.append('Error: No digit character in password!')
				b_valid = False
			if not self.type_in_password(password, 'symbol'):
				l_msg.append('Error: No symbol character in password!')
				b_valid = False
			if not self.length_of_password(password, min_length):
				l_msg.append(f'Error: Password must have at least {min_length} characters!')
				b_valid = False
		else: # if not password
			b_valid = False
			l_msg.append('Error: No password!')

		if b_valid == False:
			b_check = False
		else:
			b_check = True

		d_result.update({'b_valid': b_check, 'l_msg': l_msg})

		return d_result


	def create_secure_password(self, length: int = 25) -> str:
		"""
		Creates a secure password with a given length, but at least with 12 characters.
		:param length: int = 25
		:return pw: str
		"""
		# instantiate variables
		pw = ''
		l_pw_raw = []
		d_group = {
				'0': self.l_alpha,
				'1': self.l_cap_alpha,
				'2': self.l_digits,
				'3': self.l_symbols
				}

		# minimal length of passwords are 12 characters
		if length < 12:
			length = 12

		# get one character from each group first and append to the list
		l_pw_raw.append(random.choice(self.l_alpha))
		l_pw_raw.append(random.choice(self.l_cap_alpha))
		l_pw_raw.append(random.choice(self.l_digits))
		l_pw_raw.append(random.choice(self.l_symbols))

		# fill list up wih characters from randomized groups
		for i in range(length-4):
			i_rand = random.randrange(0,4)
			rand_char = random.choice(d_group[str(i_rand)])
			l_pw_raw.append(rand_char)

		# shuffle the list and create pw-string to return
		random.shuffle(l_pw_raw)
		for c in l_pw_raw:
			pw += c
		return pw


	def check_valid_email(self, email: str):
		"""
		Checks, if email address is valid.
		:param email: str
		:return d_valid_email: dict {'b_valid': bool, 'l_msg': []}
		"""
		# initialize variables
		b_valid = False
		l_msg = []

		# check if email is given
		if not email:
			l_msg.append('Error: No email!')
			return {'b_valid': False, 'l_msg': l_msg}

		# step 0: lowercase
		email = email.strip().lower()

		# step 1: define regex pattern for email validation
		# Explanation:
		# ^ 					--> start of string
		# [a-z0-9._%+-]{2,}		--> start of string
		# @ 					--> start of string
		# [a-z0-9.-]{2,}		--> start of string
		# \. 					--> start of string
		# [a-z]{2,}				--> start of string
		# $ 					--> start of string
		email_pattern = r'^[a-z0-9._%+-]{2,}@[a-z0-9.-]{2,}\.[a-z]{2,}$'
		
		# step 2: check match
		if re.match(email_pattern, email):
			b_valid = True
		else:
			# if invalid, find reason for better feedback
			if '@' not in email:
				l_msg.append('Error: Email address contains no @!')
			else:
				parts = email.split('@')
				if len(parts[0]) < 2:
					l_msg.append('Error: Part before @ contains less than 2 characters!')
				if '.' not in email:
					l_msg.append('Error: Email address contains no dot!')
				else:
					domain_parts = parts[1].split('.')
					if len(domain.parts[0]) < 2:
						l_msg.append('Error: Email part between @ and dot must contain at least 2 characters!')
					if len(domain.parts[-1]) < 2:
						l_msg.append('Error: Email oart behind @ and dot must contain at least 2 characters!')
		return {'b_valid': b_valid, 'l_msg': l_msg}
	


#=== main

if __name__ == '__main__':
	creds = Creds()
	print(creds.check_valid_email('emailhost.com'))
