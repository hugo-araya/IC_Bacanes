import tkinter as tk
from tkinter import ttk

def funcion_click():
    accion.configure(text = 'Hicisteis click ***')
    etiqueta.configure(foreground = 'red')

if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.title('Hola Mundo')
    ventana.geometry('300x200')
    ventana.resizable(0,0)

    etiqueta = ttk.Label(ventana, text = 'Hola Raton con Cola')
    etiqueta.grid(column = 0 , row = 0)

    accion = ttk.Button(ventana, text = 'Haz click aqui', command = funcion_click)
    accion.grid(column = 1, row = 0)

    ventana.mainloop()
