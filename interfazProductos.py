from tkinter import *
from tkinter import ttk
from productosList import ProductosList
from tkinter import messagebox
from interfazCrearProductos import Create_product

class Product_Interface(Frame):
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
        self.title_Label = Label(self.root, text='FORMULARIO PARA CREACION DE PRODUCTOS ', background=self.colorFondo, fg='white', font=('Times',20))
        self.title_Label.grid(row=0, column=0, columnspan=10, pady=20)

        self.idproductLabel = Label(self.root, text='Id Producto: ', background=self.colorFondo, fg='white')
        self.idproductLabel.grid(row=1, column=0, columnspan=2, sticky='ew', padx=(5,0), pady=(15,15))
        self.idproductEntry = Entry(self.root, textvariable=self.temp_idProduct, state=DISABLED)
        self.idproductEntry.grid(row=1, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # ID USER
        self.descriptionLabel = Label(self.root, text='Descripcion: ', background=self.colorFondo, fg='white')
        self.descriptionLabel.grid(row=1, column=5, columnspan=2, sticky='ew', padx=(5,0), pady=(15,15))
        self.descriptionEntry = Entry(self.root, textvariable=self.temp_description, state=DISABLED)
        self.descriptionEntry.grid(row=1, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # NAMES
        self.priceLabel = Label(self.root, text='Precio: ', background=self.colorFondo, fg='white')
        self.priceLabel.grid(row=2, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.priceEntry = Entry(self.root, textvariable=self.temp_price, state=DISABLED)
        self.priceEntry.grid(row=2, column=2, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # PROFILE
        self.ivaLabel = Label(self.root, text='IVA (%): ', background=self.colorFondo, fg='white')
        self.ivaLabel.grid(row=2, column=5, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.ivaEntry = ttk.Combobox(self.root, state='disabled', values=['5', '12'], textvariable=self.temp_iva)
        self.ivaEntry.grid(row=2, column=7, columnspan=3, sticky='ew', padx=(0,15), pady=(15,15))

        # LAST NAMES
        self.noteLabel = Label(self.root, text='Nota: ', background=self.colorFondo, fg='white')
        self.noteLabel.grid(row=3, column=0, columnspan=2, sticky='ew', padx=(15,0), pady=(15,15))
        self.noteEntry = Entry(self.root, textvariable=self.temp_note, state=DISABLED)
        self.noteEntry.grid(row=3, column=2, columnspan=8, sticky='ew', padx=(0,15), pady=(15,15))


        #OPCIONES BUSCAR

        self.buscar_label = Label(self.root, text='Ingresar nombre de producto: ', background=self.colorFondo, fg='white')
        self.buscar_label.grid(row=5, column=0, columnspan=3, pady=20, sticky='e')
        self.buscar_entry = Entry(self.root, textvariable=self.temp_BuscarUser)
        self.buscar_entry.grid(row=5, column=4, columnspan=4, pady=20, sticky='w')
        self.buscar_btn = Button(self.root, text='BUSCAR REGISTRO', command=self.buscarRegistro)
        self.buscar_btn.grid(row=5, column=7, columnspan=3, pady=20, sticky='w')

        #BOTONES DE DESPLAZAMIENTO
        self.first_btn = Button(self.root, text='Primero', command=self.ir_al_primer_registro)
        self.first_btn.grid(row=4, column=0, padx=(10,3), pady=5)

        self.previous_btn = Button(self.root, text='Anterior', command=self.ir_al_registro_anterior)
        self.previous_btn.grid(row=4, column=1, padx=3, pady=5)

        self.next_btn = Button(self.root, text='Siguiente', command=self.ir_al_siguiente_registro)
        self.next_btn.grid(row=4, column=2, padx=3, pady=5)

        self.last_btn = Button(self.root, text='Ultimo', command = self.ir_al_ultimo_registro)
        self.last_btn.grid(row=4, column=3, padx=3, pady=5)

        self.last_btn = Button(self.root, text='Actualizar', command=self.actualizarTabla)
        self.last_btn.grid(row=4, column=4, padx=(3, 10), pady=5)

        #BOTONES DE MANIPULACION DE DATOS

        self.create_btn = Button(self.root, text='Crear', command=self.ventanaCrearProducto)
        self.create_btn.grid(row=4, column=5, padx=(10, 3), pady=15)

        self.edit_btn = Button(self.root, text='Editar', command=self.editarRegistro)
        self.edit_btn.grid(row=4, column=6, padx=3, pady=15)

        self.save_btn = Button(self.root, text='Guardar', state=DISABLED, command=self.guardarCambios)
        self.save_btn.grid(row=4, column=7, padx=3, pady=15)

        self.delete_btn = Button(self.root, text='Borrar', command=self.eliminarRegistro)
        self.delete_btn.grid(row=4, column=8, padx=3, pady=15)

        self.cancel_btn = Button(self.root, text='Cancelar', state=DISABLED, command=self.cancelarEdicion)
        self.cancel_btn.grid(row=4, column=9, padx=(3,20), pady=15)

        #INCLUYENDO TABLA

        self.columns = ('product_id','description', 'price', 'iva', 'note')

        self.tree = ttk.Treeview(self.root, columns=self.columns, show='headings')

        self.tree.heading('product_id', text='ID')
        self.tree.heading('description', text='DESCRIPCION')
        self.tree.heading('price', text='PRECIO')
        self.tree.heading('iva', text='IVA (%)')
        self.tree.heading('note', text='NOTA')

        self.tree.column('#1', width=70, anchor='center')
        self.tree.column('#2', width=150, anchor='center')
        self.tree.column('#3', width=150, anchor='center')
        self.tree.column('#4', width=150, anchor='center')
        self.tree.column('#5', width=150, anchor='center')


        #Colocando usuarios dentro de la tabla
        self.listadoDict = self.metodosProductos.dataJson['products']
        
        for x in self.listadoDict:
            self.tree.insert('', 'end', 
                             values=[
                                 x['_Producto__id'], 
                                 x['_Producto__descripcion'], 
                                 x['_Producto__precio'], 
                                 x['_Producto__iva'], 
                                 x['_Producto__nota']])

        self.contadorRegistros = 0

        if len(self.tree.get_children()) != 0:
            self.tree.selection_set(self.tree.get_children()[self.contadorRegistros])
            self.tree.focus(self.tree.focus(self.tree.get_children()[self.contadorRegistros]))

        self.tree.grid(row=6, column=0, columnspan=10, padx=15, pady=15)

        #Creando un scrollbar vertical para desplazarse en la tabla
        self.verScrol = ttk.Scrollbar(self.root, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.verScrol.set)
        self.verScrol.grid(row=6, column=10, sticky='ns', padx=10)
        


    def AsigEntry(self):
        self.temp_idProduct.set(self.idproductEntry.get())
        self.temp_description.set(self.descriptionEntry.get())
        self.temp_price.set(self.priceEntry.get())
        self.temp_iva.set(self.ivaEntry.get())
        self.temp_note.set(self.noteEntry.get())
        self.temp_BuscarUser.set(self.buscar_entry.get())

    def EliminarEntrys(self):
        self.idproductEntry.delete(0, END)
        self.descriptionEntry.delete(0, END)
        self.priceEntry.delete(0, END)
        self.ivaEntry.delete(0, END)
        self.noteEntry.delete(0, END)

    def DesactivarEntrys(self):
        self.idproductEntry['state'] = DISABLED
        self.descriptionEntry['state'] = DISABLED
        self.priceEntry['state'] = DISABLED
        self.ivaEntry['state'] = DISABLED
        self.noteEntry['state'] = DISABLED

    def ActivarEntrys(self):
        self.idproductEntry['state'] = NORMAL
        self.descriptionEntry['state'] = NORMAL
        self.priceEntry['state'] = NORMAL
        self.ivaEntry['state'] = NORMAL
        self.noteEntry['state'] = NORMAL



    def editarRegistro(self):
        self.AsigEntry()

        self.idproductEntry['state'] = DISABLED
        self.descriptionEntry['state'] = NORMAL
        self.priceEntry['state'] = NORMAL
        self.ivaEntry['state'] = NORMAL
        self.noteEntry['state'] = NORMAL

        self.edit_btn['state'] = DISABLED
        self.save_btn['state'] = NORMAL
        self.cancel_btn['state'] = NORMAL
        
    def guardarCambios(self):
        self.AsigEntry()
        entrysActuales = [self.idproductEntry.get(), self.descriptionEntry.get(), self.priceEntry.get(), self.ivaEntry.get(), self.noteEntry.get()]
        registroActual = self.tree.item(self.tree.selection()[0])['values']
        registroActualStr = []

        for x in registroActual:
            registroActualStr.append(str(x))

        if entrysActuales == registroActualStr:
            messagebox.showinfo('INFORMACION DE EDICION', 'REGISTRO EDITADO CON EXITO, POR FAVOR ACTUALIZAR LA TABLA')

            self.idproductEntry['state'] = NORMAL

            self.EliminarEntrys()

            self.DesactivarEntrys()

            self.edit_btn['state'] = NORMAL
            self.save_btn['state'] = DISABLED
            self.cancel_btn['state'] = DISABLED

        else:

            productExist = False

            for x in self.listadoDict:
                if (x['_Producto__descripcion'] == self.temp_description.get()) and (x['_Producto__descripcion'] != registroActualStr[1]):
                    productExist = True

            if (self.descriptionEntry.get() == '' or self.priceEntry.get() == '' or self.ivaEntry.get() == '' or self.noteEntry.get() == ''):
                messagebox.showerror(message='Debe llenar todos los campos.', title='ERROR DE EDICION DE PRODUCTO')
            elif productExist:
                messagebox.showerror(title='NOMBRE DE PRODUCTO NO VALIDO', message='El nombre de producto ya existe.')
            else:
                self.metodosProductos.editarProducto(
                    registroActualStr[1],
                    self.temp_description.get(),
                    self.temp_price.get(),
                    self.temp_iva.get(),
                    self.temp_note.get())
                
                messagebox.showinfo('INFORMACION DE EDICION', 'REGISTRO EDITADO CON EXITO, POR FAVOR ACTUALIZAR LA TABLA')

                self.idproductEntry['state'] = NORMAL

                self.EliminarEntrys()

                self.DesactivarEntrys()

                self.edit_btn['state'] = NORMAL
                self.save_btn['state'] = DISABLED
                self.cancel_btn['state'] = DISABLED

    def eliminarRegistro(self):

        self.AsigEntry()
        self.ActivarEntrys()
        self.metodosProductos.borrarProducto(self.temp_description.get())
        self.EliminarEntrys()
        self.DesactivarEntrys()
        messagebox.showinfo('ELIMINACION DE USUARIOS', 'Usuario eliminado correctamente!')

    def buscarRegistro(self):
        self.AsigEntry()

        descriptionExist = False

        for x in self.listadoDict:
            if x['_Producto__descripcion'] == self.temp_BuscarUser.get():
                descriptionExist = True

        if self.temp_BuscarUser.get() == '':
            messagebox.showerror('ERROR DE BUSQUEDA', 'Debe llenar el campo de busqueda.')
        elif not(descriptionExist):
            messagebox.showerror('RESULTADO DE BUSQUEDA', 'El producto que busca, no existe.')
        elif descriptionExist:
            messagebox.showinfo('RESULTADO DE BUSQUEDA', 'Producto encontrado!')
            ids = self.tree.get_children()
            indexRegistroBuscado = -1

            for registro in ids:
                indexRegistroBuscado+=1
                if str(self.tree.item(registro)['values'][1]) == self.temp_BuscarUser.get():
                    break
            
            self.tree.selection_set(ids[indexRegistroBuscado])
            self.contadorRegistros = indexRegistroBuscado

            self.colocar_informacion_en_campos()

            self.buscar_entry.delete(0, END)

    def cancelarEdicion(self):

        self.idproductEntry['state'] = NORMAL

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

        self.idproductEntry.insert(0, atribSelecActual[0])
        self.descriptionEntry.insert(0, atribSelecActual[1])
        self.priceEntry.insert(0, atribSelecActual[2])
        self.ivaEntry.insert(0, atribSelecActual[3])
        self.noteEntry.insert(0, atribSelecActual[4])

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


    def ventanaCrearProducto(self):
        root = Tk()
        Create_product(root)
        root.mainloop()

    def actualizarTabla(self):
        self.metodosProductos = ProductosList()
        self.listadoDict = self.metodosProductos.dataJson['products']

        for i in self.tree.get_children():
            self.tree.delete(i)
        for x in self.listadoDict:
            self.tree.insert('', 'end', 
                            values=[
                                 x['_Producto__id'], 
                                 x['_Producto__descripcion'], 
                                 x['_Producto__precio'], 
                                 x['_Producto__iva'], 
                                 x['_Producto__nota']])
