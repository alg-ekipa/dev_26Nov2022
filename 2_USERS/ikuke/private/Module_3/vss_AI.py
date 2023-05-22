import tkinter as tk
from tkinter import messagebox
import sqlite3

class SmartHome:
    def __init__(self):
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                               (username TEXT PRIMARY KEY, pin TEXT)''')
        self.conn.commit()

    def add_user(self, username, pin):
        try:
            self.cursor.execute("INSERT INTO users VALUES (?, ?)", (username, pin))
            self.conn.commit()
            messagebox.showinfo("User Added", "User added successfully.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")

    def remove_user(self, username):
        self.cursor.execute("DELETE FROM users WHERE username=?", (username,))
        self.conn.commit()
        messagebox.showinfo("User Removed", "User removed successfully.")

    def update_user(self, username, new_pin):
        self.cursor.execute("UPDATE users SET pin=? WHERE username=?", (new_pin, username))
        self.conn.commit()
        messagebox.showinfo("User Updated", "User updated successfully.")

    def is_authorized(self, username, pin):
        self.cursor.execute("SELECT * FROM users WHERE username=? AND pin=?", (username, pin))
        return self.cursor.fetchone() is not None


def verify_access():
    username = username_entry.get()
    pin = pin_entry.get()

    if home.is_authorized(username, pin):
        messagebox.showinfo("Access Granted", "Access granted to the smart home.")
    else:
        messagebox.showerror("Access Denied", "Access denied to the smart home.")


def add_user():
    username = add_username_entry.get()
    pin = add_pin_entry.get()

    if username and pin:
        home.add_user(username, pin)
        add_username_entry.delete(0, tk.END)
        add_pin_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a username and PIN.")


def remove_user():
    username = remove_username_entry.get()

    if username:
        home.remove_user(username)
        remove_username_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a username.")


def update_user():
    username = update_username_entry.get()
    new_pin = update_pin_entry.get()

    if username and new_pin:
        home.update_user(username, new_pin)
        update_username_entry.delete(0, tk.END)
        update_pin_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a username and new PIN.")


home = SmartHome()

# Create GUI window
window = tk.Tk()
window.title("Smart Home Access Control")

# Verify Access Section
username_label = tk.Label(window, text="Username:")
username_label.pack()

username_entry = tk.Entry(window)
username_entry.pack()

pin_label = tk.Label(window, text="PIN:")
pin_label.pack()

pin_entry = tk.Entry(window, show="*")
pin_entry.pack()

verify_button = tk.Button(window, text="Verify Access", command=verify_access)
verify_button.pack()

# Add User Section
add_user_label = tk.Label(window, text="Add User")
add_user_label.pack()

add_username_label = tk.Label(window, text="Username:")
add_username_label.pack()

add_username_entry = tk.Entry(window)
add_username_entry.pack()

add_pin_label = tk.Label(window, text="PIN:")
add_pin_label.pack()

add_pin_entry = tk.Entry(window, show="