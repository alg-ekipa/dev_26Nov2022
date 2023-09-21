import tkinter as tk

def login_page():
    # Clear the current window
    clear_window()

    # Create the login page components
    left_frame = tk.Frame(root, width=300, height=300, bg="white")
    left_frame.grid(row=0, column=0, padx=10, pady=10)

    right_frame = tk.Frame(root, width=300, height=300, bg="white")
    right_frame.grid(row=0, column=1, padx=10, pady=10)

    image_label = tk.Label(left_frame, image=image)
    image_label.pack(padx=10, pady=10)

    page_name_label = tk.Label(right_frame, text="PyFloraPosuda", font=("Helvetica", 24))
    page_name_label.pack(padx=10, pady=10)

    username_label = tk.Label(right_frame, text="Username:")
    username_label.pack(padx=10, pady=10)

    password_label = tk.Label(right_frame, text="Password:")
    password_label.pack(padx=10, pady=10)

    username_entry = tk.Entry(right_frame)
    username_entry.pack(padx=10, pady=10)

    password_entry = tk.Entry(right_frame, show="*")
    password_entry.pack(padx=10, pady=10)

    login_button = tk.Button(right_frame, text="Login", command=login)
    login_button.pack(padx=10, pady=10)

def clear_window():
    # Clear all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

def login():
    # Implement your login logic here
    # For simplicity, let's just print the entered username and password
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}")
    print(f"Password: {password}")

# Create the main window
root = tk.Tk()
root.title("PyFloraPosuda")
root.geometry("800x600")

# Load an image
image = tk.PhotoImage(file="black-cat-in-a-pot.png")

# Create the initial page
login_page()

# Start the Tkinter main loop
root.mainloop()
