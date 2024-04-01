def find_password(username:str, DE_PASSWORD_PATH:str, load) -> str : # Find password using username
    # Open Password File.. 
    with open( file=DE_PASSWORD_PATH, mode='r', encoding='utf-8') as file :
        data: dict = {}
        # if the file is not empty.. 
        try :
            data = load(file)
        except:
            # if the file is empty..
            raise Exception("Error: The database is empty..!")
    found: bool = False
    # Looping in the (keys or usernames)..  
    print()
    for key in data.keys() :
        # find the username.. 
        if username.lower() in key.lower() :
            print (f" \033[0;31m- \033[0;34m{key} \033[0;31m= \033[0;32m{data[key]}\033[0m")
            found = True 
    if not found :
        # if the username is not found.. 
        return f"\033[4;31mError : Username `{username}` is not found in the database..!\033[0m"