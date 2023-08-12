from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('500x200')

frame1 = LabelFrame(root, background='red', width='250', height='200')
frame1.grid(row=0, column=0)

frame2 = Frame(root, background='lightBlue', width='250', height='200')
frame2.grid(row=0, column=1)

labelPrueba = Label(frame1, text='ESTO ES UNA PRUEBA')
labelPrueba.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()