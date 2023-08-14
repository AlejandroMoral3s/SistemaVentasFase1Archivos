from tkinter import *
from tkinter import ttk

class Main_menu():

    def __init__(self, root):
        self.root = root
        self.root.title('Sistema de Ventas')
        self.root.geometry('500x200')

        self.menu = Menu(self.root)
        self.root.config(menu = self.menu)

        #Creando Menu Archivo
        self.file = Menu(self.menu, tearoff=0)
        self.file.add_command(label='Clientes')
        self.file.add_command(label='Productos')
        self.file.add_command(label='Usuarios')
        self.file.add_separator()
        self.file.add_command(label='Cambio de Clave')
        self.file.add_command(label='Cambio de Usuario')
        self.file.add_separator()
        self.file.add_command(label='Salir', command=self.salir)

        #Creando Menu Movimientos
        self.movements = Menu(self.menu, tearoff=0)
        self.movements.add_command(label='Nueva Factura')
        self.movements.add_command(label='Reporte de Facturas')

        #Creando Menu Ayuda
        self.help = Menu(self.menu, tearoff=0)
        self.help.add_command(label='Acerca de')
        self.help.add_command(label='Ayuda')

        #Creando las pesatanias del menu

        self.menu.add_cascade(label='ARCHIVO', menu=self.file)
        self.menu.add_cascade(label='MOVIMIENTOS', menu=self.movements)
        self.menu.add_cascade(label='AYUDA', menu = self.help)

    def salir(self):
        self.root.destroy()