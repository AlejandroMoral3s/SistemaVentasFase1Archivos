from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from usuariosList import UsuariosList

class Create_user(Frame):

    def __init__(self, root):
        super().__init__(root)

        self.metodosUsuarios = UsuariosList()
        

        self.root = root
        self.colorFondo = '#440c29'
        self.root.configure(bg=self.colorFondo)

        #Creando variables temporales
        self.temp_userName = StringVar()
        self.temp_userId = StringVar()
        self.temp_names = StringVar()
        self.temp_profile = StringVar()
        self.temp_lastNames = StringVar()
        self.temp_pass = StringVar()
        self.temp_confirPass = StringVar()

        # TITLE
        self.title_Label = Label(self.root, text='FORMULARIO PARA CREACION DE USUARIOS ', background=self.colorFondo, fg='white')
        self.title_Label.grid(row=0, column=0, columnspan=10)

        self.userNameLabel = Label(self.root, text='Usuario: ', background=self.colorFondo, fg='white')
        self.userNameLabel.grid(row=1, column=0, columnspan=2, sticky='ew', padx=(5,0), pady=(15,15))
        self.userNameEntry = Entry(self.root, textvariable=self.temp_userName)
        self.userNameEntry.grid(row=1, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # ID USER
        self.id_userLabel = Label(self.root, text='Id Usuario: ', background=self.colorFondo, fg='white')
        self.id_userLabel.grid(row=2, column=0, columnspan=2, sticky='ew', padx=(5,0), pady=(15,15))
        self.id_userEntry = Entry(self.root, textvariable=self.temp_userId)
        self.id_userEntry.grid(row=2, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # NAMES
        self.names_label = Label(self.root, text='Nombres: ', background=self.colorFondo, fg='white')
        self.names_label.grid(row=2, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.names_entry = Entry(self.root, textvariable=self.temp_names)
        self.names_entry.grid(row=2, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))


        # PROFILE
        self.profileLabel = Label(self.root, text='Perfil: ', background=self.colorFondo, fg='white')
        self.profileLabel.grid(row=3, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.profileCombo = ttk.Combobox(self.root, state='readonly', values=['Administrador', 'Vendedor'], textvariable=self.temp_profile)
        self.profileCombo.grid(row=3, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # LAST NAMES
        self.lastNames_label = Label(self.root, text='Apellidos: ', background=self.colorFondo, fg='white')
        self.lastNames_label.grid(row=3, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.lastNames_entry = Entry(self.root, textvariable=self.temp_lastNames)
        self.lastNames_entry.grid(row=3, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))


        # CLAVE
        self.clave_label = Label(self.root, text='Clave: ', background=self.colorFondo, fg='white')
        self.clave_label.grid(row=4, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.clave_entry = Entry(self.root, textvariable=self.temp_pass)
        self.clave_entry.grid(row=4, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # CLAVE CONFIRMACION
        self.confir_label = Label(self.root, text='Confirmacion: ', background=self.colorFondo, fg='white')
        self.confir_label.grid(row=4, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.confir_entry = Entry(self.root, textvariable=self.temp_confirPass)
        self.confir_entry.grid(row=4, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        self.listadoDict = self.metodosUsuarios.dataJson['users']

        #BOTONES DE DESPLAZAMIENTO
        self.first_btn = Button(self.root, text='CREAR USUARIO', command=self.createUser)
        self.first_btn.grid(row=5, column=0, columnspan=5, padx=(25,5), pady=5)

        self.previous_btn = Button(self.root, text='CANCELAR', command=self.root.destroy)
        self.previous_btn.grid(row=5, column=5,columnspan=5, padx=5, pady=5)

    def AsigEntry(self):
        self.temp_userId.set(self.id_userEntry.get())
        self.temp_userName.set(self.userNameEntry.get())
        self.temp_names.set(self.names_entry.get())
        self.temp_profile.set(self.profileCombo.get())
        self.temp_lastNames.set(self.lastNames_entry.get())
        self.temp_pass.set(self.clave_entry.get())
        self.temp_confirPass.set(self.confir_entry.get())

    def createUser(self):
        self.AsigEntry()

        if (self.userNameEntry.get() == '' or self.names_entry.get() == '' or self.profileCombo.get() == '' or self.lastNames_entry.get() == '' or self.clave_entry.get() == '' or self.confir_entry.get() == ''):
            messagebox.showerror(message='DEBE LLENAR CADA CAMPO SOLICITADO', title='ERROR DE CREACION DE USUARIO')
        else:
            userExists = False
            idExists = False
            for x in self.listadoDict:
                if x['_Usuario__nombreUsuario'] == self.temp_userName.get():
                    userExists = True

                if x['_Usuario__id'] == int(self.temp_userId.get()):
                    idExists = True
            
            if userExists:
                messagebox.showerror(message='El NOMBRE de usuario ya existe.', title='USUARIO NO VALIDO')
            elif idExists:
                messagebox.showerror(message='El ID de usuario ya existe.', title='ID NO VALIDO')
            elif self.temp_pass.get() != self.temp_confirPass.get():
                messagebox.showerror(message='La contraseña y la confirmacion no coinciden.', title='ERROR DE CONTRASEÑA')
            else:
                self.metodosUsuarios.crearUsuario(
                    int(self.temp_userId.get()),
                    self.temp_profile.get(),
                    self.temp_names.get(),
                    self.temp_lastNames.get(),
                    self.temp_userName.get(),
                    self.temp_pass.get(),
                    self.temp_confirPass.get())
                messagebox.showinfo(message='USUARIO CREADO CON EXITO!', title='INFORMACION')
                self.root.destroy()