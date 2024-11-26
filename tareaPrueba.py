from tkinter import *
from tkinter import ttk
from math import pi

ventana = Tk() 
ventana.title("Ecuaciones Algebraicas y Geométricas")
ventana.config(width=600, height=700)

frame = ttk.Frame(ventana)

notebook = ttk.Notebook(ventana)
notebook.pack(fill="both")

pestaña1 = Frame(notebook, width=600, height=400)
pestaña2 = Frame(notebook, width=600, height=400)

notebook.add(pestaña1, text="Área")
notebook.add(pestaña2, text="Ecuación")

# PESTAÑA 1

def mostrar_seleccion():
    figura = var.get()
    label.config(text=f"Seleccionaste: {figura}")
    # Ocultar todos los campos de entrada
    ocultar_campos()
    # Mostrar los campos según la opción seleccionada
    if figura == "Círculo":
        mostrar_circulo()
    elif figura == "Triángulo":
        mostrar_triangulo()
    elif figura == "Cuadrado":
        mostrar_cuadrado()
    elif figura == "Rectángulo":
        mostrar_rectangulo()

def ocultar_campos():
    entry_circulo.place_forget()
    entry_triangulo.place_forget()
    entry_base.place_forget()
    entry_cuadrado.place_forget()
    entry_base_rectangulo.place_forget()
    entry_altura_rectangulo.place_forget()
    resultado_circulo.place_forget()
    resultado_triangulo.place_forget()
    resultado_cuadrado.place_forget()
    resultado_rectangulo.place_forget()

def mostrar_circulo():
    entry_circulo.place(x=160, y=30)
    boton_circulo.place(x=210, y=30)
    resultado_circulo.place(x=160, y=60)

def mostrar_triangulo():
    entry_triangulo.place(x=160, y=80)
    entry_base.place(x=230, y=80)
    boton_triangulo.place(x=280, y=80)
    resultado_triangulo.place(x=160, y=110)

def mostrar_cuadrado():
    entry_cuadrado.place(x=160, y=120)
    boton_cuadrado.place(x=210, y=120)
    resultado_cuadrado.place(x=160, y=150)

def mostrar_rectangulo():
    entry_base_rectangulo.place(x=260, y=260)
    entry_altura_rectangulo.place(x=260, y=160)
    boton_rectangulo.place(x=320, y=160)
    resultado_rectangulo.place(x=160, y=190)

var = StringVar()
label = Label(pestaña1, text="Selecciona una opción")
label.place(x=20, y=200)

radio1 = Radiobutton(pestaña1, text="Círculo", variable=var, value="Círculo", command=mostrar_seleccion)
radio1.place(x=20, y=30)
radio2 = Radiobutton(pestaña1, text="Triángulo", variable=var, value="Triángulo", command=mostrar_seleccion)
radio2.place(x=20, y=60)
radio3 = Radiobutton(pestaña1, text="Cuadrado", variable=var, value="Cuadrado", command=mostrar_seleccion)
radio3.place(x=20, y=90)
radio4 = Radiobutton(pestaña1, text="Rectángulo", variable=var, value="Rectángulo", command=mostrar_seleccion)
radio4.place(x=20, y=120)

# Cálculo para el círculo
def calcular_circulo():
    try:
        radio = float(entry_circulo.get())
        area = pi * radio**2
        resultado_circulo.config(text=f"El área es: {area:.2f}")
    except ValueError:
        resultado_circulo.config(text="Por favor ingresa un número válido")

# Cálculo para el triángulo
def calcular_triangulo():
    try:
        altura = float(entry_triangulo.get())
        base = float(entry_base.get())
        area_triangulo = (base * altura) / 2
        resultado_triangulo.config(text=f"El área es: {area_triangulo:.2f}")
    except ValueError:
        resultado_triangulo.config(text="Por favor ingresa un número válido")

