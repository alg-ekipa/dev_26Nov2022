from tkinter import *

root=Tk()
root.geometry('600x400')
root.title('Alg-ekipa')

frame1=Frame(root, bg='blue', bd=10, width=200, height=100)
frame2=Frame(root, bg='red', bd=10, width=200, height=100)

label1=Label(frame1, text='Na frame1_prva', bg='blue', fg='white')
label2=Label(frame1, text='Na frame1_druga', bg='blue', fg='white')
button1=Button(frame2, text='Klikni me')

frame1.pack(pady=10)
frame2.pack(pady=10)

label1.pack()
label2.pack()
button1.pack()


root.mainloop()