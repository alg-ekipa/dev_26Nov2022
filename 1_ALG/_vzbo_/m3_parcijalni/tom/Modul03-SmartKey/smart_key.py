from gui import RootWindow as App
from data import create_tables


if __name__ == "__main__":
    create_tables()
    app = App()    
    app.mainloop()
