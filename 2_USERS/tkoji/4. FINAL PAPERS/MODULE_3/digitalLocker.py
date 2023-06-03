from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlite3 as sql

root = Tk()
isUserActive = False
lst_pwd = []
sql_connection = sql.connect('tom_users.db')
s = sql_connection.cursor()

#########################
### GLOBAL FUNCTIONS  ###
#########################
def ring():
    messagebox.showinfo(title="Platform 9¾", message="Terrible Things Are About To Happen At Hogwarts.")

def admin():
    
    def read_db(rows):
        for i in rows:
            tree.insert('', 'end',values=i)

# Admin Frame configuration          
    lbl_admin = LabelFrame(frm_main, text='Admin Menu')
    lbl_admin.columnconfigure((0,1,2), weight=1, minsize=90)
    lbl_admin.grid(row=5,column=0, columnspan=10, rowspan=10, padx=30, pady=30,ipadx=20, ipady=10)

# Admin SQL widget configuration
    lbl_sql = LabelFrame(frm_main, text='Wizard Administration',padx=5,pady=5)
    lbl_sql.grid(row=6,column=0,padx=20, ipadx=20)
       
    tree = ttk.Treeview(lbl_sql, columns=(1,2,3,4), show='headings', height=5,padding=1)
    tree.grid(padx=10, pady=10,row=6, column=0, rowspan=4)

    tree.heading(1, text="PIN")
    tree.column(1, anchor=CENTER, stretch=NO, width=100)
    tree.heading(2, text="Name")
    tree.column(2, anchor=CENTER, stretch=NO, width=100)
    tree.heading(3, text="Surname") 
    tree.column(3, anchor=CENTER, stretch=NO, width=100)
    tree.heading(4, text="Active")
    tree.column(4, anchor=CENTER, stretch=NO, width=100)

    query = "SELECT * FROM users"
    s.execute(query)
    rows = s.fetchall()
    read_db(rows)
    
# Admin User Management widget configuration
    # admin_message_box = LabelFrame(lbl_sql, text='Users',padx=20,pady=20)
    # admin_message_box.grid(row=6,column=1)
    
    admin_name_box = Message(lbl_sql, text='Name',padx=5,pady=5)
    admin_name_box.grid(row=6,column=2)

    admin_name_entry = Entry(lbl_sql)
    admin_name_entry.grid(row=6,column=3,columnspan=2)
    
    admin_sname_box = Message(lbl_sql,width=60,text='Surname',padx=5,pady=5)
    admin_sname_box.grid(row=7,column=2)

    admin_sname_entry = Entry(lbl_sql)
    admin_sname_entry.grid(row=7,column=3,columnspan=2)
    
    admin_pin_box = Message(lbl_sql, text='PIN number',padx=5,pady=5)
    admin_pin_box.grid(row=8,column=2)

    admin_pin_box = Entry(lbl_sql)
    admin_pin_box.grid(row=8,column=3,columnspan=2)
    
    admin_active_box = Message(lbl_sql, text='Is user active?',padx=5,pady=5)
    admin_active_box.grid(row=9,column=2)
    
    ch_box_locker = Checkbutton(lbl_sql, variable=isUserActive)
    ch_box_locker.grid(row=9, column=3,columnspan=2)
    
    button_save = Button(lbl_sql, text='Save',padx=5,pady=5)
    button_save.grid(row=10,column=1)
    
    button_delete = Button(lbl_sql, text='Delete',padx=5,pady=5)
    button_delete.grid(row=10,column=2)
        
    button_cancel = Button(lbl_sql, text='Cancel',padx=5,pady=5)
    button_cancel.grid(row=10,column=3)

    button_logout = Button(lbl_sql, text='Logout',padx=5,pady=5)
    button_logout.grid(row=10,column=4)


def unlock():
    messagebox.showinfo(title="Platform 9¾", message="Are you Gryffindor or Slytherin?")
    
    lbl_keyboard = LabelFrame(frm_main, text='Unlock the locker to enter the Platform')
    lbl_keyboard.columnconfigure(0,minsize=90)
    lbl_keyboard.grid(row=2,padx=30, pady=0,ipadx=30, ipady=0)
     
#########################
### GUI configuration ###
#########################
#PIN code hidden 
    password_entry = Entry(lbl_keyboard, width=35 ,bg='#FFFFFF')
    password_entry.grid(row=3,column=0,columnspan=4)
    
# Buttons
    button1 = Button(lbl_keyboard, text='1',padx=40,pady=20, command=lambda: button_click(1))
    button1.grid(row=4,column=0)

    button2 = Button(lbl_keyboard, text='2',padx=40,pady=20, command=lambda: button_click(2))
    button2.grid(row=4,column=1)

    button3 = Button(lbl_keyboard, text='3',padx=40,pady=20, command=lambda: button_click('3'))
    button3.grid(row=4,column=2)

    button4 = Button(lbl_keyboard, text='4',padx=40,pady=20, command=lambda: button_click('4'))
    button4.grid(row=5,column=0)

    button5 = Button(lbl_keyboard, text='5',padx=40,pady=20, command=lambda: button_click('5'))
    button5.grid(row=5,column=1)

    button6 = Button(lbl_keyboard, text='6',padx=40,pady=20, command=lambda: button_click('6'))
    button6.grid(row=5,column=2)

    button7 = Button(lbl_keyboard, text='7',padx=40,pady=20, command=lambda: button_click('7'))
    button7.grid(row=6,column=0)

    button8 = Button(lbl_keyboard, text='8',padx=40,pady=20, command=lambda: button_click('8'))
    button8.grid(row=6,column=1)

    button9 = Button(lbl_keyboard, text='9',padx=40,pady=20, command=lambda: button_click('9'))
    button9.grid(row=6,column=2)

    button10 = Button(lbl_keyboard, text='C',padx=40,pady=20,command=lambda: clear_list())
    button10.grid(row=7,column=0)

    button11 = Button(lbl_keyboard, text='0',padx=40,pady=20, command=lambda: button_click('0'))
    button11.grid(row=7,column=1)

    button12 = Button(lbl_keyboard, text='E',padx=40,pady=20, command=lambda: validate_password())
    button12.grid(row=7,column=2) 
    
    def button_click(number):
        lst_pwd.append(number)
        password_entry.insert(END, int(number))
  
  
    def validate_password():
        print(lst_pwd)
        access_code = int("".join(map(str, lst_pwd)))
        print(access_code)

        if access_code == 1111:
            msg_locker = Message(lbl_keyboard, text='Welcome to Hogwards, wizard!',padx=40,pady=30,width=150,anchor=CENTER)
            msg_locker.grid(row=2,column=1,columnspan=4)
            admin()
            
        else:
            msg_locker = Message(lbl_keyboard, text='Go away muggle!',padx=40,pady=30,width=150,anchor=CENTER)
            msg_locker.grid(row=2,column=1)
            clear_list()
    
    def clear_list():
        password_entry.delete(first=0,last=100)
        lst_pwd.clear()

frm_main = Frame(root)
frm_main.grid(row=0, column=0)
lbl_keyboard = LabelFrame(frm_main, text='Platform 9¾')
lbl_keyboard.columnconfigure((0,1,2), weight=1, minsize=90)
lbl_keyboard.grid(row=0, column=0,padx=30, pady=30,ipadx=20, ipady=10)

rb_show_password = Button(lbl_keyboard, text='Ring', command=ring)
rb_show_password.grid(row=1, column=0)

rb_hide_password = Button(lbl_keyboard, text='Unlock', command=unlock)
rb_hide_password.grid(row=1, column=2)

root.mainloop()