from tkinter import *

root = Tk()
root.geometry('600x600')
root.title('Alg-ekipa')

for i in range(3):
    root.columnconfigure(i, weight=1, minsize=50)
    root.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        ime=Label(root, text=f'{i,j}')
        ime.grid(row=i, column=j, padx=15, pady=15)



root.mainloop()
