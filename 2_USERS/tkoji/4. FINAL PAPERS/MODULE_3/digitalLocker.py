from tkinter import *
from tkinter import messagebox

root = Tk()

#########################
###     FUNCTIONS     ###
#########################
def ring():
    messagebox.showinfo(title="Platform 9¾", message="Terrible Things Are About To Happen At Hogwarts.")
    
def unlock():
    messagebox.showinfo(title="Platform 9¾", message="Are you Gryffindor or Slytherin?")
    
    label_locker_keyboard = LabelFrame(frame_settings, text='Unlocker the locker enter Platform 9¾')
    label_locker_keyboard.columnconfigure((0,1,2), weight=0, minsize=90)
    label_locker_keyboard.grid(row=1, column=0, columnspan=3, padx=30, pady=0,ipadx=20, ipady=0)
    
    label_locker_display = LabelFrame(frame_settings, text='Display message.')
    label_locker_display.columnconfigure((0,1,2), weight=0, minsize=90)
    label_locker_display.grid(row=1, column=3, columnspan=3, rowspan=3, padx=30, pady=0,ipadx=20, ipady=0)

    msg_locker = Message(label_locker_display, text='',padx=40,pady=30)
    msg_locker.grid(row=0,column=0)


def admin():
    # ne znam kak odo dobit da bude ispod unlock framea, kada ukljucim admin funkciju tipkovica nestane.
    frame_admin_settings = Frame(root)
    frame_admin_settings.grid(row=0, column=4, rowspan=6, columnspan=5)
    label_admin = LabelFrame(frame_admin_settings, text='Admin panel.')

    admin_button1 = Button(label_admin, text='-',padx=40,pady=30)
    admin_button1.grid(row=0,column=0)
    
    
    
#########################
### GUI configuration ###
#########################
# PIN code hidden 
    pwd_box1 = Button(label_locker_keyboard, text='-',padx=40,pady=30,command=lambda: add_number('1'))
    pwd_box1.grid(row=0,column=0)

    pwd_box2 = Button(label_locker_keyboard, text='-',padx=40,pady=30, command=lambda: add_number('1'))
    pwd_box2.grid(row=0,column=1)

    pwd_box3 = Button(label_locker_keyboard, text='-',padx=40,pady=30, command=lambda: add_number('1'))
    pwd_box3.grid(row=0,column=2)

    pwd_box4 = Button(label_locker_keyboard, text='-',padx=40,pady=30, command=lambda: add_number('1'))
    pwd_box4.grid(row=0,column=3)

# Buttons
    button1 = Button(label_locker_keyboard, text='1',padx=40,pady=20, command=lambda: add_number('1'))
    button1.grid(row=1,column=0)

    button2 = Button(label_locker_keyboard, text='2',padx=40,pady=20, command=lambda: add_number('2'))
    button2.grid(row=1,column=1)

    button3 = Button(label_locker_keyboard, text='3',padx=40,pady=20, command=lambda: add_number('3'))
    button3.grid(row=1,column=2)

    button4 = Button(label_locker_keyboard, text='4',padx=40,pady=20, command=lambda: add_number('4'))
    button4.grid(row=2,column=0)

    button5 = Button(label_locker_keyboard, text='5',padx=40,pady=20, command=lambda: add_number('5'))
    button5.grid(row=2,column=1)

    button6 = Button(label_locker_keyboard, text='6',padx=40,pady=20, command=lambda: add_number('6'))
    button6.grid(row=2,column=2)

    button7 = Button(label_locker_keyboard, text='7',padx=40,pady=20, command=lambda: add_number('7'))
    button7.grid(row=3,column=0)

    button8 = Button(label_locker_keyboard, text='8',padx=40,pady=20, command=lambda: add_number('8'))
    button8.grid(row=3,column=1)

    button9 = Button(label_locker_keyboard, text='9',padx=40,pady=20, command=lambda: add_number('9'))
    button9.grid(row=3,column=2)

    button10 = Button(label_locker_keyboard, text=' ',padx=40,pady=20, command=lambda: add_number('9'))
    button10.grid(row=4,column=0)

    button11 = Button(label_locker_keyboard, text='0',padx=40,pady=20, command=lambda: add_number('9'))
    button11.grid(row=4,column=1)

    button12 = Button(label_locker_keyboard, text='C',padx=40,pady=20, command=lambda: admin('9'))
    button12.grid(row=4,column=2)
        
        
frame_settings = Frame(root)
frame_settings.grid(row=0, column=0, rowspan=6, columnspan=5)
# Message(root)
label_locker_keyboard = LabelFrame(frame_settings, text='Platform 9¾')
label_locker_keyboard.columnconfigure((0,1,2), weight=1, minsize=90)
label_locker_keyboard.grid(row=0, column=0, columnspan=3, padx=30, pady=30,ipadx=20, ipady=10)

rb_show_password = Button(label_locker_keyboard, text='Ring', command=ring)
rb_show_password.grid(row=1, column=0)

rb_hide_password = Button(label_locker_keyboard, text='Unlock', command=unlock)
rb_hide_password.grid(row=1, column=2)




root.mainloop()