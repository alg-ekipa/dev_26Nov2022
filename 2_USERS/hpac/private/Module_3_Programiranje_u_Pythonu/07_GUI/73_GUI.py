from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('ALG-ekipa')

frame_naslov = LabelFrame(root, text='Biljke')

dugme = Button(frame_naslov, text='Puce na okviru')
l = Label(frame_naslov, text='Label na okviru')


frame_naslov.grid(row=0, column=0, padx=10, pady=10)
dugme.grid(row=0, column=0, padx=10, pady=10)
l.grid(row=0, column=1, padx=10, pady=10)


root.mainloop()