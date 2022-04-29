# import required module
from cryptography.fernet import Fernet
import os




with open("passwords.txt","a") as f:
    if os.stat('passwords.txt').st_size == 0: #check if file is empty
        f.write("NAZWA UZYKOWNIKA | HASLO")

def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            print(line)

def add():
    name = input("nazwa użytkownika: ")
    newPassword = input("Nowe haslo: ")

    with open("passwords.txt","a") as f:
       f.write(name + "|" + newPassword + "\n")
    
def delete():
    with open("passwords.txt","w") as f:
        f.write("NAZWA UZYKOWNIKA | HASLO \n")

def encrypt():
    #genereate a encryption key
    key = Fernet.generate_key() 
# string the key in a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
        #Using the key
    fernet = Fernet(key)
    #chosing the file to encrpyt
    with open("passwords.txt","rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    # opening the file in write mode and 
    # writing the encrypted data
    with open('passwords.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt():
    with open('filekey.key', 'r') as filekey: #get the key from file
        decryption_key=filekey.read()
        key = Fernet(decryption_key)
    with open("passwords.txt","r") as file: #read the encrypted file
            decryption_file = str.encode(file.read())
    with open("passwords.txt","w") as file: #decrypt and rewrite the file
            decrypted_file =(key.decrypt(decryption_file))
            print(decrypted_file)
            writetofile = str(decrypted_file.decode('utf-8'))
            print(writetofile)
            file.write(writetofile)

 
    
   

while True:
    mode = input(
        "Would you like to add a new password,view existing ones delete them all, or generate an encryption key? (view, add, delete, encrpyt). press q to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode =="delete":
        delete()
    elif mode =="encrypt":
        encrypt()
    elif mode =="decrypt":
        decrypt()
    else:
        print("Invalid mode.")
        continue
