'''Documentation:
Module to create a class object
Has fields:
	- name
	- age
	- address
	- job
	- pay
	- height
	- weight
	- shoe_size
	- clothing_size
	- date_of_birth
Has functions:
	- set_age()
	- set_job()
	- set_address()
	- set_height()
	- set_weight()
	- set_shoe_size()
	- set_clothing_size()
	- output()
Devoloper: Funny_Code
Date: 27.02.2020
'''
class Person:
	def __init__(self, name, age, address,  job, pay, height, weight, shoe_size, clothing_size, date_of_birth):
		self.name = name
		self.age = age
		self.address = address
		self.job = job
		self.pay = pay
		self.height = height
		self.weight = weight
		self.shoe_size = shoe_size
		self.clothing_size = clothing_size
		self.date_of_birth = date_of_birth

	def set_age(self):
		new_age = int(input('Enter name: '))
		self.age = new_age
	
	def set_address(self):
		new_address = input('Enter address: ')
		self.address = new_address
	
	def set_job(self):
		new_job = input("Enter job: ")
		self.job = new_job
	
	def set_height(self):
		new_height = int(input('Enter height: '))
		self.height = height
	
	def set_weight(self):
		new_weigth = int(input('Enter weight: '))
		self.weight = new_weigth
	
	def set_shoe_size(self):
		new_shoe_size = int(input('Enter shoe size: '))
		self.shoe_size = new_shoe_size
	
	def set_clothing_size(self):
		new_clothing_size = input('Enter clothing size: ')
		self.clothing_size = new_clothing_size

	def output(self):
		for i in range(30):
			print('-', end = '')
		print('')
		print('Name:          ', self.name)
		print('Age:           ', self.age)
		print('Address:       ', self.address)
		print('Job:           ', self.job)
		print('Pay:           ', self.pay)
		print('Height:        ', self.height)
		print('Weight:        ', self.weight)
		print('Shoe size:     ', self.shoe_size)
		print('Clothing size: ', self.clothing_size)
		print('Date of birth: ', self.date_of_birth)
		for i in range(30):
			print('-', end = '')
		print('')

if __name__ == '__main__':
	Denis = Person(name = 'Denis', age = 19, address = '260/1', job = 'Python devoloper', pay = 'None', height = 176, weight = 71, shoe_size = 41, clothing_size = 'L', date_of_birth = '23.03.2000')
	Denis.output()
