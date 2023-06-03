import tkinter as tk
from tkinter.messagebox import showinfo

from .middle_frame import MiddleFrame


class TopFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=6)

        #region WIDGETS
        self.label = tk.Label(self, text='Dobro dosli!', font=('Segoe UI', '20', 'bold'))
        self.label.grid(**options, sticky=tk.N, row=0, column=0, columnspan=5)

        # button
        self.btn_pozvoni = tk.Button(self, text='Pozvoni', bg='#5bc0de', fg='#000', font='bold')
        self.btn_pozvoni['command'] = self.button_clicked
        self.btn_pozvoni.grid(**options, ipadx=20, ipady=10, sticky=tk.W, row=1, column=0)

        self.btn_otkljucaj = tk.Button(self, text='Otkljucaj', bg='#5cb85c', fg='#000', font='bold')
        self.btn_otkljucaj['command'] = self.activate_middle_frame
        self.btn_otkljucaj.grid(**options, ipadx=20, ipady=10, sticky=tk.E, row=1, column=4)


        self.mid_frame = MiddleFrame(self)

        self.mid_frame_blank = tk.Frame(self)
        self.mid_frame_blank.grid(**options, sticky=tk.EW, row=2, column=0, columnspan=5)

        #endregion

    #region METHODS
    def button_clicked(self):
        showinfo(title='Information',
                 message='Zvono je aktivirano!\nNetko će uskoro doći i otvoriti vrata!')


    def activate_middle_frame(self):
        self.mid_frame.grid(padx=5, pady=5, sticky=tk.EW, row=2, column=0, columnspan=5)
        self.mid_frame.tkraise()


    def deactivate_middle_frame(self):
        self.mid_frame_blank.tkraise()

    #endregion
