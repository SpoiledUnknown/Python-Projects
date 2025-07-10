from cryptography.fernet import Fernet as fernet

'''def write_key():
    key = fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = fernet(key)

def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| password: ", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as file:
        file.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view exisitng ones or exit (view/add/q)? ").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        break
    else:
        print("Invalid mode.")
        continue
