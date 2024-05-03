# new function in v2.0
def update_password( # Update password or username or both..
        username: str, # search username
        DE_PASSWORD_PATH: str, # the path of the database
        load, # for json file read the data
        dump, # for json file write the data
        new_password: str = None, # the new password for the update
        new_username: str = None, # the new username for the update
        function: str = None # the function which will updated -> password, username, both
    ) -> None :
    # open the file to get all data..
    with open(file = DE_PASSWORD_PATH, mode='r', encoding='utf-8') as file :
        data:dict = load(file)
    # save the keys (usernames).. 
    keys: list[str] = list(data.keys())
    # check if the username is in the database..
    if username not in keys :
        raise Exception('Username Not Found..!')

    new_data:dict[str:str] = {}
    # update password function..
    if function == "PASSWORD" :
        new_data = data 
        new_data[username] = new_password
    # update username function..
    elif function == "USERNAME" :
        # looping in the usernames..
        for key in keys :
            # find the username and updated..
            if key == username:
                new_data[new_username] = data[username]
                continue
            new_data[key] = data[key]
    # update both username and password..
    elif function == "BOTH" :
        # looping in the usernames..
        for key in keys : 
            # find the username and updated with the password..
            if key == username :
                new_data[new_username] = new_password
                continue
            new_data[key] = data[key]
    # save the update..
    with open( file=DE_PASSWORD_PATH, mode='w', encoding='utf-8') as file : 
        dump(new_data, file)
    print('\033[0;34mThe file has been successfully updated.\033[0m')