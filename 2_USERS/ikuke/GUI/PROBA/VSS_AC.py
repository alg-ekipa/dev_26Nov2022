from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
#from playsound import playsound
import sqlite3

root = Tk()
root.title('Intercom')
root.geometry('1000x1200')
root.resizable(True,True)
#password_entry 

def button_click(number):
    password_entry.insert(END, str(number))

def pozvoni():
    messagebox.showinfo(title="Zvono", message="Zvono!")
    #playsound('bell.mp3')
    uneseni_id = entry_id.get()
    cursor.execute("SELECT name FROM stanari WHERE id=?", (uneseni_id,))
    odgovor = cursor.fetchone()
    if odgovor:
        ime_stanara = odgovor[0]  # Assuming the name is stored in the first column
        odgovor = messagebox.askyesno(title='Netko zvoni', message=f'Pozvonili ste: {ime_stanara}\nZelite li otkljucati vrata?')
        if odgovor:
            messagebox.showinfo(title='Vrata', message='Otvoreno!')
    else:
        messagebox.askretrycancel(title='Vrata', message='Pokušaj ponovno?')

def otkljucaj():
    unesena_lozinka = password_entry.get()
    admin = '0000'

    if unesena_lozinka == admin:
        messagebox.showinfo(message='Admin is in d buildnig')
        admin_main_frame.grid()
    else:
        # Execute the select query
        cursor.execute("SELECT name FROM stanari WHERE password=?", (unesena_lozinka))
        result = cursor.fetchone()

        if result:
            name = result[0]
            messagebox.showinfo(message=f'Dobrodošli, {name}!')
        else:
            messagebox.showerror(message='Pogrešna lozinka')


button_frame = Frame(root,width=550,height=400, bg='#008080',cursor='circle')
button_frame.grid(row=1,column=0,sticky='NW')
button_frame.grid_propagate(2)
password_entry = Entry(button_frame, font=('Brush Script MT',25),fg='#80ff00', width=20, borderwidth=25, bg='#000000')
password_entry.grid(row=0,columnspan=5, sticky='NW')
bell_frame = Frame(button_frame,height=100,width=100, bd= 10, highlightbackground='#000000' )
bell_frame.grid(row=4,column=2,sticky='NW')
button_bell= Button(button_frame, command=pozvoni, text='🕭' ,padx=10, pady=10, 
                      bg='#f4caae', activebackground='#66d079',bd=10, relief="raised", 
                      font=('Brush Script MT',20,'bold'))
button_bell.grid(row=5,column=1)




button_1 = Button(button_frame, text="1", padx=22, pady=10, 
                  command=lambda: button_click(1), 
                  bg='#f4caae', activebackground='#66d079',bd=10, relief="raised", font=('Seven Segment',20,'bold'))
button_2 = Button(button_frame, text="2", padx=25, pady=10, 
                  command=lambda: button_click(2), 
                  bg='#f4caae', activebackground='#66d079',bd=10, relief="raised", font=('Brush Script MT',20,'bold'))
button_3 = Button(button_frame, text="3", padx=25, pady=10, 
                  command=lambda: button_click(3), 
                  bg='#f4caae', activebackground='#66d079',bd=10, relief="raised", font=('Brush Script MT',20,'bold'))
button_4 = Button(button_frame, text="4", padx=25, pady=10, 
                  command=lambda: button_click(4), 
                  bg='#f4caae', activebackground='#66d079',bd=10, relief="raised", font=('Brush Script MT',20,'bold'))
button_5 = Button(button_frame, text="5", padx=25, pady=10, 
                  command=lambda: button_click(5), 
                  bg='#f4caae', activebackground='#66d079',bd=10, relief="raised", font=('Brush Script MT',20,'bold'))
button_6 = Button(button_frame, text="6", padx=25, pady=10, 
                  command=lambda: button_click(6), 
                  bg='#f4caae', activebackground='#66d079',bd=10, relief="raised", font=('Brush Script MT',20,'bold'))
button_7 = Button(button_frame, text="7", padx=25, pady=10, 
                  command=lambda: button_click(7), 
                  bg='#f4caae', activebackground='#66d079',bd=10, relief="raised", font=('Brush Script MT',20,'bold'))
button_8 = Button(button_frame, text="8", padx=25, pady=10, 
                  command=lambda: button_click(8), 
                  bg='#f4caae', activebackground='#66d079',bd=10, relief="raised", font=('Brush Script MT',20,'bold'))
button_9 = Button(button_frame, text="9", padx=25, pady=10, 
                  command=lambda: button_click(9), 
                  bg='#f4caae', activebackground='#66d079',bd=10, relief="raised", font=('Brush Script MT',20,'bold'))
button_0 = Button(button_frame, text="0", padx=25, pady=10, 
                  command=lambda: button_click(0), 
                  bg='#f4caae', activebackground='#008080',bd=10, relief="raised", 
                  font=('Brush Script MT',20,'bold'))
button_clear = Button(button_frame, text="Clear", padx=20, pady=10, 
                      command=lambda: password_entry.delete(0, END),
                       bg='#f4caae', activebackground='#008080',bd=10, relief="raised", 
                       font=('Brush Script MT',15,'bold'))
