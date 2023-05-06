import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Alg ekipa')

closer = tk.BooleanVar()

def ring():
    messagebox.showinfo(title="Greetings!", message="Ringing...")

def unlock():
    messagebox.showinfo(title="Locker", message="Please unlock the safe...")
    label_locker_settings = tk.LabelFrame(frame_settings, text='Unlock the safe here.')
    label_locker_settings.columnconfigure((0,1,2), weight=1, minsize=90)
    label_locker_settings.grid(row=2, column=0, columnspan=3, padx=30, pady=30,ipadx=20, ipady=10)
    #ch_box_locker = tk.Checkbutton(label_locker_settings, text='Click to unlock.')
    ch_box_locker = tk.Checkbutton(label_locker_settings, text='Click to unlock.', variable=closer)
    ch_box_locker.grid(row=0, column=2)
    
    if closer == True:
        close_locker()
    else:
        pass
    
    def close_locker():
        label_locker_settings.destroy()
        
frame_settings = tk.Frame(root)
frame_settings.grid(row = 0, column=0, rowspan=3, columnspan=1)

label_frame_settings = tk.LabelFrame(frame_settings, text='Settings')
label_frame_settings.columnconfigure((0,1,2), weight=1, minsize=90)
label_frame_settings.grid(row=0, column=0, columnspan=3, padx=30, pady=30,ipadx=20, ipady=10)

rb_show_password = tk.Button(label_frame_settings, text='Ring', command=ring)
rb_show_password.grid(row=1, column=0)

rb_hide_password = tk.Button(label_frame_settings, text='Unlock', command=unlock)
rb_hide_password.grid(row=1, column=2)


root.mainloop()

