import tkinter as tk
import random as rd

root = tk.Tk()
root.title("Password generator")

#Prikaz na GUI

frm_postavke = tk.Frame(root)
frm_postavke.grid(row=0, column=0, rowspan=3, columnspan=3)

lbl_frm_postavke = tk.LabelFrame(frm_postavke, text="Postavke")
lbl_frm_postavke.columnconfigure((0,1,2), weight=1, minsize=90)
lbl_frm_postavke.grid(row=0, column=0, columnspan=3, padx=30, pady=30, ipadx=20, ipady=10)





root.mainloop()