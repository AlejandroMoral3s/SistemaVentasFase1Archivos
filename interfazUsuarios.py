from tkinter import *
from tkinter import ttk
from usuariosList import UsuariosList
from tkinter import messagebox

class User_Interface(Frame):
    def __init__(self, root):
        super().__init__(root)
        
        metodosUsuarios = UsuariosList()

        self.colorFondo = '#440c29'
        self.noId = 0

        self.root = root
        self.root.title('INTERFAZ DE USUARIOS')
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
        self.id_userEntry = Entry(self.root, textvariable=self.temp_userId, state=DISABLED)
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

        #BOTONES DE DESPLAZAMIENTO
        self.first_btn = Button(self.root, text='Primero')
        self.first_btn.grid(row=5, column=0, padx=(25,5), pady=5)

        self.previous_btn = Button(self.root, text='Anterior')
        self.previous_btn.grid(row=5, column=1, padx=5, pady=5)

        self.next_btn = Button(self.root, text='Siguiente')
        self.next_btn.grid(row=5, column=2, padx=5, pady=5)

        self.last_btn = Button(self.root, text='Ultimo')
        self.last_btn.grid(row=5, column=3, padx=(5, 15), pady=5)

        #BOTONES DE MANIPULACION DE DATOS

        self.create_btn = Button(self.root, text='Crear', command=self.createUser)
        self.create_btn.grid(row=5, column=4, padx=(35, 5), pady=15)

        self.edit_btn = Button(self.root, text='Editar')
        self.edit_btn.grid(row=5, column=5, padx=5, pady=15)

        self.save_btn = Button(self.root, text='Guardar')
        self.save_btn.grid(row=5, column=6, padx=5, pady=15)

        self.delete_btn = Button(self.root, text='Borrar')
        self.delete_btn.grid(row=5, column=7, padx=5, pady=15)

        self.search_btn = Button(self.root, text='Buscar')
        self.search_btn.grid(row=5, column=8, padx=5, pady=15)

        self.cancel_btn = Button(self.root, text='Cancelar')
        self.cancel_btn.grid(row=5, column=9, padx=(5,50), pady=15)

        #INCLUYENDO TABLA

        self.columns = ('user_id','username', 'names', 'last_names', 'profile')

        self.tree = ttk.Treeview(self.root, columns=self.columns, show='headings')

        self.tree.heading('user_id', text='ID')
        self.tree.heading('username', text='USUARIO')
        self.tree.heading('names', text='NOMBRES')
        self.tree.heading('last_names', text='APELLIDOS')
        self.tree.heading('profile', text='PERFIL')

        #Colocando usuarios dentro de la tabla
        listadoDict = metodosUsuarios.dataJson['users']
        for x in listadoDict:
            self.tree.insert('', 'end', values=[x['_Usuario__id'], x['_Usuario__username'], x['_Usuario__nombre'], x['_Usuario__apellido'], x['_Usuario__perfil']])

        self.tree.grid(row=6, column=0, columnspan=10, padx=15, pady=15)

        #Creando un scrollbar vertical para desplazarse en la tabla
        self.verScrol = ttk.Scrollbar(self.root, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.verScrol.set)
        self.verScrol.grid(row=6, column=10, sticky='ns', padx=10)
        
    def AsigEntry(self):
        self.temp_userId.set(self.id_userEntry.get())
        self.temp_userName.set(self.userNameEntry.get())
        self.temp_names.set(self.names_entry.get())
        self.temp_profile.set(self.profileCombo.get())
        self.temp_lastNames.set(self.lastNames_entry.get())
        self.temp_pass.set(self.clave_entry.get())
        self.temp_confirPass.set(self.confir_entry.get())

    #en proceso
    def createUser(self):
        self.AsigEntry()
        
        if (self.userNameEntry.get() == '' or self.names_entry.get() == '' or self.profileCombo.get() == '' or self.lastNames_entry.get() == '' or self.clave_entry.get() == '' or self.confir_entry.get() == ''):
            messagebox.showerror(message='DEBE LLENAR CADA CAMPO SOLICITADO', title='ERROR DE CREACION DE USUARIO')
        elif

        



    def prueba(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
         

