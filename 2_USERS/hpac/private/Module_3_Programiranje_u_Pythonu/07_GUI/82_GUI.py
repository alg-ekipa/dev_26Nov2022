import tkinter as tk

root = tk.Tk()
root.geometry('600x400')


ime_label = tk.Label(root, text='Ime')
unos_ime_entry = tk.Entry(root)

prezime_label =  tk.Label(root, text='Prezime')
unos_prezime_entry = tk.Entry(root)

ime_label.grid (row=0, column=0)
unos_ime_entry.grid (row=0,column=1)

prezime_label.grid (row=1, column=0)
unos_prezime_entry.grid (row=1, column=1)


root.mainloop()