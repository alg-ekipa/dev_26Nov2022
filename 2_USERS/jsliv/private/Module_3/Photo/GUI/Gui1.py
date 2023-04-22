import tkinter as tk

rootWindow = tk.Tk()
rootWindow.geometry("600x400")
rootWindow.title("Algebra - PyDev")


#tk.Button(rootWindow, text="Sad znam i ja! :P").pack()

#kreiranje widget labela
myLabel1 =tk.Label(rootWindow, text = "Olaaa :)")
myLabel2 = tk.Label(rootWindow, text="Saturday")

#myLabel1.pack(pady=30)
#myLabel2.pack()

#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=1)

myLabel1.place(x=100, y=50)
myLabel2.place(x=150, y=150)

rootWindow.mainloop()

