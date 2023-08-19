from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from facturasList import FacturasList
from clientesList import ClientesList
from productosList import ProductosList
from tkcalendar import DateEntry

class Create_Factura(Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.metodosFacturas = FacturasList()
        self.metodosClientes = ClientesList()
        self.metodosProductos = ProductosList()

        self.diccFacturas = self.metodosFacturas.dataJson['facturas']
        self.diccClientes = self.metodosClientes.dataJson['clients']
        self.diccProductos = self.metodosProductos.dataJson['products']

        self.listadoClientes = []
        self.listadoProductos = []

        for cliente in self.diccClientes:
            self.listadoClientes.append(cliente['_Cliente__nombre'])

        for producto in self.diccProductos:
            self.listadoProductos.append(producto['_Producto__descripcion'])

        """ for producto in self.diccProductos:
            listaVolatil = []
            listaVolatil.append(producto['_Producto__id'])
            listaVolatil.append(producto['_Producto__descripcion'])
            listaVolatil.append(producto['_Producto__precio'])
            listaVolatil.append(producto['_Producto__iva'])
            listaVolatil.append(producto['_Producto__nota'])
            self.listadoProductos.append(listaVolatil)"""

        self.colorFondo = '#F54620'

        self.root = root
        self.root.title('INTERFAZ DE FACTURACION')
        self.root.configure(bg=self.colorFondo)

        #Creando variables temporales
        self.temp_idFactura = StringVar()
        self.temp_fecha = StringVar()
        self.temp_cliente = StringVar()
        self.temp_producto = StringVar()
        self.temp_cantidad = StringVar()
        self.temp_total = StringVar()


        # TITLE
        self.title_Label = Label(self.root, text='FORMULARIO PARA CREACION DE FACTURAS ', background=self.colorFondo, fg='white')
        self.title_Label.grid(row=0, column=0, columnspan=10)

        # ID FACTURA
        self.idfac_label = Label(self.root, text='Id Factura: ', background=self.colorFondo, fg='white')
        self.idfac_label.grid(row=1, column=0, columnspan=2, sticky='ew', padx=(5,0), pady=10)
        self.idfac_entry = Entry(self.root, textvariable=self.temp_idFactura)
        self.idfac_entry.grid(row=1, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=10)

        # FECHA
        self.fecha_label = Label(self.root, text='Fecha: ', background=self.colorFondo, fg='white')
        self.fecha_label.grid(row=1, column=5, columnspan=2, sticky='ew', padx=(5,0), pady=10)
        self.fecha_entry = DateEntry(self.root, textvariable=self.temp_fecha)
        self.fecha_entry.grid(row=1, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=10)

        # CLIENTES
        self.cliente_label = Label(self.root, text='Cliente: ', background=self.colorFondo, fg='white')
        self.cliente_label.grid(row=2, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=10)
        self.cliente_entry = ttk.Combobox(self.root, values=self.listadoClientes, textvariable=self.temp_cliente)
        self.cliente_entry.grid(row=2, column=2, columnspan=8, sticky='ew', padx=(0,15), pady=10)

        # PRODUCTO
        self.producto_label = Label(self.root, text='Producto: ', background=self.colorFondo, fg='white')
        self.producto_label.grid(row=3, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=10)
        self.producto_entry = ttk.Combobox(self.root, values=self.listadoProductos, textvariable=self.temp_producto)
        self.producto_entry.grid(row=3, column=2, columnspan=8, sticky='ew', padx=(0,15), pady=10)

        # CANTIDAD
        self.cantidad_label = Label(self.root, text='Cantidad: ', background=self.colorFondo, fg='white')
        self.cantidad_label.grid(row=4, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=10)
        self.cantidad_entry = Entry(self.root, textvariable=self.temp_cantidad)
        self.cantidad_entry.grid(row=4, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=10)

        # TOTAL

        self.total_label = Label(self.root, text='TOTAL: ', background=self.colorFondo, fg='white')
        self.total_label.grid(row=6, column=5, columnspan=2, sticky='ew', padx=(5,0), pady=10)
        self.total_entry = Entry(self.root, textvariable=self.temp_total)
        self.total_entry.grid(row=6, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=25)
        

        #BOTONES DE DESPLAZAMIENTO
        self.add = Button(self.root, text='Añadir', command=self.addProduct)
        self.add.grid(row=4, column=5, padx=(25,5), pady=5)

        self.deleteRow = Button(self.root, text='Quitar', command=self.deleteProduct)
        self.deleteRow.grid(row=4, column=6, padx=5, pady=5)

        self.deleteAll = Button(self.root, text='Vaciar', command=self.deleteAllProducts)
        self.deleteAll.grid(row=4, column=7, padx=5, pady=5)

        self.totalFactura = 0

        self.saveFac = Button(self.root, text='Guardar', command=self.save_fac)
        self.saveFac.grid(row=4, column=8, padx=5, pady=5)


        self.columns = ('product_id','description', 'price', 'quantity', 'value')

        self.tree = ttk.Treeview(self.root, columns=self.columns, show='headings')

        self.tree.heading('product_id', text='ID PRODUCTO')
        self.tree.heading('description', text='DESCRIPCION')
        self.tree.heading('price', text='PRECIO')
        self.tree.heading('quantity', text='CANTIDAD')
        self.tree.heading('value', text='VALOR')

        self.tree.column('#1', width=100, anchor='center')
        self.tree.column('#2', width=150, anchor='center')
        self.tree.column('#3', width=70, anchor='center')
        self.tree.column('#4', width=70, anchor='center')
        self.tree.column('#5', width=70, anchor='center')

        self.tree.grid(row=5, column=0, columnspan=10, padx=15, pady=15)

        self.verScrol = ttk.Scrollbar(self.root, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.verScrol.set)
        self.verScrol.grid(row=5, column=10, sticky='ns', padx=10)


    def AsigEntry(self):
        self.temp_idFactura.set(self.idfac_entry.get())
        self.temp_fecha.set(self.fecha_entry.get())
        self.temp_cliente.set(self.cliente_entry.get())
        self.temp_producto.set(self.producto_entry.get())
        self.temp_cantidad.set(self.cantidad_entry.get())
        self.temp_total.set(self.total_entry.get())

    def addProduct(self):
        self.AsigEntry()

        if self.idfac_entry.get() == '' or self.fecha_entry.get() == '' or self.cliente_entry.get() == '' or self.producto_entry.get()=='' or self.cantidad_entry.get() == '':
            messagebox.showerror('ERROR AL INCLUIR PRODUCTO', 'Debe llenar todos los campos solicitados.')
        else:
            for producto in self.diccProductos:
                
                if producto['_Producto__descripcion'] == self.temp_producto.get():
                    subtotalConIva = float((int(self.temp_cantidad.get())*float(producto['_Producto__precio']))+(int(self.temp_cantidad.get())*(float(producto['_Producto__precio'])*(int(producto['_Producto__iva'])/100))))
                    self.tree.insert('', 'end', values=[
                        producto['_Producto__id'],
                        producto['_Producto__descripcion'],
                        producto['_Producto__precio'],
                        self.temp_cantidad.get(),
                        str(round(subtotalConIva,1))
                    ])
                    self.totalFactura += subtotalConIva
                    self.total_entry.delete(0, END)
                    self.total_entry.insert(0, round(self.totalFactura,1))
                    self.metodosFacturas.agregarProductos(producto['_Producto__descripcion'], self.temp_cantidad.get())

                    self.producto_entry.delete(0, END) 
                    self.cantidad_entry.delete(0, END)
                    self.cliente_entry['state'] = DISABLED
                    self.idfac_entry['state'] = DISABLED
                    self.fecha_entry['state'] = DISABLED

    def EliminarEntrys(self):
        self.idfac_entry.delete(0, END)
        self.fecha_entry.delete(0, END)
        self.cliente_entry.delete(0, END)
        self.producto_entry.delete(0, END)
        self.cantidad_entry.delete(0, END)
        self.total_entry.delete(0, END)

    def deleteProduct(self):
        indexSeleccion = -1
        seleccionado = self.tree.selection()[0]

        self.metodosFacturas.eliminarProducto(self.tree.item(seleccionado)['values'][1])
        self.totalFactura -= float(self.tree.item(seleccionado)['values'][4])
        self.total_entry.delete(0, END)
        self.total_entry.insert(0, round(self.totalFactura,1))

        for children in self.tree.get_children():
            indexSeleccion += 1
            if seleccionado == children:
                self.tree.delete(children)
                break

    def deleteAllProducts(self):
        
        self.idfac_entry['state'] = NORMAL
        self.cliente_entry['state'] = NORMAL
        self.fecha_entry['state'] = NORMAL
        self.totalFactura = 0
        self.EliminarEntrys()

        for i in self.tree.get_children():
            self.tree.delete(i)

        self.metodosFacturas.limpiarFactura()

    def save_fac(self):
        self.AsigEntry()

        idFacturaExist = False

        for x in self.diccFacturas:
            if x['_Factura__id'] == self.temp_idFactura.get():
                idFacturaExist

        if self.idfac_entry.get() == '' or self.fecha_entry.get() == '' or self.cliente_entry.get() == '' or self.producto_entry.get()=='' or self.cantidad_entry.get() == '':
            messagebox.showerror('ERROR AL INCLUIR PRODUCTO', 'Debe llenar todos los campos solicitados.')
        elif idFacturaExist:
            messagebox.showerror('ERROR EN CREACION DE FACTURA', 'El id de factura ya existe.')
        else:

            self.metodosFacturas.crearFactura(
                self.temp_idFactura.get(), 
                self.temp_fecha.get(),
                self.temp_cliente.get(),
                self.metodosFacturas.productos,
                self.metodosFacturas.total)
            
            messagebox.showinfo('INFORMACION DE FACTURACION', 'La factura se creo correctamente.')
            self.root.destroy()

