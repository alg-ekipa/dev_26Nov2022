from tkinter import *

root=Tk()

root.title('Algebra Py Dev - kalkulator')
root.geometry('600x400')

def submit():
    name=name_var.get()
    password=passw_var.get()

    print(f'Username: {name}, Password: {password}')

    name_var.set('')
    passw_var.set('')

name_var=StringVar()
passw_var=StringVar()

name_label=Label(root, text='Username', font=('calibre', 10, 'bold'))
name_label.grid(row=0, column=0)

name_entry=Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))
name_entry.grid(row=0, column=1)

passw_label=Label(root, text='Password', font=('calibre', 10, 'bold'))
passw_label.grid(row=1, column=0)

passw_entry=Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')
passw_entry.grid(row=1, column=1)

submit_button=Button(root, text='Submit', command=submit)
submit_button.grid(row=2, column=1)





root.mainloop()