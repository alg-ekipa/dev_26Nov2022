from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('Alg-ekipa')

frame1 = Frame(root, bg='green', bd=10, width=200, height=100)
frame2 = Frame(root, bg='black', bd=10, width=200, height=100)

label1 = Label(frame1, text='Ja sam zelen label', bg='green', fg='white')
label2 = Label(frame1, text='Ja sam isto zelen label', bg='yellow', fg='green')
button1 = Button(frame2, text = 'Klikni me!', bg='yellow')

frame1.pack(pady=10)
frame2.pack(pady=10)

label1.pack()
label2.pack()
button1.pack()


root.mainloop()