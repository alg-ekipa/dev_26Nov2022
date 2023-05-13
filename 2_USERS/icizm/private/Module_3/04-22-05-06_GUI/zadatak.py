# riješiti zadatak gdje se naprave gumbi koji otvaraju posebno prozore

import tkinter as tk

root = tk.Tk()

root.title('Smart Key')
root.geometry('600x400')


frm_key = tk.Frame(root)
frm_key.grid(row=0, column=0)

lbl_frame_key = tk.LabelFrame(frm_key, text='Key')
lbl_frame_key.columnconfigure((0,1), weight=1, minsize=90)
lbl_frame_key.grid(row=0, column=0, columnspan=2, padx=30, pady=30, ipadx=20, ipady=10)

# Buttons

btn_zvoni=tk.Button(frm_key, text='ZVONO') #command
btn_zvoni.grid(row=0, column=0)

btn_otkljucaj=tk.Button(frm_key, text='OTKLJUČAJ') #command
btn_otkljucaj.grid(row=0, column=1)


root.mainloop()