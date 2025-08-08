from cryptography.fernet import Fernet

"""  #TO CREATE A KEY FILE
def create_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
create_key()"""


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# master_pswd = input("Whats your master password : ")
# key = load_key() + master_pswd.encode()
# fer = Fernet(key)      "This part is way tougher"

key = load_key()
fer = Fernet(key)


def add():
    name = input("Name : ")
    pswd = input("Password : ")
    with open("password.txt", "a") as p:
        p.write(name + " | " + fer.encrypt(pswd.encode()).decode() + "\n")


def view():
    with open("password.txt", "r") as p:
        for i in p.readlines():
            data = i.rstrip()
            user, password = data.split("|")
            print(
                "User : ",
                user,
                "| Password : ",
                fer.decrypt(password.encode()).decode(),
            )


while True:
    q1 = (
        input(
            'Would you like to view or add new password, "q" to quit \n(view/add/q): '
        )
        .strip()
        .lower()
    )
    if q1 == "q":
        break
    if q1 == "view":
        view()
    elif q1 == "add":
        add()
