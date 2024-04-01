from string       		 import ascii_letters, digits, punctuation # Using to get the Alphabet
from os                  import listdir, remove # Using to get files and remove the files.
from argparse            import ArgumentParser # Using to handle the console interface.
from json                import load, dump # Using to communicate with JSON file.
from rich.console        import Console # Using to print the table in the console.
from os.path 			 import dirname # Using to get the full path.
from random              import choice # Using to generate the password.
from cryptography.fernet import Fernet # Using to secure the database.
from platform 			 import system # Using to get the OS name.
from rich.table          import Table # Using to generate the password table.

from src.show_passwords       import show_passwords, show_passwords_table
from src.securing_database    import decrypt_database, encrypt_database
from src.create_database_file import is_there_a_file, create_file
from src.generate_password    import generate_strong_password
from src.is_database_encrypt  import is_database_encrypt
from src.save_password 	      import save_password
from src.find_password        import find_password
from src.const 				  import Const

def main( arges ) -> None : 
	const = Const(
		ascii_letters = ascii_letters, 
		punctuation = punctuation,
		dirname = dirname,
		system = system,
		digits = digits
	)
	check_file_is_encryption:bool = is_database_encrypt(
			DATABASE_FILE_JSON = const.DATABASE_FILE_JSON,
			DATABASE_FILE_X = const.DATABASE_FILE_X,
			DATABASE_PATH = const.DATABASE_PATH,
			listdir = listdir
	)
	key:str = None 
	try :
		check_file_is_exists:bool = is_there_a_file(
			DATABASE_FILE_JSON = const.DATABASE_FILE_JSON,
			DATABASE_FILE_X = const.DATABASE_FILE_X,
			DATABASE_PATH = const.DATABASE_PATH,
			listdir=listdir
		) # if there is no database file.. 
		if not check_file_is_exists: 
			create_file(
				DE_PASSWORD_PATH = const.DE_PASSWORD_PATH
			)
		# if the database is encryption.
		if check_file_is_encryption and (arges.show_passwords_table or arges.show_passwords or arges.find_password or arges.save):
			print ('You are going to access the database.. the database is encryption...! ')
			key = input('Enter database decryption key: ')
			decrypt_database( # Decrypt the database before using it.
				DE_PASSWORD_PATH = const.DE_PASSWORD_PATH,
				EN_PASSWORD_PATH = const.EN_PASSWORD_PATH, 
				remove = remove,
				Fernet = Fernet,
				load = load,
				key=key
			) 
		# Show Passwords As Table.
		if arges.show_passwords_table :
			show_passwords_table(  # Print all passwords in the Console. 
				DE_PASSWORD_PATH = const.DE_PASSWORD_PATH,
				Console = Console,
				Table = Table,
				load = load
			)
		# Show Passwords. 
		elif arges.show_passwords:
			show_passwords(  # Print all passwords in the Console.
				DE_PASSWORD_PATH = const.DE_PASSWORD_PATH,
				load = load
			)
		# Find password in the database. 
		elif arges.find_password :
			username:str = input('Enter the Username for the password: ')
			result: str = find_password( # Calling the find function. 
				DE_PASSWORD_PATH = const.DE_PASSWORD_PATH,
				username = username,
				load = load
			) 
			print (result if result else '') 
		# Save Password into the database.
		elif arges.length and arges.save :
			username:str = input('Enter the Username for the password: ')
			password:str = generate_strong_password( # Generate New password. 
				MAX_LENGTH = const.PASSWORD_MAX_LENGTH,
				MIN_LENGTH = const.PASSWORD_MIN_LENGTH,
				letters = const.LETTERS,
				n = arges.length,
				choice = choice
			)
			result:str = save_password( # Save the Password.
				USERNAME_MIN_LENGTH = const.USERNAME_MIN_LENGTH,
				USERNAME_MAX_LENGTH = const.USERNAME_MAX_LENGTH,
				DE_PASSWORD_PATH = const.DE_PASSWORD_PATH,
				username = username,
				password = password,
				load = load,
				dump = dump
			) 
			print (result) 
		# Generate password. 
		elif arges.length and not arges.save  : 
			password:str = generate_strong_password( # Generate New password. 
				n=arges.length,
				MIN_LENGTH = const.PASSWORD_MIN_LENGTH,
				MAX_LENGTH = const.PASSWORD_MAX_LENGTH,
				letters = const.LETTERS,
				choice = choice
			) 
			print (f'\033[0;34mYour password is : \033[0;32m{password}\033[0m')
		# if the user not using any.
		else :
			raise Exception('Error Argument: Use `python PM.py --help` for help..!')

		# encrypt the database if the database was decrypted.  
		if key :
			encrypt_database(
				DE_PASSWORD_PATH = const.DE_PASSWORD_PATH,
				EN_PASSWORD_PATH = const.EN_PASSWORD_PATH, 
				remove = remove,
				Fernet = Fernet,
				load = load,
				key=key
			)
			return None

		# if the database is not encrypted before. 
		if not check_file_is_encryption and (arges.show_passwords_table or arges.show_passwords or arges.find_password or arges.save):
			print("The database is not encrytion..!")
			cho:str = input('Do you want to encrypt it? ')
			cho = cho.lower()
			if cho == 'y' or cho == 'yes' :
				cho = input('Do you have your own key? ')
				cho = cho.lower()
				key:str = None 
				if cho == 'y' or cho == 'yes' :
					key = input('Enter the key: ')
				encrypt_database(
					DE_PASSWORD_PATH = const.DE_PASSWORD_PATH,
					EN_PASSWORD_PATH = const.EN_PASSWORD_PATH, 
					remove = remove,
					Fernet = Fernet,
					load = load,
					key=key
				)
			else :
				print("\033[0;91mOk, don't forget,")
				print("the passwords in the database will not be secure,")
				print("so do not share the tool's files with anyone...!\033[0m")
	# Errors Handling. 
	except Exception as error :
		print (f'\033[4;31m{error}\033[0m')
		# encrypt database if there is an Error and if the database is decrypted before. 
		if key and not check_file_is_encryption: 
			encrypt_database(
				DE_PASSWORD_PATH = const.DE_PASSWORD_PATH,
				EN_PASSWORD_PATH = const.EN_PASSWORD_PATH, 
				remove = remove,
				Fernet = Fernet,
				load = load,
				key=key
			)

if __name__ == "__main__" :
	perser:ArgumentParser = ArgumentParser(
		prog="PM",
		epilog="This Tool Was Created by `Mohaned Sherhan` or `Mr.X` .",
	)
	perser.add_argument(
		'-l',
		'--length',
		metavar='Number',
		help="Using for setting the length of the password.",
		type=int
	)
	perser.add_argument(
		'-s',
		'--save',
		help="Save the password in the database using a username.",
		action='store_true'
	)
	perser.add_argument(
		'-sp',
		'--show-passwords',
		help='Showing all password in the database.',
		action='store_true'
	)
	perser.add_argument(
		'-fp',
		'--find-password',
		help='Find a password in the database using a username.',
		action='store_true'
	)
	perser.add_argument(
		'-spt',
		'--show-passwords-table',
		help='Show all passwords in the database in a table.',
		action='store_true'
	)
	main(perser.parse_args())