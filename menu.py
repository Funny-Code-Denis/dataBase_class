'''Console program to work with the database
Devoloper: Funny_Code
Version: 1.0
'''
import My_class
import shelve
import os
change_fields = ('Age', 'Address', 'Pay', 'Job', 'Height', 'Weight', 'Shoe size', 'Clothing size')
while True:
	try:
		choise = input('1. Bring out human data\n\
2. Add a record\n\
3. Delete the record\n\
4. Change the record\n\
5. Documentation\n\
6. Exit\n')
		if choise == '1':
			with shelve.open('My_class') as file:
				for keys in file.keys():
					print(keys)
				key = input('Enter key: ')
				Object = file[key]
			Object.output()
			os.system('pause')
		elif choise == '2':
			Name = input('Enter name: ')
			Age = int(input('Enter age: '))
			Address = input('Enter address: ')
			Job = input('Enter job: ')
			Pay = input('Enter pay: ')
			Height = int(input('Enter height: '))
			Weight = int(input('Enter weight: '))
			Shoe_size = int(input('Enter shoe size: '))
			Clothing_size = input('Enter clothing size: ')
			Date_of_birth = input('Enter date of birth: ')
			Key = input("Enter key: ")
			Object = My_class.Person(Name, Age, Address, Job, Pay, Height, Weight, Shoe_size, Clothing_size, Date_of_birth)
			with shelve.open('My_class') as file:
				file[Key] = Object
			print('The record is saved')
			os.system('pause')
		elif choise == '3':
			with shelve.open('My_class') as file:
				for keys in file.keys():
					print(keys)
				key = input('Enter key: ')
				del file[key]
				print('The record has been deleted')
				os.system('pause')
		elif choise == '4':
			with shelve.open('My_class') as file:
				for keys in file.keys():
					print(keys)
				key = input("Enter key: ")
				Object = file[key]
				fild = 1
				for element in change_fields:
					print(str(fild) + '. ', element)
					fild += 1
				fild = int(input('Enter fild: '))
				fild -= 1
				if fild == 0:
					Object.set_age()
					file[key] = Object
				elif fild == 1:
					Object.set_address()
					file[key] = Object
				elif fild == 2:
					Object.set_pay()
					file[key] = Object
				elif fild == 3:
					Object.set_job()
					file[key] = Object
				elif fild == 4:
					Object.set_height()
					file[key] = Object
				elif fild == 5:
					Object.set_weight()
					file[key] = Object
				elif fild == 6:
					Object.set_shoe_size()
					file[key] = Object
				elif fild == 7:
					Object.set_clothing_size()
					file[key] = Object
				else:
					print('Unknown comand')
				os.system('pause')
		elif choise == '5':
			print(__doc__)
		elif choise == '6':
			break
		else:
			print('Unknown comand')
			os.system('pause')
	except EOFError:
		print('Unknown comand')
		os.system('pause')
