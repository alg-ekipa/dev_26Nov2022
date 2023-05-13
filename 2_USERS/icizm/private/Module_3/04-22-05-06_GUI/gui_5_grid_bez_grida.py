from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('Alg-ekipa')

# kad si želimo napraviti mrežu možemo to napraviti i bez grida rowconfigure i columnconfigure - 2d matrica 3x3 

for i in range(3): 
    root.columnconfigure(i, weight=1, minsize=50) # weight je debljina crte
    root.rowconfigure(i, weight=1, minsize=50) 

    for j in range(3): 
        label = Label(root, text = f'{i}, {j}') # pokazuje nam gdje se nalazi koja kućica
        label.grid(row=i, column=j, pady=15, padx=15) 


root.mainloop()