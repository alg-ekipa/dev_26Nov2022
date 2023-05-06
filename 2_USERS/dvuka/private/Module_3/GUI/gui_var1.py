from tkinter import *
'''TKInter modul ima svoje tipove varijabli:
BooleanVar()
StringVar()
IntVar()
DoubleVar()
'''

root=Tk()

root.title('Algebra Py Dev - kalkulator')
root.geometry('600x200')

def get_value():
    #print(mystring.get())
    ispis_vrijednost=Label(root, text=mystring.get())
    ispis_vrijednost.pack()

mystring=StringVar()

entry1=Entry(root, textvariable=mystring, width=100, fg='blue', bd=3, )
entry1.pack()

button_submit=Button(root, text='Submit',bg='green', fg='white', command=get_value )
button_submit.pack()



root.mainloop()