button_enter = Button(button_frame, text='↵ Enter',padx=10, pady=10, command= otkljucaj, 
                      bg='#f4caae', activebackground='#008080',bd=10, relief="raised", 
                      font=('Brush Script MT',15,'bold'))

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=0)
button_enter.grid(row=4, column=2)

admin_main_frame = Frame(root,height=200,width=500, bd=10, relief='sunken', highlightbackground='#000000')
admin_main_frame.grid(row=1, column=1 ,  padx=5, pady=10)
admin_main_frame.grid_remove()


# Connect to the SQLite database
conn = sqlite3.connect('Zgrada.db')
cursor = conn.cursor()

# Create the records table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS stanari (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    surname TEXT,
                    password TEXT)''')

# Function to insert data into the database
def insert_data():
    
    name = entry_name.get()
    surname = entry_surname.get()
    password = entry_password.get()

    # Execute the insert query
    cursor.execute("INSERT INTO stanari (name, surname, password) VALUES (?, ?, ?)", (name, surname, password))

    # Commit the changes
    conn.commit()

    # Clear the entry fields
    entry_name.delete(0, END)
    entry_surname.delete(0, END)
    entry_password.delete(0, END)

    # Refresh the user table
    refresh_user_table()

# Function to delete data from the database
def delete_data():
    selected_item = user_treeview.selection()
    if selected_item:
        item_values = user_treeview.item(selected_item)['values']
        id = item_values[0]

        # Execute the delete query
        cursor.execute("DELETE FROM stanari WHERE id=?", (id,))

        # Commit the changes
        conn.commit()

        # Clear the entry fields
        entry_name.delete(0, END)
        entry_surname.delete(0, END)
        entry_password.delete(0, END)

        # Refresh the user table
        refresh_user_table()

# Function to cancel the input
def cancel_input():
    # Clear the entry fields
    entry_name.delete(0, END)
    entry_surname.delete(0, END)
    entry_password.delete(0, END)

# Function to show user table in Treeview
def show_user_table():
    # Clear the Treeview
    for record in user_treeview.get_children():
        user_treeview.delete(record)

    # Execute the select query
    cursor.execute("SELECT id, name, surname, password FROM stanari")
    rows = cursor.fetchall()

    # Insert data into the Treeview
    for row in rows:
        user_treeview.insert("", "end", values=row)

# Function to refresh the user table
def refresh_user_table():
    # Clear the Treeview
    for record in user_treeview.get_children():
        user_treeview.delete(record)

    # Show the updated user table
    show_user_table()

# Labels
label_id = Label(admin_main_frame, text='ID:')
label_id.grid(row=0, column=0, padx=5, pady=5)

label_name = Label(admin_main_frame, text='Name:')
label_name.grid(row=1, column=0, padx=5, pady=5)

label_surname = Label(admin_main_frame, text='Surname:')
label_surname.grid(row=2, column=0, padx=5, pady=5)

label_password = Label(admin_main_frame, text='Password:')
label_password.grid(row=3, column=0, padx=5, pady=5)

# Entry fields
entry_id = Entry(admin_main_frame)
entry_id.grid(row=0, column=1, padx=5, pady=5)

entry_name = Entry(admin_main_frame)
entry_name.grid(row=1, column=1, padx=5, pady=5)

entry_surname = Entry(admin_main_frame)
entry_surname.grid(row=2, column=1, padx=5, pady=5)

entry_password = Entry(admin_main_frame)
entry_password.grid(row=3, column=1, padx=5, pady=5)

# Buttons
button_insert = Button(admin_main_frame, text='Insert', command=insert_data)
button_insert.grid(row=4, column=0, padx=5, pady=5)

button_delete = Button(admin_main_frame, text='Delete', command=delete_data)
button_delete.grid(row=4, column=1, padx=5, pady=5)

button_cancel = Button(admin_main_frame, text='Cancel', command=cancel_input)
button_cancel.grid(row=4, column=2, padx=5, pady=5)

button_refresh = Button(admin_main_frame, text='Refresh', command=refresh_user_table)
button_refresh.grid(row=4, column=3, padx=5, pady=5)

# Treeview to display user table
treeview_frame = Frame(root,height=200,width=300, bd=5, relief='sunken', highlightbackground='#000000')
treeview_frame.grid(row=2 , column=0 , padx=10, pady=10)
treeview_frame.grid_remove()
treeview_frame.grid_propagate(1)

user_treeview = ttk.Treeview(treeview_frame, columns=('ID', 'Name', 'Surname', 'Password'), show='headings')
user_treeview.grid(row=0, column=0, padx=5, pady=5)

user_treeview.heading('ID', text='ID')
user_treeview.heading('Name', text='Name')
user_treeview.heading('Surname', text='Surname')
user_treeview.heading('Password', text='Password')

adminVar = IntVar()

def toggle_treeview_frame():
    if adminVar.get() == 1:
        treeview_frame.grid()
    else:
        treeview_frame.grid_remove()

admin_frame = Frame(admin_main_frame)
admin_frame.grid(row=1, column=0)
admin_check = Checkbutton(admin_main_frame, text='Pokaži tablicu', variable=adminVar, command=toggle_treeview_frame)
admin_check.grid(row=2, column=5)




root.mainloop()

# Close the database connection
conn.close()


