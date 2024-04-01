class Const: 
    def __init__(self, dirname, system,ascii_letters, digits, punctuation) :
        self.PASSWORD_MIN_LENGTH:int = 16  # The min length of the password.
        self.PASSWORD_MAX_LENGTH:int = 2000  # The max length of the password.
        self.USERNAME_MIN_LENGTH:int = 4  # The min length of the username.
        self.USERNAME_MAX_LENGTH:int = 20  # The max lingth of the username.
        self.DATABASE_PATH:str = dirname(__file__).replace('src','DataBase\\' if system() == "Windows" else 'DataBase/' ) # The database folder path.
        self.DATABASE_FILE_JSON:str = ".passwords.json"
        self.DATABASE_FILE_X:str = ".passwords.json.x"
        self.EN_PASSWORD_PATH: str = self.DATABASE_PATH + self.DATABASE_FILE_X  # The encryption database file.
        self.DE_PASSWORD_PATH: str = self.DATABASE_PATH + self.DATABASE_FILE_JSON  # The decryption database file.
        self.LETTERS:str = ascii_letters + digits + punctuation.replace('\\', '')  # The Alphabet.