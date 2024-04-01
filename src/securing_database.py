def encrypt_database(load, Fernet, remove, DE_PASSWORD_PATH:str, EN_PASSWORD_PATH:str, key:str=None ) -> None: # Encrypt the database.. 
    data:str = None 
    try : 
        with open(file= DE_PASSWORD_PATH, mode='r', encoding='utf-8') as file :
            data = file.read()
    except :
        # If the database is not found.. 
        raise Exception('Error: The database file is not found..!')

    if not data : 
        # If the database is empty.. 
        raise Exception('Error: The database is empty..!')
    # If there is no key.. 
    if not key : 
        key = Fernet.generate_key().decode() 
        print (f"Your Encryption key is : \033[0;32m{key}\033[0m")
    print("\033[0;91mPlease keep your key in a safe place.")
    print("Do Not share it with anyone.")
    print("If you lose your key, you will not be able to access the database..!\033[0m")
    print ("\033[0;34mThe database has been encrypted successfully.\033[0m")
    # Generate the cypher.. 
    cypher:Fernet = Fernet( key.encode() )
    # Encrypt the data.. 
    enc_data: str = cypher.encrypt(data.encode()).decode()
    # Save the data into the new file.. 
    with open(file= EN_PASSWORD_PATH, mode='w', encoding='utf-8') as file :
        file.write(enc_data)
    # remove the old file.. 
    remove( DE_PASSWORD_PATH )

def decrypt_database(load, Fernet, remove, EN_PASSWORD_PATH:str, DE_PASSWORD_PATH:str, key:str=None ) -> None : # Decrypt the database.. 
    data:str = None
    try : 
        # read the encryption file.. 
        with open(file= EN_PASSWORD_PATH , mode='r', encoding='utf-8') as file :
            data = file.read()
    except : 
        # If there is no database.. 
        raise Exception('Error: There is no database is found..!')
    # If there is no data in the databse.. 
    if not data: 
        raise Exception('Error: The database is empty..!')
    # Generate the cypher.. 
    cypher:Fernet = Fernet( key.encode() )
    # Decrypt the file.. 
    enc_data: str = cypher.decrypt(data.encode()).decode()
    # Save the data into new file.. 
    with open(file= DE_PASSWORD_PATH , mode='w', encoding='utf-8') as file :
        file.write(enc_data)
    # remove the old file.. 
    remove( EN_PASSWORD_PATH )