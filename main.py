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
    saltWindow.configure()
    saltWindow.title("Your salt")
    saltWindow.geometry("600x300")
    l1 = Label(saltWindow, font="Helvetica 20 bold italic")
    e1 = Entry(saltWindow, font="Helvetica 20 bold italic", bd=0, state="readonly", textvariable=saltStringVar, justify="center")
    e1.place(rely=.5, relx=.5, anchor=CENTER, relwidth=1.0)

#Configuring root
root = Tk()
root.title("Safe communication encrypted P2P")
root.geometry("600x500")
root.configure(bg="#282830")

#Adding the widgets
Canva1 = Canvas(root, bg="#282830")
b1Label = Label(Canva1, bg="#282830", text="If you don't yet have a salt click here", fg="#eee", font="Helvetica 17 bold italic")
b1 = Button(Canva1, bg="#303030", relief=GROOVE, borderwidth=2, text="Generate new salt, then continue", font="Helvetica 15 bold italic", fg="#eee")
b2Label = Label(Canva1, bg="#282830", text="In the case you already have a salt, then click here", font="Helvetica 17 bold italic", fg="#eee")
b2 = Button(Canva1, bg="#303030", relief=GROOVE, borderwidth=2, font="Helvetica 15 bold italic", fg="#eee", text="Continue", command=generate_new_salt)

#Placing everything
Canva1.place(relwidth=1.0, relheight=1.0)
b1Label.place(rely=.05, relx=.5, anchor=CENTER)
b1.place(rely=.15, relx=.5, anchor=CENTER)
b2Label.place(rely=.25, relx=.5, anchor=CENTER)
b2.place(rely=.35, relx=.5, anchor=CENTER)
root.mainloop()