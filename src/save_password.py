def save_password(username:str, password:str, USERNAME_MIN_LENGTH:int, USERNAME_MAX_LENGTH:int, DE_PASSWORD_PATH:str, load, dump) -> str : # Save password into the database.. 
    # Check the min and max length of the username.. 
    username_len:int = len(username)
    if username_len < USERNAME_MIN_LENGTH or username_len > USERNAME_MAX_LENGTH : 
        raise Exception(f"Error: The length of usename is less than `{USERNAME_MIN_LENGTH}` or more than `{USERNAME_MAX_LENGTH}`...!")
    data: dict = {}
    try : 
        # Opening the file and load the data if the file is not empty.. 
        with open( file= DE_PASSWORD_PATH , mode='r', encoding='utf-8') as file :
            data = load(file) 
    except : 
        # If there is not data in the file continue.. 
        pass
    # Check if the username is in the data.. 
    if username in data.keys() :
        raise Exception(f'Error: username `{username}` is in the database..!')
    # Add the new username and password to the data..
    data[username] = password
    # Open the file to add the new data..
    with open( file= DE_PASSWORD_PATH , mode='w', encoding='utf-8') as file :
        dump(data, file)
    # If all Tasks is good return the password.. 
    return f'\033[0;34mYour password is : \033[0;32m{password} \n\033[0;34mThe password has been saved..\033[0m'