# Python OOP
class Employee:

	num_of_emps = 0
	raise_amt = 1.04
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@company.com'
		self.pay = pay

		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str_1.split('-')
		return cls(first, last, pay)

	# @staticmethod
	# def is_workday(day):
	# 	if day.weekday() == 5 or day.weekday() == 6:
	# 		return False
	# 	return True

emp_1 = Employee('Kingston', 'Duru', 1000000)
emp_2 = Employee('David', 'Bill', 2000000)

# import datetime
# my_date = datetime.data(2016, 7, 10)

# print(Employee.is_workday(my_date))