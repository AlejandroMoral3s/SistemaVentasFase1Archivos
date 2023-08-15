from tkinter import *

class User_Interface(Frame):
    def __init__(self, root):
        super().__init__(root)

        # TITLE
        self.title_Label = Label(self, text='FORMULARIO PARA CREACION DE ')
        self.title_Label.grid(row=0, column=0, columnspan=3)
        self.title_Label.grid_rowconfigure(1, weight=3)
        self.title_Label.grid_columnconfigure(1, weight=1)

        self.title_Label2 = Label(self, text='USUARIOS')
        self.title_Label2.grid(row=1, column=0)

        # ID USER
        self.id_userLabel = Label(self, text='Id Usuario: ')
        self.id_userLabel.grid(row=2, column=0)
        self.id_userEntry = Entry(self)
        self.id_userEntry.grid(row=2, column=1)

        # PROFILE
        self.id_profileLabel = Label(self, text='Perfil: ')
        self.id_profileLabel.grid(row=3, column = 0)

        # NAMES
        self.names_label = Label(self, text='NOMBRES: ')
        self.names_label.grid(row=2, column=2)
