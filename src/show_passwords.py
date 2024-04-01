def show_passwords(DE_PASSWORD_PATH:str , load) -> None : # Show Passwords.. 
    data:dict = {}
    try : 
        with open(file= DE_PASSWORD_PATH, mode='r', encoding='utf-8') as file :
            data = load(file)
    except :
        # If the database is empty.. 
        raise Exception('Error: Database is empty..!')
    i:int = 0
    print ('')
    # Looping in the database.. 
    for key in data.keys() :
        i += 1 
        print (f'\033[0;31m{i} - \033[0;34m{key} \033[0;31m= \033[0;32m{data[key]}\033[0m')
    print('')

def show_passwords_table(DE_PASSWORD_PATH:str, load, Table, Console) -> None : # show passwords in table.. 
    data: dict = {}
    try :
        with open(file= DE_PASSWORD_PATH, mode='r', encoding='utf-8') as file :
            data = load(file)
    except:
        # If the database is empty.. 
        raise Exception("Error: The database is empty..!")
    # Create The table.. 
    table = Table(
        title='Passwords',
        caption='Note: Passwords longer than 30 characters will be truncated. To retrieve the full password, use (--find-password) function or (--show-passwords) function.'
    )
    # Create the columns.. 
    table.add_column("ID")
    table.add_column("Username")
    table.add_column("Password",max_width=30)

    print("\n")
    i:int = 1
    # Create the rows.. 
    for key in data.keys() :
        table.add_row( str(i), key, data[key], style='bright_green')
        i += 1 
    # Print the Table.. 
    Console().print(table)
    print("\n")