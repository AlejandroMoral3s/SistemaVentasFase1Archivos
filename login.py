from tkinter import *
from tkinter import messagebox
import json
from interfazUsuarios import *

class Login_window:

    def __init__(self, root):
        self.root = root
        self.root.title('Sistema de Ventas')
        
        self.dataJson = {}
        self.obtain_data_json()

        self.userExists = False

        #Creating frames

        self.imageFrame = Frame(self.root, bg='red')
        self.imageFrame.grid(row=0, column = 0, padx=5, pady=5)

        self.dataFrame = Frame(self.root, bg='lightBlue', width=250, height=200)
        self.dataFrame.grid(row=0, column = 1, padx=5, pady=5)
        self.dataFrame.pack_propagate(False)

        self.logo = PhotoImage(file='images/logo.png')
        self.logo = self.logo.subsample(10)

        #Create labelImage

        Label(self.imageFrame, image= self.logo).grid(columnspan=2, row=0)

        #Create fields USER

        self.username = StringVar()
        self.password = StringVar()

        self.label_user = Label(self.dataFrame, text='USER: ')
        self.label_user.grid(row=0, column=0, padx=5, pady=5)

        self.entry_user = Entry(self.dataFrame, textvariable=self.username)
        self.entry_user.grid(row=0, column=1, padx=5, pady=5)
        self.entry_user.focus()

        #Create fields PASSWORD

        self.label_pass = Label(self.dataFrame, text='PASS: ')
        self.label_pass.grid(row=1, column=0, padx=5, pady=5)

        self.entry_pass = Entry(self.dataFrame, textvariable=self.password)
        self.entry_pass.grid(row=1, column=1, padx=5, pady=5)

        #Create buttons 

        self.button_login = Button(self.dataFrame, text='INICIAR SESION', command = self.obtain_values)
        self.button_login.grid(row=2, column=0, padx=5, pady=5)
        
        self.button_cancel = Button(self.dataFrame, text= 'SALIR', command=self.root.destroy)
        self.button_cancel.grid(row=2, column=1, padx=5, pady=5)

    def obtain_data_json(self):
        with open('usuarios.json', 'r') as f:
            data = f.read()
            dataJson = json.loads(data)
            self.dataJson = dataJson

    def obtain_values(self, *args):
        userExists = False
        for user in self.dataJson["users"]:
            if (user["username"] == self.username.get()) and (user["password"] == self.password.get()):
                userExists = True

        if userExists:
            self.root.destroy()
            mn = Tk()
            Main_menu(mn)
            mn.mainloop()
        else:
            messagebox.showerror(message='EL USUARIO O CONTRASEÑA SON ERRONEOS, POR FAVOR VERIFICAR.', title='ERROR DE INICIO DE SESION')


class Main_menu():

    def __init__(self, root):

        #Raiz
        self.root = root
        self.root.title(f'Sistema de Ventas')
        self.root.geometry('500x200')

        #Instanciando el menu archivo
        self.menu = Menu(self.root)
        self.root.config(menu = self.menu)

        #Creando Menu Archivo
        self.file = Menu(self.menu, tearoff=0)
        self.file.add_command(label='Clientes')
        self.file.add_command(label='Productos')
        self.file.add_command(label='Usuarios', command=lambda:self.showContent(User_Interface))
        self.file.add_separator()
        self.file.add_command(label='Cambio de Clave')
        self.file.add_command(label='Cambio de Usuario', command= self.userChange)
        self.file.add_separator()
        self.file.add_command(label='Salir', command=self.out)

        #Creando Menu Movimientos
        self.movements = Menu(self.menu, tearoff=0)
        self.movements.add_command(label='Nueva Factura')
        self.movements.add_command(label='Reporte de Facturas')

        #Creando Menu Ayuda
        self.help = Menu(self.menu, tearoff=0)
        self.help.add_command(label='Acerca de')
        self.help.add_command(label='Ayuda')

        #Creando las pesatanias del menu

        self.menu.add_cascade(label='ARCHIVO', menu=self.file)
        self.menu.add_cascade(label='MOVIMIENTOS', menu=self.movements)
        self.menu.add_cascade(label='AYUDA', menu = self.help)

        self.frameUsuarios = Frame(self.root)
        self.frameUsuarios.grid(sticky=N+S+E+W)

    def showContent(self, frameUsuarios):
        self.frameUsuarios.destroy()
        self.frameUsuarios = frameUsuarios(self.root)
        self.frameUsuarios.grid(sticky=N+S+E+W)
        
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


