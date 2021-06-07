import tkinter as tk
from database import user_exists, add_user

import tkinter.messagebox as msgbox


def login(root):
    dialog = tk.Toplevel(root, padx=5, pady=5)
    dialog.title("Login")
    dialog.transient(root)
    dialog.resizable(False, False)

    tk.Label(dialog, text='Username :').grid(row=0, sticky='W')
    tk.Label(dialog, text='Password  :').grid(row=1, sticky='W')

    username = tk.Entry(dialog)
    username.insert(0, "demo_user")
    password = tk.Entry(dialog, show='*')
    password.insert(0, "password")

    username.grid(row=0, column=1, columnspan=2)
    password.grid(row=1, column=1, columnspan=2)

    def ok():
        user = username.get()
        pswd = password.get()

        li = user_exists(user, pswd)

        if li is None:
            msgbox.showerror('Error', 'User does not exist')
        elif li is False:
            msgbox.showerror('Error', 'Password did not match')
        else:
            dialog.destroy()
            root.setvar('user', user)
            root.setvar('loggedin', True)

    dialog.grid_columnconfigure(1, weight=1)
    dialog.grid_columnconfigure(2, weight=1)

    tk.Button(dialog, text='Login', command=ok).grid(
        row=2, column=1, sticky='ew', pady=(10, 0))
    tk.Button(dialog, text='Cancel', command=dialog.destroy).grid(
        row=2, column=2, sticky='ew', pady=(10, 0))


def register(root):
    dialog = tk.Toplevel(root, padx=5, pady=5)
    dialog.title("Signup")
    dialog.transient(root)
    dialog.resizable(False, False)

    tk.Label(dialog, text='Username :').grid(row=0, sticky='W')
    tk.Label(dialog, text='Full Name :').grid(row=1, sticky='W')
    tk.Label(dialog, text='Password  :').grid(row=2, sticky='W')

    username = tk.Entry(dialog)
    fullname = tk.Entry(dialog)
    password = tk.Entry(dialog, show='*')

    username.grid(row=0, column=1, columnspan=2)
    fullname.grid(row=1, column=1, columnspan=2)
    password.grid(row=2, column=1, columnspan=2)

    def ok():
        user = username.get()
        name = fullname.get()
        pswd = password.get()

        li = add_user(user, name, pswd)

        if not li:
            msgbox.showerror('Error', 'User is already registered')
        else:
            dialog.destroy()
            root.setvar('user', user)
            root.setvar('loggedin', True)

    dialog.grid_columnconfigure(1, weight=1)
    dialog.grid_columnconfigure(2, weight=1)

    tk.Button(dialog, text='Signup', command=ok).grid(
        row=3, column=1, sticky='ew', pady=(10, 0))
    tk.Button(dialog, text='Cancel', command=dialog.destroy).grid(
        row=3, column=2, sticky='ew', pady=(10, 0))
