from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from clientesList import ClientesList
from productosList import ProductosList
from facturasList import FacturasList
from tkinter import messagebox
from reporteFacturas import *

class Report_Interface(Frame):

    def __init__(self, root):
        super().__init__(root)

        self.colorFondo = '#19BDB4'

        self.metodosFacturas = FacturasList()
        self.metodosProductos = ProductosList()
        self.metodosClientes = ClientesList()

        self.diccFacturas = self.metodosFacturas.dataJson['facturas']
        self.diccClientes = self.metodosClientes.dataJson['clients']
        self.diccProductos = self.metodosProductos.dataJson['products']

        self.listadoClientes = []
        self.listadoProductos = []

        self.tipoFiltro = ''

        for cliente in self.diccClientes:
            self.listadoClientes.append(cliente['_Cliente__nombre'])

        for producto in self.diccProductos:
            self.listadoProductos.append(producto['_Producto__descripcion'])

        self.root = root
        self.root.title('INTERFAZ DE REPORTES')
        self.root.configure(bg=self.colorFondo)

        # TITLE
        self.title_Label = Label(self.root, text='FORMULARIO PARA CREACION DE REPORTE DE FACTURAS ', background=self.colorFondo, fg='white')
        self.title_Label.grid(row=0, column=0, columnspan=10)

        self.strainType_Label = Label(self.root, text='TIPO DE FILTRO: ', background=self.colorFondo, fg='white')
        self.strainType_Label.grid(row=1, column=0, columnspan=4, sticky='e', padx=(5,50), pady=35)
        self.strainType_Entry = ttk.Combobox(self.root, state='readonly', values=['Por cliente', 'Por producto', 'Por Rango de fecha'])
        self.strainType_Entry.grid(row=1, column=4, columnspan=4, sticky='w', padx=(0,15), pady=35)

        # 
        self.clients_Label = Label(self.root, text='Clientes: ', background=self.colorFondo, fg='white')
        self.clients_Label.grid(row=2, column=0, sticky='ew', padx=(5,0), pady=(15,15))
        self.clients_Entry = ttk.Combobox(self.root, values=self.listadoClientes, state=DISABLED)
        self.clients_Entry.grid(row=2, column=1, sticky='ew', padx=(0,15), pady=(15,15))

        # NAMES
        self.products_Label = Label(self.root, text='Productos: ', background=self.colorFondo, fg='white')
        self.products_Label.grid(row=2, column=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.products_Entry = ttk.Combobox(self.root, values=self.listadoProductos, state=DISABLED)
        self.products_Entry.grid(row=2, column=3, sticky='ew', padx=(0,15), pady=(15,15))

        # PROFILE
        self.from_Label = Label(self.root, text='Desde: ', background=self.colorFondo, fg='white')
        self.from_Label.grid(row=2, column=4, sticky='ew', padx=(15,0), pady=(15,15))
        self.from_Entry = DateEntry(self.root, state =DISABLED)
        self.from_Entry.grid(row=2, column=5, sticky='ew', padx=(0,15), pady=(15,15))

        # PROFILE
        self.until_Label = Label(self.root, text='Hasta: ', background=self.colorFondo, fg='white')
        self.until_Label.grid(row=2, column=6, sticky='ew', padx=(15,0), pady=(15,15))
        self.until_Entry = DateEntry(self.root, state=DISABLED)
        self.until_Entry.grid(row=2, column=7, sticky='ew', padx=(0,15), pady=(15,15))


        self.add = Button(self.root, text='FILTRAR', command=self.filtroGeneral)
        self.add.grid(row=3, column=0,columnspan=8, padx=(25,5), pady=15)

        self.add = Button(self.root, text='GENERAR REPORTE DE FACTURAS', command=self.extraerListaIdsEnArbol)
        self.add.grid(row=5, column=0,columnspan=8, padx=(25,5), pady=45)


        self.columns = ('factura_id','date', 'client', 'total_factura')

        self.tree = ttk.Treeview(self.root, columns=self.columns, show='headings')

        self.tree.heading('factura_id', text='ID FACTURA')
        self.tree.heading('date', text='FECHA DE EMISION')
        self.tree.heading('client', text='A NOMBRE DE')
        self.tree.heading('total_factura', text='TOTAL DE FACTURA')
        

        self.tree.column('#1', width=150, anchor='center')
        self.tree.column('#2', width=150, anchor='center')
        self.tree.column('#3', width=150, anchor='center')
        self.tree.column('#4', width=150, anchor='center')
        

        self.tree.grid(row=4, column=0, sticky='ew', columnspan=8, padx=15, pady=15)

        self.verScrol = ttk.Scrollbar(self.root, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.verScrol.set)
        self.verScrol.grid(row=4, column=8, sticky='ns', padx=10)

        self.strainType_Entry.bind('<<ComboboxSelected>>', self.activarFiltros)

    def activarFiltros(self, event):
        if self.strainType_Entry.current() == 0:

            self.clients_Entry['state'] = NORMAL
            self.clients_Entry['state'] = 'readonly'

            self.products_Entry['state'] = DISABLED
            self.from_Entry['state'] = DISABLED
            self.until_Entry['state'] = DISABLED
            self.tipoFiltro = 'cliente'

        elif self.strainType_Entry.current() == 1:
           
            self.products_Entry['state'] = NORMAL
            self.products_Entry['state'] = 'readonly'

            self.clients_Entry.delete(0, END)
            self.from_Entry.delete(0, END)
            self.until_Entry.delete(0, END)

            self.clients_Entry['state'] = DISABLED
            self.from_Entry['state'] = DISABLED
            self.until_Entry['state'] = DISABLED
            self.tipoFiltro = 'producto'

        elif self.strainType_Entry.current() == 2:
            
            self.from_Entry['state'] = NORMAL
            self.until_Entry['state'] = NORMAL
            self.from_Entry['state'] = 'readonly'
            self.until_Entry['state'] = 'readonly'

            self.products_Entry.delete(0, END)
            self.clients_Entry.delete(0, END)

            self.products_Entry['state'] = DISABLED
            self.clients_Entry['state'] = DISABLED
            self.tipoFiltro = 'fecha'

    def limpiarRegistros(self):
        for children in self.tree.get_children():
            self.tree.delete(children)

    def filtroGeneral(self):
        
        if self.tipoFiltro == 'cliente':

            self.limpiarRegistros()
            self.filtroClientes()

        elif self.tipoFiltro == 'producto':

            self.limpiarRegistros()
            self.filtroProductos()

        elif self.tipoFiltro == 'fecha':

            self.limpiarRegistros()
            self.filtroFechas()

    def filtroClientes(self):
        
        for factura in self.diccFacturas:
            
            if factura['_Factura__cliente'] == self.clients_Entry.get():

                self.tree.insert('', 'end', values=[
                    factura['_Factura__id'],
                    factura['_Factura__fecha'],
                    factura['_Factura__cliente'],
                    str(factura['_Factura__total'])
                ])

    def filtroProductos(self):
        
        for factura in self.diccFacturas:
            for producto in factura['_Factura__productos']:
                if producto['_Producto__descripcion'] == self.products_Entry.get():
                    self.tree.insert('', 'end', values=[
                        factura['_Factura__id'],
                        factura['_Factura__fecha'],
                        factura['_Factura__cliente'],
                        str(factura['_Factura__total'])
                    ])
                    break

    def filtroFechas(self):
        
        for factura in self.diccFacturas:
            
            if (self.from_Entry.get() <= factura['_Factura__fecha']) and (factura['_Factura__fecha'] <= self.until_Entry.get()):
                
                self.tree.insert('', 'end', values=[
                    factura['_Factura__id'],
                    factura['_Factura__fecha'],
                    factura['_Factura__cliente'],
                    str(factura['_Factura__total'])
                ])

    def extraerListaIdsEnArbol(self):
        listaIds = []

        for row in self.tree.get_children():
            listaIds.append(int(self.tree.item(row)['values'][0]))

        reportePdf = ReporteFacturas()
        reportePdf.getIDS(listaIds)

