from tkinter import *
"""TKInter modul ima svoje tipove varijabli:
BoolenVar()
StringVar()
IntVar()
DoubleVar()
"""


root = Tk()
root.title("Algebra by DEV - kalkulator")
root.geometry("600x400")

def get_value():
    ispis_vrijednosti = Label(root, text=mystring.get())
    ispis_vrijednosti.pack()
    

mystring = StringVar()

entry1 = Entry(root, textvariable=mystring, width = 100, fg = "blue", bd = 3)
entry1.pack()

button_submit = Button(root, text="Submit", bg="green", fg = "white", command=get_value)
button_submit.pack()

root.mainloop()