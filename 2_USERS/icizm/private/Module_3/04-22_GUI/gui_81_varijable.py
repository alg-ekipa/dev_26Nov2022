''' TkInter ima svoje tipove varijabli : 
BooleanVar()
StringVar()
IntVar()
DoubleVar()
'''

from tkinter import *

root = Tk()

root.title('Algebra Py DEV - upisivanje teksta')
root.geometry('600x400')

def get_value(): 
    # print(mystring.get()) #ispisuje u konzolu
    ispis_vrijednost = Label(root, text=mystring.get())
    ispis_vrijednost.pack()

mystring = StringVar()

entry1 = Entry(root, textvariable=mystring, width=100, fg='blue', bd=3) 
# stavljen veliki width jer želimo neki string koji može biti i dugačak
# textvariable - prenosi uneseni string u varijablu
entry1.pack() #da bude na sredini

button_submit = Button(root, text='Submit', bg='green', fg='white', command=get_value)
button_submit.pack()



root.mainloop()