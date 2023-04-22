from tkinter import *

root=Tk()
root.geometry('600x400')
root.title('Alg-ekipa')

frame1=Frame(root, bg='#E8CDF3', bd=10, width=200, height=100)
frame2=Frame(root, bg='#CDD4F3', bd=10, width=200, height=100)

label1=Label(frame1, text='Na frame1', bg='white', fg='black', font=('Verdana', 10))
label2=Label(frame1, text='Dodatni', bg='#E8CDF3', fg='black', font=('Standard', 12))

button1=Button(frame2, text='Klikni me!')

frame1.pack(pady=10)
frame2.pack(pady=10)

label1.pack()
label2.pack()
button1.pack()





root.mainloop()