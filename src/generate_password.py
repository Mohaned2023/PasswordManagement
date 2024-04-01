def generate_strong_password(n:int, MIN_LENGTH:int, MAX_LENGTH:int, letters:str, choice) -> str : # Generate Password..
    # Check the min and max length of the password..
    if n < MIN_LENGTH or n > MAX_LENGTH :
        raise Exception(f"Error: The lenght of the password is less than `{MIN_LENGTH}` or more than `{MAX_LENGTH:,}`...!")
    # returning the password using `choice` function in `random` module..  
    return ''.join( choice(letters) for _ in range(n) )