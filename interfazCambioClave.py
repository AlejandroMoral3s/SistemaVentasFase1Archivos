from tkinter import *
from usuariosList import UsuariosList
from tkinter import messagebox

class Cambio_Clave_Interfaz(Frame):

    def __init__(self, root, username):
        
        self.root = root
        #self.userActual = username
        self.userActual = username

        self.root.title('CAMBIO DE CLAVE')
        self.colorFondo= '#491AD9'
        self.root.config(bg=self.colorFondo)

        self.metodosUsuarios = UsuariosList()

        self.diccUsuarios = self.metodosUsuarios.dataJson['users']

        self.claveActual_label = Label(self.root, text='Clave Actual: ', fg='white', font=('Times'), bg=self.colorFondo)
        self.claveActual_label.grid(row=0, column=0, padx=15, pady=15)

        self.claveActual_entry = Entry(self.root, show="*")
        self.claveActual_entry.grid(row=0, column=1, padx=(0, 15))

        self.nuevaClave_label = Label(self.root, text='Nueva Clave: ', fg='white', font=('Times'), bg=self.colorFondo)
        self.nuevaClave_label.grid(row=1, column=0, padx=15, pady=15)

        self.nuevaClave_entry = Entry(self.root, show="*")
        self.nuevaClave_entry.grid(row=1, column=1, padx=(0, 15))

        self.confirmacion_label = Label(self.root, text='Confirmacion: ', fg='white', font=('Times'), bg=self.colorFondo)
        self.confirmacion_label.grid(row=2, column=0, padx=15, pady=15)

        self.confirmacion_entry = Entry(self.root, show="*")
        self.confirmacion_entry.grid(row=2, column=1, padx=(0, 15))

        
        self.Aceptar_btn = Button(self.root, text='ACEPTAR', bg='green', fg='white', command=self.AceptarFunct)
        self.Aceptar_btn.grid(row=3, column=0, padx=15, pady=15)

        self.Cancelar_btn =Button(self.root, text='CANCELAR', bg='red', fg='white', command=self.root.destroy)
        self.Cancelar_btn.grid(row=3, column=1, padx=15, pady=15)


    def AceptarFunct(self):

        passArchivo = ''

        for usuario in self.diccUsuarios:
            if usuario['_Usuario__nombreUsuario'] == self.userActual:
                passArchivo = usuario['_Usuario__clave']

        if self.claveActual_entry.get() == '' or self.nuevaClave_entry.get()=='' or self.confirmacion_entry.get()=='':
            messagebox.showerror('ERROR CAMBIO DE CLAVE', 'Debe llenar todos los campos solicitados.')
        elif self.nuevaClave_entry.get() != self.confirmacion_entry.get():
            messagebox.showerror('ERROR EN CAMBIO DE CLAVE', 'La nueva contraseña y su confirmacion, deben coincidir.')
        elif self.claveActual_entry.get() != passArchivo:
            messagebox.showerror('ERROR EN CAMBIO DE CLAVE', 'La clave actual es incorrecta.')
        else:
            for usuario in self.diccUsuarios:
                if usuario['_Usuario__nombreUsuario'] == self.userActual:
                    if usuario['_Usuario__clave'] == self.claveActual_entry.get():
                        self.metodosUsuarios.cambiarClaveUsuario(self.userActual, self.nuevaClave_entry.get(), self.confirmacion_entry.get())
                        messagebox.showinfo('CAMBIO DE CLAVE', 'El cambio de clave fue aplicado satisfactoriamente.')
                        self.root.destroy()
