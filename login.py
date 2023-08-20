from tkinter import *
from tkinter import messagebox
import json
from interfazUsuarios import *
from interfazClientes import *
from interfazProductos import *
from interfazFacturas import *

class Login_window(Frame):

    def __init__(self, root):
        super().__init__(root)
        
        self.root = root
        self.root.title('Sistema de Ventas')

        self.colorRojo= '#790614'
        self.colorCrema = '#f9f6ec'
        self.colorCeleste = '#88a1a8'
        self.colorMorado = '#502940'
        self.colorNegro = '#0d0c0c'

        self.root.config(bg=self.colorMorado)

        self.dataJson = {}
        self.obtain_data_json()

        self.userExists = False

        #Creating frames

        self.imageFrame = Frame(self.root, bg=self.colorMorado)
        self.imageFrame.grid(row=0, column = 0, padx=5, pady=5)

        self.dataFrame = Frame(self.root, bg=self.colorMorado, width=250, height=200)
        self.dataFrame.grid(row=0, column = 1, padx=5, pady=5)
        self.dataFrame.pack_propagate(False)

        self.logo = PhotoImage(file='images/logoUsac.png')
        self.logo = self.logo.subsample(3)

        #Create labelImage

        Label(self.imageFrame, image= self.logo).grid(columnspan=2, row=0)

        #Create fields USER

        self.username = StringVar()
        self.password = StringVar()

        self.label_user = Label(self.dataFrame, text='USER: ', bg=self.colorMorado, font='Times', fg=self.colorCrema)
        self.label_user.grid(row=0, column=0, padx=5, pady=5)

        self.entry_user = Entry(self.dataFrame, textvariable=self.username, bg = self.colorCrema)
        self.entry_user.grid(row=0, column=1, padx=5, pady=5)
        self.entry_user.focus()

        #Create fields PASSWORD

        self.label_pass = Label(self.dataFrame, text='PASS: ',bg=self.colorMorado, font='Times', fg=self.colorCrema)
        self.label_pass.grid(row=1, column=0, padx=5, pady=5)

        self.entry_pass = Entry(self.dataFrame, textvariable=self.password, bg = self.colorCrema, show="*")
        self.entry_pass.grid(row=1, column=1, padx=5, pady=5)

        #Create buttons 

        self.button_login = Button(self.dataFrame, text='INICIAR SESION', command = self.obtain_values, bg=self.colorCeleste)
        self.button_login.grid(row=2, column=0, padx=5, pady=10)
        
        self.button_cancel = Button(self.dataFrame, text= 'SALIR', command=self.root.destroy, bg=self.colorCeleste)
        self.button_cancel.grid(row=2, column=1, padx=5, pady=5)

        

    def obtain_data_json(self):
        with open('info.json', 'r') as f:
            data = f.read()
            dataJson = json.loads(data)
            self.dataJson = dataJson

    def obtain_values(self, *args):
        userExists = False
        userNameActual = None
        for user in self.dataJson["users"]:
            if (user["_Usuario__nombreUsuario"] == self.username.get()) and (user["_Usuario__clave"] == self.password.get()):
                userExists = True
                userNameActual = user["_Usuario__nombreUsuario"]

        if userExists:
            self.root.destroy()
            mn = Tk()
            Main_menu(mn, userNameActual)
            mn.mainloop()
        else:
            messagebox.showerror(message='EL USUARIO O CONTRASEÑA SON ERRONEOS, POR FAVOR VERIFICAR.', title='ERROR DE INICIO DE SESION')


class Main_menu(Frame):

    def __init__(self, root, username):
        super().__init__(root)

        self.colorRojo= '#790614'
        self.colorCrema = '#f9f6ec'
        self.colorCeleste = '#88a1a8'
        self.colorMorado = '#502940'
        self.colorNegro = '#0d0c0c'

        self.logo = PhotoImage(file='images/carrito.gif')
        self.logo = self.logo.subsample(3)

        self.userNameActual = username
        self.root = root
        self.root.title(f'Sistema de Ventas')
        self.root.geometry('500x250')

        self.fondo1 = Label(self.root, image=self.logo).place(x=0, y=0, relheight=1, relwidth=1)

        self.userAdmin = False

        #Instanciando el menu archivo
        self.menu = Menu(self.root)
        self.root.config(menu = self.menu, bg = self.colorMorado)

        self.dataJson = {}
        self.obtain_data_json()

        for user in self.dataJson['users']:
            if user['_Usuario__perfil'] == 'Administrador' and user['_Usuario__nombreUsuario'] == self.userNameActual:
                self.userAdmin = True

        #Creando Menu Archivo
        self.file = Menu(self.menu, tearoff=0)

        self.file.add_command(label='Clientes', command=self.display_ci)
        self.file.add_command(label='Productos', command=self.display_pi)

        if self.userAdmin:
            self.file.add_command(label='Usuarios', command=self.display_ui)
        else:
            self.file.add_command(label='Usuarios', state=DISABLED)

        self.file.add_separator()
        self.file.add_command(label='Cambio de Clave')
        self.file.add_command(label='Cambio de Usuario', command= self.userChange)
        self.file.add_separator()
        self.file.add_command(label='Salir', command=self.out)

        #Creando Menu Movimientos
        self.movements = Menu(self.menu, tearoff=0)
        self.movements.add_command(label='Nueva Factura', command=self.display_fi)
        if self.userAdmin:
            self.movements.add_command(label='Reporte de Facturas')
        else:
            self.movements.add_command(label='Reporte de Facturas', state=DISABLED)

        #Creando Menu Ayuda
        self.help = Menu(self.menu, tearoff=0)
        self.help.add_command(label='Acerca de')
        self.help.add_command(label='Ayuda')

        #Creando las pesatanias del menu

        self.menu.add_cascade(label='ARCHIVO', menu=self.file)
        self.menu.add_cascade(label='MOVIMIENTOS', menu=self.movements)
        self.menu.add_cascade(label='AYUDA', menu = self.help)
        

    def obtain_data_json(self):
        
        with open('info.json', 'r') as f:
            data = f.read()
            dataJson = json.loads(data)
            self.dataJson = dataJson
        
    def display_ui(self):
        root = Tk()
        User_Interface(root)
        root.mainloop()
        
    def display_ci(self):
        root = Tk()
        Client_Interface(root)
        root.mainloop()

    def display_pi(self):
        root = Tk()
        Product_Interface(root)
        root.mainloop()

    def display_fi(self):
        root = Tk()
        Create_Factura(root)
        root.mainloop()

    def userChange(self):
        self.root.destroy()
        log = Tk()
        Login_window(log)
        log.mainloop() 

    def out(self):
        self.root.destroy() 



root = Tk()
login = Login_window(root)
root.mainloop()


