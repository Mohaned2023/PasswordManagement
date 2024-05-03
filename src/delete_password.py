# new function in v2.0
def delete_password( # Delete password and username..
        username: str, # search username.
        DE_PASSWORD_PATH: str, # the path of the database
        load, # for json file read the data
        dump  # for json file write the data
    ) -> None : 
    # open the database.
    with open(file = DE_PASSWORD_PATH , mode = 'r', encoding='utf-8') as file :
        data:dict = load(file) 
    # get all keys (usernames).
    keys: list[str] = list(data.keys())
    newData:dict[str : str] = {}
    # check if the username is in the database.
    if username in keys :
        print(f'Did you wont to delete the password of username `{username}` ?')
        choice: str = input(f'[yes/no]: ')
        if choice.lower() != 'yes' and choice.lower() != 'y' :
            print('\033[0;34mOk, I will not delete it..\033[0m')
            return None
        # looping in the usernames
        for key in keys :
            # if the username skip the adding to the new data.
            if key == username :
                continue
            newData[key] = data[key]
    # if the username is not found.
    else : 
        raise Exception('Username Not Found..!')
    # write the new data.
    with open(file = DE_PASSWORD_PATH , mode = 'w', encoding='utf-8') as file :
        dump(newData, file)
    print(f'\033[0;34mThe password of username `\033[0;91m{username}\033[0;34m` has been successfully deleted.\033[0m')