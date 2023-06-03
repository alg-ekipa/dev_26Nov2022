#make python program which simulates access control with bell button on gui with nice bell picture and bell sound, and access button which trigers another window where keyboard with pin buttons (0-9) input via gui appears and grants access for diferent people and one admin which has pin code 1234 and is able to add, delete and modifiy existing users via another window which opens if pin 1234 is entered


from tkinter import Tk, Button, Label, Entry, messagebox, Toplevel

class AccessControlSystem:
    def __init__(self):
        self.admin_pin = "1234"  # Admin PIN
        self.users = {"John": "4321", "Alice": "9876"}  # Existing users (name: PIN)
        self.current_user = None

        # Create main window
        self.root = Tk()
        self.root.title("Access Control")
        self.root.geometry("200x150")

        # Bell button
        bell_button = Button(self.root, text="Bell", command=self.open_access_window)
        bell_button.pack()

    def open_access_window(self):
        # Create access window
        access_window = Toplevel(self.root)
        access_window.title("Access Window")
        access_window.geometry("200x150")

        # Keyboard GUI
        for i in range(3):
            for j in range(3):
                digit = str(i * 3 + j + 1)
                button = Button(access_window, text=digit, width=5, command=lambda digit=digit: self.enter_digit(digit))
                button.grid(row=i, column=j)

        zero_button = Button(access_window, text="0", width=5, command=lambda: self.enter_digit("0"))
        zero_button.grid(row=3, column=0)

        access_button = Button(access_window, text="Access", width=5, command=self.check_pin)
        access_button.grid(row=3, column=1)

        cancel_button = Button(access_window, text="Cancel", width=5, command=access_window.destroy)
        cancel_button.grid(row=3, column=2)

    def enter_digit(self, digit):
        if self.current_user is None:
            messagebox.showerror("Error", "Please select a user first.")
        else:
            self.current_user += digit

    def check_pin(self):
        if self.current_user is None:
            messagebox.showerror("Error", "Please select a user first.")
        else:
            if self.current_user == self.admin_pin:
                self.open_admin_window()
            elif self.current_user in self.users and self.current_user == self.users[self.current_user]:
                messagebox.showinfo("Access Granted", "Access granted for user: {}".format(self.current_user))
            else:
                messagebox.showerror("Access Denied", "Invalid PIN for user: {}".format(self.current_user))

        self.current_user = None

    def open_admin_window(self):
        # Create admin window
        admin_window = Toplevel(self.root)
        admin_window.title("Admin Window")
        admin_window.geometry("200x150")

        # User management controls
        add_user_label = Label(admin_window, text="Add User:")
        add_user_label.pack()

        add_user_entry = Entry(admin_window)
        add_user_entry.pack()

        add_pin_label = Label(admin_window, text="Enter PIN:")
        add_pin_label.pack()

        add_pin_entry = Entry(admin_window)
        add_pin_entry.pack()

        add_user_button = Button(admin_window, text="Add User", command=lambda: self.add_user(add_user_entry.get(), add_pin_entry.get()))
        add_user_button.pack()

        delete_user_label = Label(admin_window, text="Delete User:")
        delete_user_label.pack()

        delete_user_entry = Entry(admin_window)
        delete_user_entry.pack()

        delete_user_button = Button(admin_window, text="Delete User", command=lambda: self.delete_user(delete_user_entry.get()))
        delete_user_button.pack()

    def add_user(self, username, pin):
        if username in self.users:
            messagebox.showerror("Error", "User already exists.")
        else:
            self.users[username] = pin
            messagebox.showinfo("User Added", "User {} has been added.".format(username))

    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
            messagebox.showinfo("User Deleted", "User {} has been deleted.".format(username))
        else:
            messagebox.showerror("Error", "User does not exist.")


# Run the access control system
access_control = AccessControlSystem()
access_control.root.mainloop()
