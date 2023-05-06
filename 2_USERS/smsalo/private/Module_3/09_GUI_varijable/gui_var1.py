''' TKInter modul ima svoje tipove varijabli:
BooleanVar()
StringVar()
IntVar()
Doublevar()
'''

from tkinter import *

root=Tk()
root.geometry('300x200')
root.title('Alg-ekipa')

def get_value():
    #print(mystring.get())          ispis u terminalu
    ispis_vrijednost=Label(root, text=mystring.get())
    ispis_vrijednost.pack()


mystring=StringVar()

entry_1=Entry(root, textvariable=mystring, width=100, fg='blue', bd=3)      #povezivanje varijable i mjesta
entry_1.pack()

button_submit=Button(root, text='Submit', bg='green', fg='white', command=get_value)
button_submit.pack()

root.mainloop()