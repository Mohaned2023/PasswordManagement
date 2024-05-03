## **About the Tool :**
- This tool is made to generate strong passwords.   
- Also manage passwords and save them in a `JSON` file to encrypt the data so that it is not hacked.  
- As well as other features, such as displaying passwords in two different formats and searching for a
specific password that has been previously saved

## **Features :**
1) **Generate Password:** 
    - This feature generated a password with min length of 16 and max length of 2000.
    - The generated password will appear on the screen in green, **noting** that `there are no spaces in the password`.
    - The password is generated by random selection from the **ASCII** table.
    - The Alphabet: ``abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[]^_`{|}~``
    - As you can see in the `Alphabet` there is **No space**.
2) **Save Password:**
    - This feature is used ot save the password in a **JSON** file.
    - By using a **username** for the password, the tool can store each password individually.
    - Saving the password as this : `'username':'password'`.
    - After saving the password into a **JSON** file it will ask you if you want to **encrypt** the file.
    - If the file was previously encrypted, the tool will encrypt it immediately after using it.
3) **Encryption and Decryption:**
    - This feature is automatically used by the tool to encrypt and decrypt the **JSON** file.
    - It uses very strong cypher for the encryption and with very strong key.
    - You can also use your own key.
    - If the file is not ecrypt the tool will ask you if you need to ecrypt the file.
    - If the file was ecrypt before using, the tool will be encrypted automatically.
    - Please keep your key in a safe place and do Not share it with anyone.
> [!NOTE]
> if you lost your key or deleted the **JSON** file, you will not be able to access the password!
4) **Show Passwords:**
    - This feature shows you all passwords in the **JSON** file.
    - There are two ways to display passwords, the first displays the complete password and the other displays the passwords formatted in a table.
    - The second method displays only the first 30 characters of the password.
    - In other words, if there is a password that is more than 30 characters long, only 30 characters will be displayed.
    - To view the entire password, use the first method or the **find** feature
5) **Find Password:**
    - This feature searches the json file and displays the results.
    - Search is done by **username**.
    - You can also use any keyword for quick search.
    - Please when you add new password to the file Make sure you give it an understandable name so you can look for it at another time.
    - **Like** : `'example@gmail.com'` or `'github Mohaned2023'`.
6) **Delete Password:**
    - This feature delete the password from the database.
    - Delete the password by **username**.
> [!NOTE]
> If you delete the password, you will not be able to recover it.
7) **Update info:**
    - This feature used to update the information in the database.
    - To specify the target, you must search by entering the **username** first. 
    - You can update 1.`Password` 2.`Username` 3.`Password and Username`.
    - When you update the password will create for you a new password.
    - It will ask you to enter a length for the new password.

## **Usage:**
- **display the help message:**
```bash 
python PM.py -h | python PM.py --help
```
- **Generate Password:**
```bash
python PM.py -l <Number> | python PM.py --length <Number>
```
- **Generate Password And Save It:**
```bash
python PM.py -l <Number> -s | python PM.py --length <Number> --save
```
- **Find Password:**
```bash
python PM.py -fp | python PM.py --find-password
```
- **Show Password method 1:**
```bash
python PM.py -sp | python PM.py --show-passwords
```
- **Show Password method 2 as Table:**
```bash
python PM.py -spt | python PM.py --show-passwords-table
```
- **Delete Password:**
```bash
python PM.py -dp | python PM.py --delete-password
```
- **Update Password:**
```bash
python PM.py -up | python PM.py --update-password
```

## **About The Programmer:**
Hi, my name is `Mohaned Sharhan` known as `Mr.X`.   
- I liked that this tool worked for the purpose of protecting my accounts from being hacked by creating strong passwords, saving them, and encrypting them.   
- It was difficult to build a sensory tool like this one from scratch without any help, but I did it and succeeded.
- I am proud that I was able to accomplish this difficult task alone without any help.
- I learned really cool things like encryption and decryption text and files.
- I'm excited to build more cool tools
> I have completed in **2024-04-01 11:04 PM**.  

### **My Accounts:**
> - [**LinkedIn**](https://www.linkedin.com/in/mohaned2023)  
> - [**X**](https://x.com/MrX2023M)
> - [**Instagram**](https://www.instagram.com/mr.lxzl)