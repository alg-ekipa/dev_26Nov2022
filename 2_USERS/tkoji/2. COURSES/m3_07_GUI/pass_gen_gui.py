import tkinter as tk
import random as rd

root = tk.Tk()
root.title('Password generator')    

frame_settings = tk.Frame(root)
frame_settings.grid(row = 0, column=0, rowspan=3, columnspan=3)

label_frame_settings = tk.LabelFrame(frame_settings, text='Settings')
label_frame_settings.columnconfigure((0,1,2), weight=1, minsize=90)
label_frame_settings.grid(row=0, column=0, columnspan=3, padx=30, pady=30,ipadx=20, ipady=10)

ch_box_letters = tk.Checkbutton(label_frame_settings, text='Just letters')
ch_box_letters.grid(row=0, column=0)

ch_box_numbers = tk.Checkbutton(label_frame_settings, text='Just numbers')
ch_box_numbers.grid(row=0, column=1)
                    
ch_box_special = tk.Checkbutton(label_frame_settings, text='Just specials')
ch_box_special.grid(row=0, column=2)

rb_show_password = tk.Radiobutton(label_frame_settings, text='Show generated password')
rb_show_password.grid(row=1, column=0)

rb_hide_password = tk.Radiobutton(label_frame_settings, text='Hide generated password')
rb_hide_password.grid(row=1, column=2)

slider_length = tk.Scale(label_frame_settings, orient='horizontal', length=350, from_ = 8, to=40)
slider_length.grid(row=2, column=0, columnspan=3)

# FRAME ACTION BUTTONS


# FRAME SHOW PASSWORD


root.mainloop()