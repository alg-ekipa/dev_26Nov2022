from tkinter import *

root=Tk()
root.geometry('600x400')
root.title('Alg-ekipa')

frame_naslov=LabelFrame(root, text='Biljke')

b=Button(frame_naslov, text='Gumb na frame-u')
l=Label(frame_naslov, text='Label na frame-u')

frame_naslov.grid(row=0, column=0, padx=10, pady=10)
b.grid(row=0, column=0, pady=10, padx=10)
l.grid(row=0, column=1, padx=10, pady=10)



root.mainloop()