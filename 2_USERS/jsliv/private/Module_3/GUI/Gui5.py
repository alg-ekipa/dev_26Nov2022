from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("Alg-ekipa")

for i in range(3):
    root.columnconfigure(i, weight=1, minsize=50)
    root.rowconfigure(i, weight=1, minsize=50)

    for j in range(3):
        label = Label(root, text=f"{i, j}")
        label.grid(row=i, column=j, pady = 15, padx = 15)




root.mainloop()