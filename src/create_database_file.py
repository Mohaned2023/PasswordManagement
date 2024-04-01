def is_there_a_file(DATABASE_PATH:str, DATABASE_FILE_JSON:str, DATABASE_FILE_X:str, listdir) -> bool : # Check if there is a database file.. 
    files: list[str] = listdir(DATABASE_PATH)
    # If there is file.. 
    if DATABASE_FILE_JSON in files or DATABASE_FILE_X in files : 
        return True 
    # If there is no file.. 
    return False 

def create_file(DE_PASSWORD_PATH:str) -> None: # Create database file.. 
    with open(DE_PASSWORD_PATH, 'w') as file : 
        pass