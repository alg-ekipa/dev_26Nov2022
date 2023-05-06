from tkinter import *

root = Tk()

root.geometry("600x400")

img_py = PhotoImage(file="C:/Users/JulijanaS/Desktop/VisualStudioCode/dev_26Nov2022-1/2_USERS/jsliv/private/Module_3/GUI/python-logo.png").subsample(5)
#ovaj subsample prilagođava veličinu slike

label_poruka = Label(root, text = "Poruka", font = ("Segoe UI", 16))

label_slika = Label(root, text="Pišem po slici",
                    font = ("Segoe UI", 20),
                    compound= CENTER,
                    image = img_py)

label_poruka.pack(pady=10)
label_slika.pack(pady=10)



root.mainloop()