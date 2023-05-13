from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('Alg-ekipa')
# Lableframe - ima neki naslov na sebi

frame_naslov = LabelFrame(root, text= 'Biljke')

b = Button(frame_naslov, text='Gumb na okviru')

l = Label(frame_naslov, text='Label na okviru')

frame_naslov.grid(row=0, column=0, padx=10, pady=10)
b.grid(row=0, column=0, padx=10, pady=10)
l.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()