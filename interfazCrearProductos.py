from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from productosList import ProductosList

class Create_product(Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.metodosProductos = ProductosList()

        self.colorFondo = '#FB516B'

        self.root = root
        self.root.title('INTERFAZ DE PRODUCTOS')
        self.root.configure(bg=self.colorFondo)

        #Creando variables temporales
        self.temp_idProduct = StringVar()
        self.temp_description = StringVar()
        self.temp_price = StringVar()
        self.temp_iva = StringVar()
        self.temp_note = StringVar()

        self.temp_BuscarUser = StringVar()

        # TITLE
        self.title_Label = Label(self.root, text='FORMULARIO PARA CREACION DE PRODUCTOS ', background=self.colorFondo, fg='white')
        self.title_Label.grid(row=0, column=0, columnspan=10)

        self.idproductLabel = Label(self.root, text='Id Producto: ', background=self.colorFondo, fg='white')
        self.idproductLabel.grid(row=1, column=0, columnspan=2, sticky='ew', padx=(5,0), pady=(15,15))
        self.idproductEntry = Entry(self.root, textvariable=self.temp_idProduct)
        self.idproductEntry.grid(row=1, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # ID USER
        self.descriptionLabel = Label(self.root, text='Descripcion: ', background=self.colorFondo, fg='white')
        self.descriptionLabel.grid(row=1, column=5, columnspan=2, sticky='ew', padx=(5,0), pady=(15,15))
        self.descriptionEntry = Entry(self.root, textvariable=self.temp_description)
        self.descriptionEntry.grid(row=1, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # NAMES
        self.priceLabel = Label(self.root, text='Precio: ', background=self.colorFondo, fg='white')
        self.priceLabel.grid(row=2, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.priceEntry = Entry(self.root, textvariable=self.temp_price)
        self.priceEntry.grid(row=2, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # PROFILE
        self.ivaLabel = Label(self.root, text='IVA(%): ', background=self.colorFondo, fg='white')
        self.ivaLabel.grid(row=2, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.ivaEntry = ttk.Combobox(self.root, values=['5', '12'], textvariable=self.temp_iva)
        self.ivaEntry.grid(row=2, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # LAST NAMES
        self.noteLabel = Label(self.root, text='Nota: ', background=self.colorFondo, fg='white')
        self.noteLabel.grid(row=3, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.noteEntry = Entry(self.root, textvariable=self.temp_note)
        self.noteEntry.grid(row=3, column=2, columnspan=8, sticky='ew', padx=(0,15), pady=(15,15))

        self.listadoDict = self.metodosProductos.dataJson['products']

        #BOTONES DE DESPLAZAMIENTO
        self.first_btn = Button(self.root, text='CREAR PRODUCTO', command=self.createProduct)
        self.first_btn.grid(row=5, column=0, columnspan=5, padx=(25,5), pady=5)

        self.previous_btn = Button(self.root, text='CANCELAR', command=self.root.destroy)
        self.previous_btn.grid(row=5, column=5,columnspan=5, padx=5, pady=5)

    def AsigEntry(self):
        self.temp_idProduct.set(self.idproductEntry.get())
        self.temp_description.set(self.descriptionEntry.get())
        self.temp_price.set(self.priceEntry.get())
        self.temp_iva.set(self.ivaEntry.get())
        self.temp_note.set(self.noteEntry.get())

    def createProduct(self):
        self.AsigEntry()

        if (self.idproductEntry.get() == '' or self.descriptionEntry.get() == '' or self.priceEntry.get() == '' or self.ivaEntry.get() == '' or self.noteEntry.get() == ''):
            messagebox.showerror(message='DEBE LLENAR CADA CAMPO SOLICITADO', title='ERROR DE CREACION DE PRODUCTO')
        else:
            descriptionExist = False
            idExists = False

            for x in self.listadoDict:
                if x['_Producto__descripcion'] == self.temp_description.get():
                    descriptionExist = True

                if x['_Producto__id'] == int(self.temp_idProduct.get()):
                    idExists = True
            
            if descriptionExist:
                messagebox.showerror(message='La descripcion de producto ya existe.', title='PRODUCTO NO VALIDO')
            elif idExists:
                messagebox.showerror(message='El ID de producto ya existe.', title='ID NO VALIDO')
            else:
                self.metodosProductos.crearProducto(
                    int(self.temp_idProduct.get()),
                    self.temp_description.get(),
                    self.temp_price.get(),
                    self.temp_iva.get(),
                    self.temp_note.get())
                
                messagebox.showinfo(message='PRODUCTO CREADO CON EXITO!', title='INFORMACION')
                self.root.destroy()