import tkinter as tk
from tkinter import messagebox

class RingSystem:
    def __init__(self):
        self.ring_status = False

    def ring_doorbell(self):
        self.ring_status = True
        messagebox.showinfo("Ring", "Someone is at the door!")

    def reset_ring(self):
        self.ring_status = False


class AccessControl:
    def __init__(self):
        self.authorized_users = {"Alice": "1234", "Bob": "5678"}

    def is_authorized(self, username, pin):
        return username in self.authorized_users and self.authorized_users[username] == pin


def handle_ring():
    if ring_system.ring_status:
        messagebox.showinfo("Ring", "Someone is at the door!")
    else:
        messagebox.showinfo("Ring", "No one is at the door.")

def handle_access():
    username = username_entry.get()
    pin = pin_entry.get()

    if access_control.is_authorized(username, pin):
        messagebox.showinfo("Access", "Access granted to the smart home.")
    else:
        messagebox.showerror("Access", "Access denied to the smart home.")


def ring_doorbell():
    ring_system.ring_doorbell()
    handle_ring()


def reset_ring():
    ring_system.reset_ring()
    handle_ring()


ring_system = RingSystem()
access_control = AccessControl()

window = tk.Tk()
window.title("Smart Home Simulation")

ring_label = tk.Label(window, text="Ring System")
ring_label.pack()

ring_button = tk.Button(window, text="Ring Doorbell", command=ring_doorbell)
ring_button.pack()

reset_button = tk.Button(window, text="Reset Ring", command=reset_ring)
reset_button.pack()

access_label = tk.Label(window, text="Access Control")
access_label.pack()

username_label = tk.Label(window, text="Username:")
username_label.pack()

username_entry = tk.Entry(window)
username_entry.pack()

pin_label = tk.Label(window, text="PIN:")
pin_label.pack()

pin_entry = tk.Entry(window, show="*")
pin_entry.pack()

access_button = tk.Button(window, text="Verify Access", command=handle_access)
access_button.pack()

handle_ring()

window.mainloop()