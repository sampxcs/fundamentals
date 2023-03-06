"""INTERFAZ GRAFICA"""
import tkinter as tk
from tkinter import ttk


def sumar():
    """sumar"""
    number01 = int(number_01_input.get())
    number02 = int(number_02_input.get())

    result_label.config(text=f"El resultado es {number01 + number02}")


ventana = tk.Tk()
ventana.title("Calculadora Increible")
ventana.config(width=300, height=200)

number_01_label = ttk.Label(text="Ingresa el primer numero")
number_01_label.place(x=20, y=20)

number_01_input = ttk.Entry()
number_01_input.place(x=180, y=20, width=60)

number_02_label = ttk.Label(text="Ingresa el segundo numero")
number_02_label.place(x=20, y=40)

number_02_input = ttk.Entry()
number_02_input.place(x=180, y=40, width=60)

boton = ttk.Button(text="SUMAR", command=sumar)
boton.place(x=20, y=60)

result_label = ttk.Label(text="")
result_label.place(x=20, y=90)

ventana.mainloop()
