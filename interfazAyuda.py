from tkinter import *


class Help_Interface(Frame):
    
    def __init__(self, root):
        super().__init__(root)

        self.root = root
        self.root.config(bg='#2F21B9')

        self.color = '#2F21B9'

        self.titulo = Label(self.root, text='INFORMACION DE APLICACION', bg=self.color, fg='white', font=('Times', 20))
        self.titulo.grid(row=0, column=0, columnspan=2, padx=30, pady=30)

        self.titlenombreSistema = Label (self.root, text='NOMBRE DE SISTEMA: ', bg=self.color, fg='#39F7E2', relief='sunken')
        self.titlenombreSistema.grid(row=1, column=0, padx=20, pady=20)

        self.nombreSistema = Label (self.root, text='COOL STORE S.A.', bg=self.color, fg='white', font=('Times'))
        self.nombreSistema.grid(row=1, column=1, padx=20, pady=20, sticky='w')

        self.titleNombreEstudiantes = Label (self.root, text='DESARROLLADORES: ', bg=self.color, fg='#39F7E2', relief='sunken')
        self.titleNombreEstudiantes.grid(row=2, column=0, padx=20, pady=20)

        self.Estud1 = Label (self.root, text='Diego Alejandro Morales Obregón | 202040187', bg=self.color, fg='white', font=('Times'))
        self.Estud1.grid(row=2, column=1, padx=20, pady=20, sticky='w')

        self.Estud2 = Label (self.root, text='María de los Ángeles Aguilar Santiago | 202041639', bg=self.color, fg='white', font=('Times'))
        self.Estud2.grid(row=3, column=1, padx=20, pady=(0, 20), sticky='w')

        self.titleAnio = Label (self.root, text='AÑO: ', bg=self.color, fg='#39F7E2', relief='sunken')
        self.titleAnio.grid(row=4, column=0, padx=20, pady=20)

        self.anio = Label (self.root, text='2023', bg=self.color, fg='white', font=('Times'))
        self.anio.grid(row=4, column=1, padx=20, pady=20, sticky='w')

        self.titleSemestre = Label (self.root, text='SEMESTRE: ', bg=self.color, fg='#39F7E2', relief='sunken')
        self.titleSemestre.grid(row=5, column=0, padx=20, pady=20)

        self.semestre = Label (self.root, text='Segundo', bg=self.color, fg='white', font=('Times'))
        self.semestre.grid(row=5, column=1, padx=20, pady=20, sticky='w')

