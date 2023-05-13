from tkinter import *

root = Tk()
root.geometry('600x400')

def klikni_gumb():
    print(f'{n}. stisnut je gumb')

temperatura_label= Label(root, text='Temperatura: ')
unos_temp_entry = Entry(root)
# command pokrece nesto
ispis_button = Button(root, text='Ispis poruke', command=klikni_gumb)

temperatura_label.grid(row = 0, column= 0, ipadx = 20, ipady = 20)

unos_temp_entry.grid(row = 1, column=1)

ispis_button.grid(row = 1, column=0)


root.mainloop()