from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('ALG-ekipa')

frame1 = Frame(root, bg='light grey', border=3, width=200, height=100)
frame2 = Frame(root, bg='magenta', border=5, width=200, height=75)

label1= Label(frame1, text='Na prvom okviru')
label2 =Label(frame1, text='Na frame1, drugi tekst')

button1 = Button(frame2, text='Bijelo dugme', bg='magenta', fg='white')




frame1.pack(pady=10)
frame2.pack(pady=10)

label1.pack()
label2.pack()
button1.pack()


root.mainloop()