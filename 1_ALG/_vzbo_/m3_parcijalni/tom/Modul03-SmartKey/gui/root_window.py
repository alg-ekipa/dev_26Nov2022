import tkinter as tk

from .top_frame import TopFrame


class RootWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.ulocked = False
        self.title('Algebra - Smart Key')
        self.geometry('600x600')

        top_frame = TopFrame(self)
        top_frame.pack(padx=10, pady=10, fill='x')

        
