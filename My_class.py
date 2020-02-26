import shelve
import os
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

class teacher(Person):
	def __init__(self, name, age = 20, pay = None):
		Person.__init__(self, name, age)
		self.pay = pay
	def tell(self):
		print('Name - {}\nAge - {}\npay - {}\n'.format(self.name, self.age, self.pay))

class Student(Person):
	def __init__(self, name, age, kurs):
		Person.__init__(self, name, age)
		self.kurs = kurs
	def tell(self):
		print('Name - {}\nAge -  {}\nKurs -  {}'.format(self.name, self.age, self.kurs))
	def change(self, add = 1):
		self.kurs += add

while True:
	nameOBJ = input('Введите имя для создания объекта и укажите класс:')
	if nameOBJ == 'exit': break
	choise_class = input('1. Teacher\n2. Student: ')
	if choise_class == '1':
		key_name = nameOBJ
		NAME = input("Введите имя: ")
		AGE = input('Введите возраст: ')
		PAY = int(input('Введите зарплату: '))
		nameOBJ = teacher(NAME, AGE, PAY)
		Bfile = shelve.open('My_class')
		Bfile[key_name] = nameOBJ
	if choise_class == '2':
		key_name = nameOBJ
		NAME = input('Введите имя: ')
		AGE = input("Введите возраст: ")
		KURS = int(input('Введите курс: '))
		nameOBJ = Student(NAME, AGE, KURS)
		with shelve.open('My_class') as Bfile:
			Bfile[key_name] = nameOBJ
print("output from file:\n")
for i in range(100):
	print("-", end = '')
print('')
with shelve.open('My_class') as Bfile:
	while True:
		name_obj = input('Enter key: ')
		if name_obj == 'exit': break
		try:
			obj = Bfile[name_obj]
			obj.tell()
		except KeyError:
			print("Key not found")