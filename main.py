#Importing necessary libraries
import base64
import os
from tkinter import *
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generate_new_salt():
    salt = os.urandom(16)
    print(salt)
    salt = str(salt)
    saltStringVar = StringVar()
    saltStringVar.set(salt)
    saltWindow = Toplevel()
    saltWindow.configure(bg="#282830")
    saltWindow.title("Your salt")
    saltWindow.geometry("900x300")
    l1 = Label(saltWindow, font="Helvetica 20 bold italic", bg="#282830", fg="#e92d2d", text="Copy just the text inside, without those ' and the b")
    e1 = Entry(saltWindow, bg="#282830", fg="#e92d2d", font="Helvetica 15 bold italic", bd=0, state="readonly", textvariable=saltStringVar, justify="center")
    e1.place(rely=.5, relx=.5, anchor=CENTER, relwidth=1.0)
    l1.place(rely=.3, relx=.5, anchor=CENTER)

def continue_with_salt():
    window1 = Toplevel()
    window1.configure(bg="#282830")
    window1.title("Safe communication encrypted P2P")
    window1.geometry("800x500")
    encryptL1 = Label(window1, font="Helvetica 20 bold italic", bg="#282830", fg="#e92d2d", text="Insert your salt below:")
    encryptE1 = Entry(window1, fg="#e92d2d", font="Helvetica 15 bold italic", bd=0)
    encryptL2 = Label(window1, font="Helvetica 20 bold italic", bg="#282830", fg="#e92d2d", text="Insert your master password below:")
    encryptE2 = Entry(window1, fg="#e92d2d", font="Helvetica 15 bold italic", bd=0)
    encryptL3 = Label(window1, font="Helvetica 20 bold italic", bg="#282830", fg="#e92d2d", text="Message to encrypt:")
    encryptE3 = Entry(window1, fg="#e92d2d", font="Helvetica 15 bold italic", bd=0)
    encryptL1.place(rely=.2, relx=.5, anchor=CENTER)
    encryptE1.place(rely=.3, relx=.5, anchor=CENTER)
    encryptL2.place(rely=.4, relx=.5, anchor=CENTER)
    encryptE2.place(rely=.5, relx=.5, anchor=CENTER)
    encryptL3.place(rely=.6, relx=.5, anchor=CENTER)
    encryptE3.place(rely=.7, relx=.5, anchor=CENTER)
    def encrypt():
        salt_input = encryptE1.get()
        Mpassword_input = encryptE2.get()
        message_input = encryptE3.get()
        salt = salt_input.encode()
        password = Mpassword_input.encode()
        message = message_input.encode()
        kdf = PBKDF2HMAC (
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
        )
        print(salt)
        print(password)
        key = base64.urlsafe_b64encode(kdf.derive(password))
        print(key)
        f = Fernet(key)
        token = f.encrypt(message)
        print(token)
    encrypyB1 = Button(window1, bg="#282830", font="Helvetica 20 bold italic", relief=GROOVE, borderwidth=2, fg="#e92d2d", text="Encrypt", command=encrypt)
    encrypyB1.place(rely=.9, relx=.5, anchor=CENTER)

#Configuring root
root = Tk()
root.title("Safe communication encrypted P2P")
root.geometry("600x500")
root.configure(bg="#282830")

#Adding the widgets
Canva1 = Canvas(root, bg="#282830")
b1Label = Label(Canva1, bg="#282830", text="If you don't yet have a salt click here", fg="#eee", font="Helvetica 17 bold italic")
b1 = Button(Canva1, bg="#303030", relief=GROOVE, borderwidth=2, text="Generate new salt, then continue", font="Helvetica 15 bold italic", fg="#eee", command=generate_new_salt)
b2Label = Label(Canva1, bg="#282830", text="In the case you already have a salt, then click here", font="Helvetica 17 bold italic", fg="#eee")
b2 = Button(Canva1, bg="#303030", relief=GROOVE, borderwidth=2, font="Helvetica 15 bold italic", fg="#eee", text="Continue", command=continue_with_salt)

#Placing everything
Canva1.place(relwidth=1.0, relheight=1.0)
b1Label.place(rely=.05, relx=.5, anchor=CENTER)
b1.place(rely=.15, relx=.5, anchor=CENTER)
b2Label.place(rely=.25, relx=.5, anchor=CENTER)
b2.place(rely=.35, relx=.5, anchor=CENTER)
root.mainloop()