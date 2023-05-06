from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("Alg-ekipa")

frame1 = Frame(root, bg = "blue", bd=10, width = 100, height = 50)  #bd - znaći border/granica
frame2 = Frame(root, bg = "red", bd=10, width = 100, height = 50)

label1 = Label(frame1, text="Na frame1_prva", bg="blue")
label2 = Label(frame2, text="Na frame1_druga.", bg="green")
button1 = Button(frame2, text="Klikni me")

frame1.pack(pady=10)
frame2.pack(pady=10)

label1.pack()
label2.pack()
button1.pack

root.mainloop()