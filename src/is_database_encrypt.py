def is_database_encrypt(DATABASE_PATH:str, DATABASE_FILE_JSON:str, DATABASE_FILE_X:str , listdir) -> bool : # check if the database is encrypted.. 
    # Get all files in `DataBase` folder.. 
    files: list[str] = listdir(DATABASE_PATH)
    # If the file is not encrypted and not decrypted.. 
    if DATABASE_FILE_JSON in files and DATABASE_FILE_X in files:
        raise Exception('Error: Database is not good..!') 
    # If the database is encrypted.. 
    elif DATABASE_FILE_X in files :
        return True
    # If the file is not encrypted..
    else :
        return False