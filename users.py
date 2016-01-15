#!/usr/bin/python3
from datetime import date

class DuplicateUsernameError(Exception):
	pass

class InvalidEmailError(Exception):
	pass

class DuplicateEmailError(Exception):
	pass	

class UnderageError(Exception):
	pass

class LocationNotServicedError(Exception):
	pass

users = {}

class User:
	def __init__(self, email, username, age, location):
		self.email = email
		self.username = username
		self.age = age
		self.location = location
		self.add_user()

	def add_user(self):
		users[self.username] = self

	def remove_user(self):
		del users[self.username]

	def get_users(user_type=None):
		if user_type is not None:
			return [u for u in users.values() if type(u).__name__ == user_type]
		return users

	def __repr__(self):
		return "User: %s" % self.username

class Staff(User):
	def __init__(self, employee_id, department, *args, **kwargs):
		self.employee_id = employee_id
		self.department = department
		super(Staff, self).__init__(*args, **kwargs)

	def __repr__(self):
		return "Staff: %s" % self.username

class Customer(User):
	def __init__(self, customer_id, account_type, *args, **kwargs):
		self.customer_id = customer_id
		self.account_type = account_type
		super(Customer, self).__init__(*args, **kwargs)

	def __repr__(self):
		return "Customer: %s" % self.username


customers = [
	('c1', 'Free', 'u1@email.com', 'user1', 24, 'USA'),
	('c2', 'Premium', 'u3@email.com.au', 'user2', 39, 'AUS'),
	('c3', 'Free', 'u3@email.com.nz', 'user3', 55, 'NZL'),
	('c4', 'Free', 'u3@email.com.uk', 'user4', 17, 'GBR'),
]

staff = [
	('s1', 'sales', 's1@email.com', 'user1', 34, 'USA'),
	('s2', 'hr', 's3@email.com', 'user2', 58, 'CAN'),
	('s3', 'research', 's3@email.com', 'user3', 31, 'CAN'),
	('s4', 'sales', 's4@email.com', 'user4', 26, 'USA'),
]

for customer_id, account_type, email, username, age, location in customers:

	try: 

		if username in users:
			raise DuplicateUsernameError()

		split_email = email.split('@')
		split_domain = split_email[1].split('.')

		if len(split_email) != 2 or (len(split_domain) != 2 and len(split_domain) != 3):
			raise InvalidEmailError()

		if email in [u.email for u in users.values()] > 0:
			raise DuplicateEmailError()

		if date.today().year - 18 < date.today().year - age:
			raise UnderageError()

		if location not in ['USA', 'GBR', 'AUS', 'CAN']:
			raise LocationNotServicedError()

	except DuplicateUsernameError:
		print('Username "%s" already taken.' % username)

	except InvalidEmailError:
		print('Email "%s" is invalid.' % email)

	except DuplicateEmailError:
		print('Email "%s" alredy registered.' % email)

	except UnderageError:
		print('Must be 18. Join us in "%s" year(s)!' % str(18-int(age)))

	except LocationNotServicedError:
		print('Service is not provide in  "%s".' % location)

	else:
		Customer(customer_id, account_type, email, username, age, location)