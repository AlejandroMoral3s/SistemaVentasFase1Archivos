from tkinter import *
from tkinter import ttk
from usuarios import *
from volcadoInformacion import *

persona1 = Usuario('0', 'Admin', 'Alejandro', 'Morales', '123', '123')
persona2 = Usuario('1', 'Vendedor', 'Gerardo', 'Luna', '125', '125')

usuarios1 = []
volatil = []


root = Tk()

frame = LabelFrame(root, text='PRUEBA DE INGRESO DE USUARIOS')
frame.grid(row=0, column=0, pady=20, padx = 20)

#ID USUARIO
label_id = Label(frame, text='ID: ')
label_id.grid(row = 1, column=0)

entry_id = Entry(frame)
entry_id.focus()
entry_id.grid(row=1, column= 1)

#PERFIL USUARIO
label_perfil = Label(frame, text='PERFIL: ')
label_perfil.grid(row = 1, column=2)

entry_perfil = Entry(frame)
entry_perfil.grid(row=1, column=3)

#NOMBRE USUARIO
label_nombre = Label(frame, text='NOMBRE: ')
label_nombre.grid(row=2, column = 0)

entry_nombre = Entry(frame)
entry_nombre.grid(row=2, column =1)

#APELLIDO USUARIO
label_apellido = Label(frame, text='APELLIDO: ')
label_apellido.grid(row=2, column=2)

entry_apellido = Entry(frame)
entry_apellido.grid(row=2, column=3)

#CLAVE USUARIO
label_clave = Label(frame, text='CLAVE: ')
label_clave.grid(row=3, column=0)

entry_clave = Entry(frame)
entry_clave.grid(row=3, column=1)

#CONFIRMACION CLAVE USUARIO
label_confirmacion = Label(frame, text='CONFIRMACION: ')
label_confirmacion.grid(row=3, column=2)

entry_confirmacion = Entry(frame)
entry_confirmacion.grid(row=3, column=3)

#BUTTON GRABADO
buttonSave = Button(frame, text='GRABAR INFORMACION', command=lambda: almacenarInformacion('usuarios.txt', usuarios1))
buttonSave.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

#BUTTON RECUPERADO
buttonSave = Button(frame, text='RECUPERAR INFORMACION', command=lambda: recuperarInformacion('usuarios.txt'))
buttonSave.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()