# Cálculo para el cuadrado
def calcular_cuadrado():
    try:
        lado = float(entry_cuadrado.get())
        area_cuadrado = lado ** 2
        resultado_cuadrado.config(text=f"El área es: {area_cuadrado:.2f}")
    except ValueError:
        resultado_cuadrado.config(text="Por favor ingresa un número válido")

# Cálculo para el rectángulo
def calcular_rectangulo():
    try:
        base = float(entry_base_rectangulo.get())
        altura = float(entry_altura_rectangulo.get())
        area_rectangulo = base * altura
        resultado_rectangulo.config(text=f"Área del rectángulo: {area_rectangulo:.2f} unidades cuadradas")
    except ValueError:
        resultado_rectangulo.config(text="Por favor ingresa un número válido")

# Componentes para el Círculo
radio_circulo = Label(pestaña1, text="Círculo")
radio_circulo.place(x=100, y=10)
etiq_radio = Label(pestaña1, text="Radio")
etiq_radio.place(x=100, y=30)
entry_circulo = Entry(pestaña1, width=6)
resultado_circulo = Label(pestaña1)
boton_circulo = Button(pestaña1, text="Calcular", command=calcular_circulo)

# Componentes para el Triángulo
lado_triangulo = Label(pestaña1, text="Triángulo")
lado_triangulo.place(x=100, y=60)
etiq_altura = Label(pestaña1, text="Altura")
etiq_altura.place(x=200, y=100)
entry_triangulo = Entry(pestaña1, width=6)
etiq_base = Label(pestaña1, text="Base")
etiq_base.place(x=200, y=80)
entry_base = Entry(pestaña1, width=6)
boton_triangulo = Button(pestaña1, text="Calcular", command=calcular_triangulo)
resultado_triangulo = Label(pestaña1)

# Componentes para el Cuadrado
radio_cuadrado = Label(pestaña1, text="Cuadrado")
radio_cuadrado.place(x=100, y=100)
etiq_lado = Label(pestaña1, text="Lado")
etiq_lado.place(x=120, y=120)
entry_cuadrado = Entry(pestaña1, width=6)
boton_cuadrado = Button(pestaña1, text="Calcular", command=calcular_cuadrado)
resultado_cuadrado = Label(pestaña1)

# Componentes para el Rectángulo
base_rectangulo = Label(pestaña1, text="Base")
base_rectangulo.place(x=120, y=160)
entry_base_rectangulo = Entry(pestaña1, width=6)
altura_rectangulo = Label(pestaña1, text="Altura")
altura_rectangulo.place(x=210, y=160)
entry_altura_rectangulo = Entry(pestaña1, width=6)
boton_rectangulo = Button(pestaña1, text="Calcular", command=calcular_rectangulo)
resultado_rectangulo = Label(pestaña1)

# PESTAÑA 2 - Ecuación
def calcular_resultado():
    try:
        x = int(entry_ecua_x.get())
        y = int(entry_ecua_y.get())
        z = ((2 * x + 3 * y) ** 2) / 5
        resultado_z.config(state="normal")
        resultado_z.delete(0, END)
        resultado_z.insert(0, f"{z:.2f}")
        resultado_z.config(state="readonly")
    except ValueError:
        resultado_z.config(state="normal")
        resultado_z.delete(0, END)
        resultado_z.insert(0, "Error")
        resultado_z.config(state="readonly")

ecua_x = Label(pestaña2, text="X = ")
ecua_x.place(x=40, y=50)

entry_ecua_x = Entry(pestaña2)
entry_ecua_x.insert(0, "0")
entry_ecua_x.place(x=60, y=50)

ecua_y = Label(pestaña2, text="Y = ")
ecua_y.place(x=160, y=50)

entry_ecua_y = Entry(pestaña2)
entry_ecua_y.insert(0, "0")
entry_ecua_y.place(x=180, y=50)

ecua_calcular = Button(pestaña2, text="Calcular", command=calcular_resultado)
ecua_calcular.place(x=120, y=110)

resultado_z = Entry(pestaña2, state="readonly")
resultado_z.place(x=120, y=150)

ventana.mainloop()

