from tkinter import *

class Gumb(Button):
    def __init__(self, text, row, col, command, color=None, **kwargs):
        self.text = text
        self.row = row
        self.column = col
        self.command = command
        self.color = color
        super().__init__()
        self['bg'] = self.color
        self['text'] = self.text
        self['command'] = self.command
        self.grid(row=self.row, column=self.column)


def test_gumb():
    print('Gumb je stisnut, radi!')

window = Tk()
window.title("Test Button Class")
window.geometry('400x200')

btn1 = Gumb("Click Me", 0, 0, test_gumb, 'green')
btn2 = Gumb("Click Me2", 0, 1, test_gumb, 'red')

window.mainloop()