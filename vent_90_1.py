import tkinter as tk
from tkinter import ttk

from tkinter import messagebox as mBox

def funcion_click():
    if nombre.get() == '':
        color = 'blue'
    else:
        color = 'red'
    etiqueta.configure(foreground = color, text = 'Hola ' + nombre.get())

def funcion_mensaje():
    #mBox.showinfo("Mensaje uno", 'Mensaje dos') 
    mBox.askyesnocancel("Hola", 'Chao')

if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.title('Hola Mundo')
    ventana.geometry('500x200')
    ventana.resizable(0,0)

    etiqueta = ttk.Label(ventana, text = 'Hola Raton con Cola')
    etiqueta.grid(column = 0 , row = 0)

    nombre = tk.StringVar()
    preguntar_nombre = ttk.Entry(ventana, width = 20, textvariable = nombre)
    preguntar_nombre.grid(column = 0, row = 1)

    accion = ttk.Button(ventana, text = 'Click', command = funcion_click)
    accion.grid(column = 1, row = 1)

    accion1 = ttk.Button(ventana, text = 'Mensaje', command = funcion_mensaje)
    accion1.grid(column = 1, row = 2)

    ventana.mainloop()
