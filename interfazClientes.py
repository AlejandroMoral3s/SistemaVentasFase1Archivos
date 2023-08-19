from tkinter import *
from tkinter import ttk
from clientesList import ClientesList
from interfazCrearClientes import Create_client
from tkinter import messagebox
from tkcalendar import DateEntry

class Client_Interface(Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.metodosClientes = ClientesList()

        self.colorFondo = '#695AD6'

        self.root = root
        self.root.title('INTERFAZ DE CLIENTES')
        self.root.configure(bg=self.colorFondo)

        #Creando variables temporales
        self.temp_clientId = StringVar()
        self.temp_idType = StringVar()
        self.temp_noId = StringVar()
        self.temp_names = StringVar()
        self.temp_lastNames = StringVar()
        self.temp_adress = StringVar()
        self.temp_phone = StringVar()
        self.temp_city = StringVar()
        self.temp_nacDate = StringVar()
        self.temp_ingDate = StringVar()

        self.temp_BuscarUser = StringVar()

        # TITLE
        self.title_Label = Label(self.root, text='FORMULARIO PARA CREACION DE CLIENTES', background=self.colorFondo, fg='white')
        self.title_Label.grid(row=0, column=0, columnspan=10)

        # ID CLIENTE
        self.id_Label = Label(self.root, text='Id Cliente: ', background=self.colorFondo, fg='white')
        self.id_Label.grid(row=1, column=0, columnspan=2, sticky='ew', padx=(5,0), pady=(15,15))
        self.idEntry = Entry(self.root, textvariable=self.temp_clientId, state=DISABLED)
        self.idEntry.grid(row=1, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # TIPO IDENTIFICACION
        self.idType_label = Label(self.root, text='Tipo Identificacion: ', background=self.colorFondo, fg='white')
        self.idType_label.grid(row=1, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.idType_entry = ttk.Combobox(self.root, values=['DPI', 'PASAPORTE'], textvariable=self.temp_idType, state=DISABLED)
        self.idType_entry.grid(row=1, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # NO. IDENTIFICACION
        self.noId_Label = Label(self.root, text='No. Identificacion: ', background=self.colorFondo, fg='white')
        self.noId_Label.grid(row=2, column=0, columnspan=2, sticky='ew', padx=(5,0), pady=(15,15))
        self.noId_Entry = Entry(self.root, textvariable=self.temp_noId, state=DISABLED)
        self.noId_Entry.grid(row=2, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # NOMBRES
        self.names_label = Label(self.root, text='Nombres: ', background=self.colorFondo, fg='white')
        self.names_label.grid(row=2, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.names_entry = Entry(self.root, textvariable=self.temp_names, state=DISABLED)
        self.names_entry.grid(row=2, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # APELLIDO
        self.lastNames_label = Label(self.root, text='Apellidos: ', background=self.colorFondo, fg='white')
        self.lastNames_label.grid(row=3, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.lastNames_entry = Entry(self.root, state='disabled', textvariable=self.temp_lastNames)
        self.lastNames_entry.grid(row=3, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # DIRECCION
        self.adress_label = Label(self.root, text='Direccion: ', background=self.colorFondo, fg='white')
        self.adress_label.grid(row=3, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.adress_entry = Entry(self.root, textvariable=self.temp_adress, state=DISABLED)
        self.adress_entry.grid(row=3, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # TELEFONO
        self.phone_label = Label(self.root, text='Telefono: ', background=self.colorFondo, fg='white')
        self.phone_label.grid(row=4, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.phone_entry = Entry(self.root, textvariable=self.temp_phone, state=DISABLED)
        self.phone_entry.grid(row=4, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # CIUDAD
        self.city_label = Label(self.root, text='Ciudad: ', background=self.colorFondo, fg='white')
        self.city_label.grid(row=4, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.city_entry = ttk.Combobox(self.root, values=['Coban', 'Tactic', 'Chamelco', 'Carchá'], textvariable=self.temp_city, state=DISABLED)
        self.city_entry.grid(row=4, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # FECHA DE NACIMIENTO
        self.nacDate_label = Label(self.root, text='Fecha de Nacimiento: ', background=self.colorFondo, fg='white')
        self.nacDate_label.grid(row=5, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.nacDate_entry = DateEntry(self.root, textvariable=self.temp_nacDate, state=DISABLED)
        self.nacDate_entry.grid(row=5, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # FECHA DE INGRESO
        self.ingDate_label = Label(self.root, text='Fecha de Ingreso: ', background=self.colorFondo, fg='white')
        self.ingDate_label.grid(row=5, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.ingDate_entry = DateEntry(self.root, textvariable=self.temp_ingDate, state=DISABLED)
        self.ingDate_entry.grid(row=5, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        #OPCIONES BUSCAR

        self.buscar_label = Label(self.root, text='Ingresar No.Identificacion: ', background=self.colorFondo, fg='white')
        self.buscar_label.grid(row=7, column=0, columnspan=3, pady=20, sticky='e')
        self.buscar_entry = Entry(self.root, textvariable=self.temp_BuscarUser)
        self.buscar_entry.grid(row=7, column=4, columnspan=4, pady=20, sticky='w')
        self.buscar_btn = Button(self.root, text='BUSCAR REGISTRO', command=self.buscarRegistro)
        self.buscar_btn.grid(row=7, column=7, columnspan=3, pady=20, sticky='w')

        #BOTONES DE DESPLAZAMIENTO
        self.first_btn = Button(self.root, text='Primero', command=self.ir_al_primer_registro)
        self.first_btn.grid(row=6, column=0, padx=(10,3), pady=5)

        self.previous_btn = Button(self.root, text='Anterior', command=self.ir_al_registro_anterior)
        self.previous_btn.grid(row=6, column=1, padx=3, pady=5)

        self.next_btn = Button(self.root, text='Siguiente', command=self.ir_al_siguiente_registro)
        self.next_btn.grid(row=6, column=2, padx=3, pady=5)

        self.last_btn = Button(self.root, text='Ultimo', command = self.ir_al_ultimo_registro)
        self.last_btn.grid(row=6, column=3, padx=3, pady=5)

        self.last_btn = Button(self.root, text='Actualizar', command=self.actualizarTabla)
        self.last_btn.grid(row=6, column=4, padx=(3, 10), pady=5)

        #BOTONES DE MANIPULACION DE DATOS

        self.create_btn = Button(self.root, text='Crear', command=self.ventanaCrearCliente)
        self.create_btn.grid(row=6, column=5, padx=(10, 3), pady=15)

        self.edit_btn = Button(self.root, text='Editar', command=self.editarRegistro)
        self.edit_btn.grid(row=6, column=6, padx=3, pady=15)

        self.save_btn = Button(self.root, text='Guardar', state=DISABLED, command=self.guardarCambios)
        self.save_btn.grid(row=6, column=7, padx=3, pady=15)

        self.delete_btn = Button(self.root, text='Borrar', command=self.eliminarRegistro)
        self.delete_btn.grid(row=6, column=8, padx=3, pady=15)

        self.cancel_btn = Button(self.root, text='Cancelar', state=DISABLED, command=self.cancelarEdicion)
        self.cancel_btn.grid(row=6, column=9, padx=(3,20), pady=15)

        #INCLUYENDO TABLA

        self.columns = ('client_id','id_type', 'no_id', 'names', 'last_names','direction', 'phone', 'city', 'nac_date', 'ing_date')

        self.tree = ttk.Treeview(self.root, columns=self.columns, show='headings')

        self.tree.heading('client_id', text='ID')
        self.tree.heading('id_type', text='TIPO_ID')
        self.tree.heading('no_id', text='NO_ID')
        self.tree.heading('names', text='NOMBRES')
        self.tree.heading('last_names', text='APELLIDOS')
        self.tree.heading('direction', text='DIRECCION')
        self.tree.heading('phone', text='TELEFONO')
        self.tree.heading('city', text='CIUDAD')
        self.tree.heading('nac_date', text='F_NACIMIENTO')
        self.tree.heading('ing_date', text='F_INGRESO')

        self.tree.column('#1', width=70, anchor='center')
        self.tree.column('#2', width=100, anchor='center')
        self.tree.column('#3', width=100, anchor='center')
        self.tree.column('#4', width=150, anchor='center')
        self.tree.column('#5', width=150, anchor='center')
        self.tree.column('#6', width=100, anchor='center')
        self.tree.column('#7', width=100, anchor='center')
        self.tree.column('#8', width=100, anchor='center')
        self.tree.column('#9', width=100, anchor='center')
        self.tree.column('#10', width=100, anchor='center')

        #Colocando usuarios dentro de la tabla
        self.listadoDict = self.metodosClientes.dataJson['clients']
        
        for x in self.listadoDict:
            self.tree.insert('', 'end', 
                values=[
                    x['_Cliente__id'], 
                    x['_Cliente__tipoDocumento'], 
                    x['_Cliente__noDocumento'], 
                    x['_Cliente__nombre'], 
                    x['_Cliente__apellido'], 
                    x['_Cliente__direccion'], 
                    x['_Cliente__telefono'], 
                    x['_Cliente__ciudad'], 
                    x['_Cliente__fechaNac'], 
                    x['_Cliente__fechaIng']])

        self.contadorRegistros = 0
        self.tree.selection_set(self.tree.get_children()[self.contadorRegistros])
        self.tree.focus(self.tree.focus(self.tree.get_children()[self.contadorRegistros]))

        self.tree.grid(row=8, column=0, columnspan=10, padx=15, pady=15)

        #Creando un scrollbar vertical para desplazarse en la tabla
        self.verScrol = ttk.Scrollbar(self.root, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.verScrol.set)
        self.verScrol.grid(row=8, column=10, sticky='ns', padx=10)
        

    def AsigEntry(self):
        self.temp_clientId.set(self.idEntry.get())
        self.temp_idType.set(self.idType_entry.get())
        self.temp_noId.set(self.noId_Entry.get())
        self.temp_names.set(self.names_entry.get())
        self.temp_lastNames.set(self.lastNames_entry.get())
        self.temp_adress.set(self.adress_entry.get())
        self.temp_phone.set(self.phone_entry.get())
        self.temp_city.set(self.city_entry.get())
        self.temp_nacDate.set(self.nacDate_entry.get())
        self.temp_ingDate.set(self.ingDate_entry.get())
        self.temp_BuscarUser.set(self.buscar_entry.get())

    def EliminarEntrys(self):
        self.idEntry.delete(0, END)
        self.idType_entry.delete(0, END)
        self.noId_Entry.delete(0, END)
        self.names_entry.delete(0, END)
        self.lastNames_entry.delete(0, END)
        self.adress_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.nacDate_entry.delete(0, END)
        self.ingDate_entry.delete(0, END)

    def DesactivarEntrys(self):
        self.idEntry['state'] = DISABLED
        self.idType_entry['state'] = DISABLED
        self.noId_Entry['state'] = DISABLED
        self.names_entry['state'] = DISABLED
        self.lastNames_entry['state'] = DISABLED
        self.adress_entry['state'] = DISABLED
        self.phone_entry['state'] = DISABLED
        self.city_entry['state'] = DISABLED
        self.nacDate_entry['state'] = DISABLED
        self.ingDate_entry['state'] = DISABLED

    def ActivarEntrys(self):
        self.idEntry['state'] = NORMAL
        self.idType_entry['state'] = NORMAL
        self.noId_Entry['state'] = NORMAL
        self.names_entry['state'] = NORMAL
        self.lastNames_entry['state'] = NORMAL
        self.adress_entry['state'] = NORMAL
        self.phone_entry['state'] = NORMAL
        self.city_entry['state'] = NORMAL
        self.nacDate_entry['state'] = NORMAL
        self.ingDate_entry['state'] = NORMAL



    def editarRegistro(self):
        self.AsigEntry()

        self.idEntry['state'] = DISABLED
        self.idType_entry['state'] = NORMAL
        self.noId_Entry['state'] = NORMAL
        self.names_entry['state'] = NORMAL
        self.lastNames_entry['state'] = NORMAL
        self.adress_entry['state'] = NORMAL
        self.phone_entry['state'] = NORMAL
        self.city_entry['state'] = NORMAL
        self.nacDate_entry['state'] = NORMAL
        self.ingDate_entry['state'] = NORMAL

        self.edit_btn['state'] = DISABLED
        self.save_btn['state'] = NORMAL
        self.cancel_btn['state'] = NORMAL
        
    def guardarCambios(self):
        self.AsigEntry()
        entrysActuales = [self.idEntry.get(), self.idType_entry.get(), self.noId_Entry.get(), self.names_entry.get(), self.lastNames_entry.get(), self.adress_entry.get(), self.phone_entry.get(), self.city_entry.get(), self.nacDate_entry.get(), self.ingDate_entry.get()]
        registroActual = self.tree.item(self.tree.selection()[0])['values']
        registroActualStr = []

        for x in registroActual:
            registroActualStr.append(str(x))

        if entrysActuales == registroActualStr:
            messagebox.showinfo('INFORMACION DE EDICION', 'REGISTRO EDITADO CON EXITO, POR FAVOR ACTUALIZAR LA TABLA')

            self.idEntry['state'] = NORMAL

            self.EliminarEntrys()

            self.DesactivarEntrys()

            self.edit_btn['state'] = NORMAL
            self.save_btn['state'] = DISABLED
            self.cancel_btn['state'] = DISABLED

        else:

            noIdExist = False

            for x in self.listadoDict:
                if (x['_Cliente__noDocumento'] == self.temp_noId.get()) and (x['_Cliente__noDocumento'] != registroActualStr[2]):
                    noIdExist = True

            if (self.idType_entry.get() == '' or self.noId_Entry.get() == '' or self.names_entry.get() == '' or self.lastNames_entry.get() == '' or self.adress_entry.get() == '' or self.phone_entry.get() == '' or self.city_entry.get() == '' or self.nacDate_entry.get() == '' or self.ingDate_entry.get() == ''):
                messagebox.showerror(message='Debe llenar todos los campos.', title='ERROR DE EDICION DE CLIENTE')
            elif noIdExist:
                messagebox.showerror(title='NUMERO DE IDENTIFICACION INCORRECTO', message='El numero de identificacion ya existe.')
            else:
                self.metodosClientes.editarCliente(
                    registroActualStr[2],
                    self.temp_idType.get(),
                    self.temp_noId.get(),
                    self.temp_names.get(),
                    self.temp_lastNames.get(),
                    self.temp_adress.get(),
                    self.temp_phone.get(),
                    self.temp_city.get(),
                    self.temp_nacDate.get(),
                    self.temp_ingDate.get())
                
                messagebox.showinfo('INFORMACION DE EDICION', 'REGISTRO EDITADO CON EXITO, POR FAVOR ACTUALIZAR LA TABLA')

                self.idEntry['state'] = NORMAL

                self.EliminarEntrys()

                self.DesactivarEntrys()

                self.edit_btn['state'] = NORMAL
                self.save_btn['state'] = DISABLED
                self.cancel_btn['state'] = DISABLED

    def eliminarRegistro(self):

        self.AsigEntry()
        self.ActivarEntrys()
        self.metodosClientes.borrarCliente(self.temp_noId.get())
        self.EliminarEntrys()
        self.DesactivarEntrys()
        messagebox.showinfo('ELIMINACION DE USUARIOS', 'Usuario eliminado correctamente!')

    def buscarRegistro(self):
        self.AsigEntry()

        noId_Exist = False

        for x in self.listadoDict:
            if x['_Cliente__numDocumento'] == self.temp_BuscarUser.get():
                noId_Exist = True

        if self.temp_BuscarUser.get() == '':
            messagebox.showerror('ERROR DE BUSQUEDA', 'Debe llenar el campo de busqueda.')
        elif not(noId_Exist):
            messagebox.showerror('RESULTADO DE BUSQUEDA', 'El cliente que busca, no existe.')
        elif noId_Exist:
            messagebox.showinfo('RESULTADO DE BUSQUEDA', 'Cliente encontrado!')
            ids = self.tree.get_children()
            indexRegistroBuscado = -1

            for registro in ids:
                indexRegistroBuscado+=1
                if self.tree.item(registro)['values'][2] == self.temp_BuscarUser.get():
                    break
            
            self.tree.selection_set(ids[indexRegistroBuscado])
            self.contadorRegistros = indexRegistroBuscado

            self.colocar_informacion_en_campos()

            self.buscar_entry.delete(0, END)

    def cancelarEdicion(self):

        self.idEntry['state'] = NORMAL

        self.EliminarEntrys()

        self.DesactivarEntrys()

        self.save_btn['state'] = DISABLED
        self.cancel_btn['state'] = DISABLED
        self.edit_btn['state'] = NORMAL



    def colocar_informacion_en_campos(self):

        tuplaSeleccion = self.tree.selection()
        atribSelecActual = self.tree.item(tuplaSeleccion[0])['values']

        self.ActivarEntrys()

        self.EliminarEntrys()

        self.idEntry.insert(0, atribSelecActual[0])
        self.idType_entry.insert(0, atribSelecActual[1])
        self.noId_Entry.insert(0, atribSelecActual[2])
        self.names_entry.insert(0, atribSelecActual[3])
        self.lastNames_entry.insert(0, atribSelecActual[4])
        self.adress_entry.insert(0, atribSelecActual[5])
        self.phone_entry.insert(0, atribSelecActual[6])
        self.city_entry.insert(0, atribSelecActual[7])
        self.nacDate_entry.insert(0, atribSelecActual[8])
        self.ingDate_entry.insert(0, atribSelecActual[9])

        self.DesactivarEntrys()

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


    def ventanaCrearCliente(self):
        root = Tk()
        Create_client(root)
        root.mainloop()

    def actualizarTabla(self):
        self.metodosClientes = ClientesList()
        self.listadoDict = self.metodosClientes.dataJson['clients']

        for i in self.tree.get_children():
            self.tree.delete(i)
        for x in self.listadoDict:
            self.tree.insert('', 'end', 
                values=[
                    x['_Cliente__id'], 
                    x['_Cliente__tipoDocumento'], 
                    x['_Cliente__noDocumento'], 
                    x['_Cliente__nombre'], 
                    x['_Cliente__apellido'], 
                    x['_Cliente__direccion'], 
                    x['_Cliente__telefono'], 
                    x['_Cliente__ciudad'], 
                    x['_Cliente__fechaNac'], 
                    x['_Cliente__fechaIng']])