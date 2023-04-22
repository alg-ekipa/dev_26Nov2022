from tkinter import *

root = Tk()
root.geometry("600x400")

def klik_gumba():
    print("Vaš unos je potvrđen.")

#šifre boja s stranice html color code

temperatura_label = Label(root, text = "Temparatura: ", background="#33F3FF", foreground="green")
unos_temp_entry = Entry(root)

ispis_button = Button(root, text = "Potvrdi", command=klik_gumba, fg="white", bg="#FF1493")

temperatura_label.grid(row = 0, column=0, padx=10, pady = 10, ipadx = 20, ipady = 20)

unos_temp_entry.grid(row=0, column=1)

ispis_button.grid(row=1, column=0, )

root.mainloop()


