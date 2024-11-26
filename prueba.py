import tkinter as tk
from tkinter import ttk
from math import pi, sqrt

ventana=tk.Tk()
ventana.title("Figuras geometricas y algebraica ")

frame = ttk.Frame(ventana)
notebook = ttk.Notebook(ventana)
notebook.pack()

pestaña1 = tk.Frame(notebook)
notebook.add(pestaña1, text="Areas ")
pestaña2 = tk.Frame(notebook)
notebook.add(pestaña2, text="Ecuacion ")

# PESTAÑA 1

def calcular_circulo ():
    try:
        radio = float(entry_circulo.get())
        area = pi*radio**2
        resultado_circulo.config(text=f"Area del circulo {area:.2} unidades cuadradas ")
    except ValueError:
        resultado_circulo.config(text="Por favor ingresa un numero valido ")

radio_circulo=tk.Label(pestaña1, text="Circulo ")
radio_circulo.pack()
entry_circulo=tk.Entry(pestaña1)
entry_circulo.pack()
boton_circulo=tk.Button(pestaña1, text="Calcular area ", command = calcular_circulo)
boton_circulo.pack()
resultado_circulo=tk.Label(pestaña1, text="Area ")
resultado_circulo.pack()

def calcular_triangulo ():
    try:
        lado = float(entry_triangulo.get())
        area = (lado ** 2)(sqrt(3)/4)
        resultado_triangulo.config(text=f"Area del triangulo {area:.2f} unidades cuadradas ")
    except ValueError:
        resultado_circulo.config(text="Por favor ingresa un numero valido ")

lado_triangulo=tk.Label(pestaña1, text="Triangulo ")
lado_triangulo.pack()
entry_triangulo=tk.Entry(pestaña1)
entry_triangulo.pack()
boton_triangulo=tk.Button(pestaña1, text="Calcular area ", command = calcular_triangulo)
boton_triangulo.pack()
resultado_triangulo=tk.Label(pestaña1, text="Area ")
resultado_triangulo.pack()

def calcular_cuadrado ():
    try:
        lado = float(entry_cuadrado.get())
        area = lado ** 2
        resultado_cuadrado.config(text=f"Area del cuadrado {area:.2} unidades cuadradas ")
    except ValueError:
        resultado_circulo.config(text="Por favor ingresa un numero valido ")

radio_cuadrado=tk.Label(pestaña1, text="Cuadrado ")
radio_cuadrado.pack()
entry_cuadrado=tk.Entry(pestaña1)
entry_cuadrado.pack()
boton_cuadrado=tk.Button(pestaña1, text="Calcular area ", command = calcular_cuadrado)
boton_cuadrado.pack()
resultado_cuadrado=tk.Label(pestaña1, text="Area ")
resultado_cuadrado.pack()

def calcular_rectangulo ():
    try:
        base = float(entry_base_rectangulo.get())
        altura = float(entry_altura_rectangulo.get())
        area = base * altura
        resultado_rectangulo.config(text=f"Area del rectangulo {area:.2} unidades cuadradas ")
    except ValueError:
        resultado_rectangulo.config(text="Por favor ingresa un numero valido ")

base_rectangulo=tk.Label(pestaña1, text="Base ")
base_rectangulo.pack()
entry_base_rectangulo=tk.Entry(pestaña1)
entry_base_rectangulo.pack()
altura_rectangulo=tk.Label(pestaña1, text="Altura ")
altura_rectangulo.pack()
entry_altura_rectangulo=tk.Entry(pestaña1)
entry_altura_rectangulo.pack()
boton_rectangulo=tk.Button(pestaña1, text="Calcular area ", command = calcular_rectangulo)
boton_rectangulo.pack()
resultado_rectangulo=tk.Label(pestaña1, text="Area ")
resultado_rectangulo.pack()

# PESTAÑA 2
ecua_x = tk.Label(pestaña2, text="X = ")
ecua_x.pack()

ecua_y = tk.Label(pestaña2, text="Y= ")
ecua_y.pack()

ecua_z = tk.Label(pestaña2, text="Z = ")
ecua_z.pack()

resultado_z=tk.Label(pestaña2, text="Ecuacion")
resultado_z.pack()

cuadro = tk.Frame(pestaña2)
cuadro.pack()

def aumentar ():
    try:
        numero = int(entry_ecuacion.get())
        entry_ecuacion.delete(0, tk.END)
        entry_ecuacion.insert(0, str(numero + 1))
    except ValueError:
        entry_ecuacion.delete(0,tk.END)
        entry_ecuacion(0, "0")

def disminuir ():
    try:
        numero = int(entry_ecuacion.get())
        entry_ecuacion.delete(0, tk.END)
        entry_ecuacion.insert(0, str(numero - 1))
    except ValueError:
        entry_ecuacion.delete(0,tk.END)
        entry_ecuacion(0, "0")

entry_ecuacion = tk.Entry(cuadro, )
entry_ecuacion.insert(0, "0")
entry_ecuacion.pack()

bot_aut=tk.Button(cuadro, command=aumentar)
bot_aut.pack()
bot_dis=tk.Button(cuadro, command=disminuir)
bot_dis.pack()

cal_ecua=tk.Button(pestaña2, text="Calcular ecuacion ")
cal_ecua.pack()

ventana.mainloop()
