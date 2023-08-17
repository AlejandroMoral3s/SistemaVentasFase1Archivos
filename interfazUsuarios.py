from tkinter import *
from tkinter import ttk
from usuariosList import UsuariosList
from tkinter import messagebox
from interfazCrearUsuarios import Create_user

class User_Interface(Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.metodosUsuarios = UsuariosList()

        self.colorFondo = '#440c29'

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
        self.userNameEntry = Entry(self.root, textvariable=self.temp_userName, state=DISABLED)
        self.userNameEntry.grid(row=1, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # ID USER
        self.id_userLabel = Label(self.root, text='Id Usuario: ', background=self.colorFondo, fg='white')
        self.id_userLabel.grid(row=2, column=0, columnspan=2, sticky='ew', padx=(5,0), pady=(15,15))
        self.id_userEntry = Entry(self.root, textvariable=self.temp_userId, state=DISABLED)
        self.id_userEntry.grid(row=2, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # NAMES
        self.names_label = Label(self.root, text='Nombres: ', background=self.colorFondo, fg='white')
        self.names_label.grid(row=2, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.names_entry = Entry(self.root, textvariable=self.temp_names, state=DISABLED)
        self.names_entry.grid(row=2, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # PROFILE
        self.profileLabel = Label(self.root, text='Perfil: ', background=self.colorFondo, fg='white')
        self.profileLabel.grid(row=3, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.profileCombo = ttk.Combobox(self.root, state='disabled', values=['Administrador', 'Vendedor'], textvariable=self.temp_profile)
        self.profileCombo.grid(row=3, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # LAST NAMES
        self.lastNames_label = Label(self.root, text='Apellidos: ', background=self.colorFondo, fg='white')
        self.lastNames_label.grid(row=3, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.lastNames_entry = Entry(self.root, textvariable=self.temp_lastNames, state=DISABLED)
        self.lastNames_entry.grid(row=3, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))


        # CLAVE
        self.clave_label = Label(self.root, text='Clave: ', background=self.colorFondo, fg='white')
        self.clave_label.grid(row=4, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.clave_entry = Entry(self.root, textvariable=self.temp_pass, state=DISABLED)
        self.clave_entry.grid(row=4, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # CLAVE CONFIRMACION
        self.confir_label = Label(self.root, text='Confirmacion: ', background=self.colorFondo, fg='white')
        self.confir_label.grid(row=4, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.confir_entry = Entry(self.root, textvariable=self.temp_confirPass, state=DISABLED)
        self.confir_entry.grid(row=4, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        #BOTONES DE DESPLAZAMIENTO
        self.first_btn = Button(self.root, text='Primero', command=self.ir_al_primer_registro)
        self.first_btn.grid(row=5, column=0, padx=(10,3), pady=5)

        self.previous_btn = Button(self.root, text='Anterior', command=self.ir_al_registro_anterior)
        self.previous_btn.grid(row=5, column=1, padx=3, pady=5)

        self.next_btn = Button(self.root, text='Siguiente', command=self.ir_al_siguiente_registro)
        self.next_btn.grid(row=5, column=2, padx=3, pady=5)

        self.last_btn = Button(self.root, text='Ultimo', command = self.ir_al_ultimo_registro)
        self.last_btn.grid(row=5, column=3, padx=3, pady=5)

        self.last_btn = Button(self.root, text='Actualizar', command=self.actualizarTabla)
        self.last_btn.grid(row=5, column=4, padx=(3, 10), pady=5)

        #BOTONES DE MANIPULACION DE DATOS

        self.create_btn = Button(self.root, text='Crear', command=self.ventanaCrearUsuario)
        self.create_btn.grid(row=5, column=5, padx=(10, 3), pady=15)

        self.edit_btn = Button(self.root, text='Editar', command=self.editarRegistro)
        self.edit_btn.grid(row=5, column=6, padx=3, pady=15)

        self.save_btn = Button(self.root, text='Guardar', state=DISABLED, command=self.guardarCambios)
        self.save_btn.grid(row=5, column=7, padx=3, pady=15)

        self.delete_btn = Button(self.root, text='Borrar')
        self.delete_btn.grid(row=5, column=8, padx=3, pady=15)

        self.search_btn = Button(self.root, text='Buscar')
        self.search_btn.grid(row=5, column=9, padx=3, pady=15)

        self.cancel_btn = Button(self.root, text='Cancelar', state=DISABLED, command=self.cancelarEdicion)
        self.cancel_btn.grid(row=5, column=10, padx=(3,20), pady=15)

        #INCLUYENDO TABLA

        self.columns = ('user_id','username', 'names', 'last_names', 'profile', 'pass', 'confirmPass')

        self.tree = ttk.Treeview(self.root, columns=self.columns, show='headings')

        self.tree.heading('user_id', text='ID')
        self.tree.heading('username', text='USUARIO')
        self.tree.heading('names', text='NOMBRES')
        self.tree.heading('last_names', text='APELLIDOS')
        self.tree.heading('profile', text='PERFIL')
        self.tree.heading('pass', text='CONTRASEÑA')
        self.tree.heading('confirmPass', text='CONFIRMACION')

        self.tree.column('#1', width=70, anchor='center')
        self.tree.column('#2', width=150, anchor='center')
        self.tree.column('#3', width=150, anchor='center')
        self.tree.column('#4', width=150, anchor='center')
        self.tree.column('#5', width=150, anchor='center')
        self.tree.column('#6', width=150, anchor='center')
        self.tree.column('#7', width=150, anchor='center')


        #Colocando usuarios dentro de la tabla
        self.listadoDict = self.metodosUsuarios.dataJson['users']
        for x in self.listadoDict:
            self.tree.insert('', 'end', values=[x['_Usuario__id'], x['_Usuario__nombreUsuario'], x['_Usuario__nombre'], x['_Usuario__apellido'], x['_Usuario__perfil'], x['_Usuario__clave'], x['_Usuario__confirmacion']])

        self.contadorRegistros = 0
        self.tree.selection_set(self.tree.get_children()[self.contadorRegistros])
        self.tree.focus(self.tree.focus(self.tree.get_children()[self.contadorRegistros]))

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

    def editarRegistro(self):
        self.AsigEntry()

        self.id_userEntry['state'] = DISABLED
        self.userNameEntry['state'] = NORMAL
        self.names_entry['state'] = NORMAL
        self.lastNames_entry['state'] = NORMAL
        self.profileCombo['state'] = NORMAL
        self.clave_entry['state'] = NORMAL
        self.confir_entry['state'] = NORMAL

        self.edit_btn['state'] = DISABLED
        self.save_btn['state'] = NORMAL
        self.cancel_btn['state'] = NORMAL
        
    def guardarCambios(self):
        self.AsigEntry()
        entrysActuales = [self.id_userEntry.get(), self.userNameEntry.get(), self.names_entry.get(), self.lastNames_entry.get(), self.profileCombo.get(), self.clave_entry.get(), self.confir_entry.get()]
        registroActual = self.tree.item(self.tree.selection()[0])['values']
        registroActualStr = []

        for x in registroActual:
            registroActualStr.append(str(x))

        if entrysActuales == registroActualStr:
            messagebox.showinfo('INFORMACION DE EDICION', 'REGISTRO EDITADO CON EXITO, POR FAVOR ACTUALIZAR LA TABLA')

            self.id_userEntry['state'] = NORMAL

            self.id_userEntry.delete(0, END)
            self.userNameEntry.delete(0, END)
            self.names_entry.delete(0, END)
            self.lastNames_entry.delete(0, END)
            self.profileCombo.delete(0, END)
            self.clave_entry.delete(0, END)
            self.confir_entry.delete(0, END)

            self.id_userEntry['state'] = DISABLED
            self.userNameEntry['state'] = DISABLED
            self.names_entry['state'] = DISABLED
            self.lastNames_entry['state'] = DISABLED
            self.profileCombo['state'] = DISABLED
            self.clave_entry['state'] = DISABLED
            self.confir_entry['state'] = DISABLED

            self.edit_btn['state'] = NORMAL
            self.save_btn['state'] = DISABLED
            self.cancel_btn['state'] = DISABLED

        else:

            usernameExists = False
            for x in self.listadoDict:
                if (x['_Usuario__nombreUsuario'] == self.temp_userName.get()) and (x['_Usuario__nombreUsuario'] != registroActualStr[1]):
                    usernameExists = True


            if (self.userNameEntry.get() == '' or self.names_entry.get() == '' or self.profileCombo.get() == '' or self.lastNames_entry.get() == '' or self.clave_entry.get() == '' or self.confir_entry.get() == ''):
                messagebox.showerror(message='Debe llenar todos los campos.', title='ERROR DE EDICION DE USUARIO')
            elif usernameExists:
                messagebox.showerror(title='NOMBRE DE USUARIO INCORRECTO', message='El nombre de usuario ya existe.')
            elif self.temp_pass.get() != self.temp_confirPass.get():
                messagebox.showerror(title='ERROR EN CONTRASEÑA', message='La contraseña y su confimacion, no coinciden.')
            else:
                self.metodosUsuarios.editarUsuario(
                    registroActualStr[1],
                    self.temp_profile.get(),
                    self.temp_names.get(),
                    self.temp_lastNames.get(),
                    self.temp_userName.get(),
                    self.temp_pass.get(),
                    self.temp_confirPass.get())
                
                messagebox.showinfo('INFORMACION DE EDICION', 'REGISTRO EDITADO CON EXITO, POR FAVOR ACTUALIZAR LA TABLA')

                self.id_userEntry['state'] = NORMAL

                self.id_userEntry.delete(0, END)
                self.userNameEntry.delete(0, END)
                self.names_entry.delete(0, END)
                self.lastNames_entry.delete(0, END)
                self.profileCombo.delete(0, END)
                self.clave_entry.delete(0, END)
                self.confir_entry.delete(0, END)

                self.id_userEntry['state'] = DISABLED
                self.userNameEntry['state'] = DISABLED
                self.names_entry['state'] = DISABLED
                self.lastNames_entry['state'] = DISABLED
                self.profileCombo['state'] = DISABLED
                self.clave_entry['state'] = DISABLED
                self.confir_entry['state'] = DISABLED

                self.edit_btn['state'] = NORMAL
                self.save_btn['state'] = DISABLED
                self.cancel_btn['state'] = DISABLED


    def cancelarEdicion(self):

        self.id_userEntry['state'] = NORMAL

        self.id_userEntry.delete(0, END)
        self.userNameEntry.delete(0, END)
        self.names_entry.delete(0, END)
        self.lastNames_entry.delete(0, END)
        self.profileCombo.delete(0, END)
        self.clave_entry.delete(0, END)
        self.confir_entry.delete(0, END)

        self.id_userEntry['state'] = DISABLED
        self.userNameEntry['state'] = DISABLED
        self.names_entry['state'] = DISABLED
        self.lastNames_entry['state'] = DISABLED
        self.profileCombo['state'] = DISABLED
        self.clave_entry['state'] = DISABLED
        self.confir_entry['state'] = DISABLED

        self.save_btn['state'] = DISABLED
        self.cancel_btn['state'] = DISABLED
        self.edit_btn['state'] = NORMAL

    def colocar_informacion_en_campos(self):

        tuplaSeleccion = self.tree.selection()
        atribSelecActual = self.tree.item(tuplaSeleccion[0])['values']

        self.id_userEntry['state'] = NORMAL
        self.userNameEntry['state'] = NORMAL
        self.names_entry['state'] = NORMAL
        self.lastNames_entry['state'] = NORMAL
        self.profileCombo['state'] = NORMAL
        self.clave_entry['state'] = NORMAL
        self.confir_entry['state'] = NORMAL

        self.id_userEntry.delete(0, END)
        self.userNameEntry.delete(0, END)
        self.names_entry.delete(0, END)
        self.lastNames_entry.delete(0, END)
        self.profileCombo.delete(0, END)
        self.clave_entry.delete(0, END)
        self.confir_entry.delete(0, END)

        self.id_userEntry.insert(0, atribSelecActual[0])
        self.userNameEntry.insert(0, atribSelecActual[1])
        self.names_entry.insert(0, atribSelecActual[2])
        self.lastNames_entry.insert(0, atribSelecActual[3])
        self.profileCombo.insert(0, atribSelecActual[4])
        self.clave_entry.insert(0, atribSelecActual[5])
        self.confir_entry.insert(0, atribSelecActual[6])

        self.id_userEntry['state'] = DISABLED
        self.userNameEntry['state'] = DISABLED
        self.names_entry['state'] = DISABLED
        self.lastNames_entry['state'] = DISABLED
        self.profileCombo['state'] = DISABLED
        self.clave_entry['state'] = DISABLED
        self.confir_entry['state'] = DISABLED

    def ir_al_primer_registro(self):
        
        ids = self.tree.get_children()
        self.contadorRegistros = 0
        self.tree.selection_set(ids[0])
        self.tree.focus(ids[0])
        self.colocar_informacion_en_campos()

    def ir_al_siguiente_registro(self):
        
        ids = self.tree.get_children()

        if ids[self.contadorRegistros] != ids[-1]:
            self.contadorRegistros+=1
            self.tree.selection_set(ids[self.contadorRegistros])
            self.tree.focus(ids[self.contadorRegistros])
        else:
            self.contadorRegistros = 0
            self.tree.selection_set(ids[self.contadorRegistros])
            self.tree.focus(ids[self.contadorRegistros])

        self.colocar_informacion_en_campos()

    def ir_al_registro_anterior(self):

        ids = self.tree.get_children()

        if ids[self.contadorRegistros] != ids[0]:
            self.contadorRegistros-=1
            self.tree.selection_set(ids[self.contadorRegistros])
            self.tree.focus(ids[self.contadorRegistros])
        else:
            self.contadorRegistros = self.tree.index(ids[-1])
            self.tree.selection_set(ids[self.contadorRegistros])
            self.tree.focus(ids[self.contadorRegistros])

        self.colocar_informacion_en_campos()

    def ir_al_ultimo_registro(self):
        ids = self.tree.get_children()
        self.contadorRegistros = self.tree.index(ids[-1])
        self.tree.selection_set(ids[-1])
        self.tree.focus(ids[-1])

        self.colocar_informacion_en_campos()

    def ventanaCrearUsuario(self):
        root = Tk()
        Create_user(root)
        root.mainloop()

    def actualizarTabla(self):
        self.metodosUsuarios = UsuariosList()
        self.listadoDict = self.metodosUsuarios.dataJson['users']

        for i in self.tree.get_children():
            self.tree.delete(i)
        for x in self.listadoDict:
            self.tree.insert('', 'end', values=[x['_Usuario__id'], x['_Usuario__nombreUsuario'], x['_Usuario__nombre'], x['_Usuario__apellido'], x['_Usuario__perfil'], x['_Usuario__clave'], x['_Usuario__confirmacion']])
        
root = Tk()
User_Interface(root)
root.mainloop()