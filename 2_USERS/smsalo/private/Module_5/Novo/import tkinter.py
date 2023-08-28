import tkinter
import customtkinter  # <- import the CustomTkinter module


customtkinter.set_appearance_mode("System")

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x240")
root_tk.title("CustomTkinter Test")

'''def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)'''



def button_event():
    print("button pressed")

button = customtkinter.CTkButton(master=root_tk,
                                 text="CTkButton",
                                 command=button_event,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
           
root_tk.mainloop()

customtkinter.disable_macos_darkmode()