# Python Object-Oriented Programming


class Employee:
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)



emp_1 = Employee('Kingston', 'Duru', 1000000)
emp_2 = Employee('David', 'Bill', 2000000)

print(Employee.fullname(emp_1))
# print(emp_2.fullname())