from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from clientesList import ClientesList
from tkcalendar import DateEntry

class Create_client(Frame):

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
        self.idEntry = Entry(self.root, textvariable=self.temp_clientId)
        self.idEntry.grid(row=1, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # TIPO IDENTIFICACION
        self.idType_label = Label(self.root, text='Tipo Identificacion: ', background=self.colorFondo, fg='white')
        self.idType_label.grid(row=1, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.idType_entry = ttk.Combobox(self.root, values=['DPI', 'PASAPORTE'], textvariable=self.temp_idType)
        self.idType_entry.grid(row=1, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # NO. IDENTIFICACION
        self.noId_Label = Label(self.root, text='No. Identificacion: ', background=self.colorFondo, fg='white')
        self.noId_Label.grid(row=2, column=0, columnspan=2, sticky='ew', padx=(5,0), pady=(15,15))
        self.noId_Entry = Entry(self.root, textvariable=self.temp_noId)
        self.noId_Entry.grid(row=2, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # NOMBRES
        self.names_label = Label(self.root, text='Nombres: ', background=self.colorFondo, fg='white')
        self.names_label.grid(row=2, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.names_entry = Entry(self.root, textvariable=self.temp_names)
        self.names_entry.grid(row=2, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # APELLIDO
        self.lastNames_label = Label(self.root, text='Apellidos: ', background=self.colorFondo, fg='white')
        self.lastNames_label.grid(row=3, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.lastNames_entry = Entry(self.root, textvariable=self.temp_lastNames)
        self.lastNames_entry.grid(row=3, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # DIRECCION
        self.adress_label = Label(self.root, text='Direccion: ', background=self.colorFondo, fg='white')
        self.adress_label.grid(row=3, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.adress_entry = Entry(self.root, textvariable=self.temp_adress)
        self.adress_entry.grid(row=3, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # TELEFONO
        self.phone_label = Label(self.root, text='Telefono: ', background=self.colorFondo, fg='white')
        self.phone_label.grid(row=4, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.phone_entry = Entry(self.root, textvariable=self.temp_phone)
        self.phone_entry.grid(row=4, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # CIUDAD
        self.city_label = Label(self.root, text='Ciudad: ', background=self.colorFondo, fg='white')
        self.city_label.grid(row=4, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.city_entry = ttk.Combobox(self.root, values=['Coban', 'Tactic', 'Chamelco', 'Carchá'], textvariable=self.temp_city)
        self.city_entry.grid(row=4, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # FECHA DE NACIMIENTO
        self.nacDate_label = Label(self.root, text='Fecha de Nacimiento: ', background=self.colorFondo, fg='white')
        self.nacDate_label.grid(row=5, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.nacDate_entry = DateEntry(self.root, textvariable=self.temp_nacDate)
        self.nacDate_entry.grid(row=5, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # FECHA DE INGRESO
        self.ingDate_label = Label(self.root, text='Fecha de Ingreso: ', background=self.colorFondo, fg='white')
        self.ingDate_label.grid(row=5, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.ingDate_entry = DateEntry(self.root, textvariable=self.temp_ingDate)
        self.ingDate_entry.grid(row=5, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        self.listadoDict = self.metodosClientes.dataJson['clients']

        #BOTONES DE DESPLAZAMIENTO
        self.first_btn = Button(self.root, text='CREAR CLIENTE', command=self.createClient)
        self.first_btn.grid(row=6, column=0, columnspan=5, padx=(25,5), pady=5)

        self.previous_btn = Button(self.root, text='CANCELAR', command=self.root.destroy)
        self.previous_btn.grid(row=6, column=5,columnspan=5, padx=5, pady=5)

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

    def createClient(self):
        self.AsigEntry()

        if (self.idType_entry.get() == '' or self.noId_Entry.get() == '' or self.names_entry.get() == '' or self.lastNames_entry.get() == '' or self.adress_entry.get() == '' or self.phone_entry.get() == '' or self.city_entry.get() == '' or self.nacDate_entry.get() == '' or self.ingDate_entry.get() == ''):
            messagebox.showerror(message='DEBE LLENAR CADA CAMPO SOLICITADO', title='ERROR DE CREACION DE CLIENTE')
        else:
            noIdExists = False
            idExists = False

            for x in self.listadoDict:
                if x['_Cliente__noDocumento'] == self.temp_noId.get():
                    noIdExists = True

                if x['_Cliente__id'] == int(self.temp_clientId.get()):
                    idExists = True

            if noIdExists:
                messagebox.showerror(message='El numero de identificacion ya existe.', title='CLIENTE NO VALIDO')
            elif idExists:
                messagebox.showerror(message='El ID de cliente ya existe.', title='ID NO VALIDO')
            else:
                self.metodosClientes.crearCliente(
                    int(self.temp_clientId.get()),
                    self.temp_idType.get(),
                    self.temp_noId.get(),
                    self.temp_names.get(),
                    self.temp_lastNames.get(),
                    self.temp_adress.get(),
                    self.temp_phone.get(),
                    self.temp_city.get(),
                    self.temp_nacDate.get(),
                    self.temp_ingDate.get())
                
                messagebox.showinfo(message='CLIENTE CREADO CON EXITO!', title='INFORMACION')
                self.root.destroy()