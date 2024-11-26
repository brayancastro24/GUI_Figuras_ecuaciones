from tkinter import *
from tkinter import ttk
from math import pi

ventana=Tk() 
ventana.title ("ecuaciones algebraicas y geometricas ")
ventana.config(width=600, height=700)

frame = ttk.Frame(ventana)

notebook = ttk.Notebook(ventana)
notebook.pack(fill="both")

pestaña1 = Frame(notebook, width=600, height=400,)
pestaña2 = Frame(notebook, width=600, height=400,)

notebook.add(pestaña1, text="Area ")
notebook.add(pestaña2, text="Ecuacion ")

# PESTAÑA 1

def mostar_seleccion ():
    figura =var.get()
    label.config(text=f"seleccionaste: {figura}")
    
var = StringVar()

radio1 = Radiobutton(pestaña1, text="Circulo", variable = var, value="Opcion 1",  command=mostar_seleccion)
radio1.place(x=20,y=30)
radio2 = Radiobutton(pestaña1, text="Triangulo", variable = var, value="Opcion 2", command=mostar_seleccion)
radio2.place(x=20, y=60)
radio3 = Radiobutton(pestaña1, text="Cuadrado", variable = var, value="Opcion 3", command=mostar_seleccion)
radio3.place(x=20, y=90)
radio4 = Radiobutton(pestaña1, text="Rectangulo", variable = var, value="Opcion 4", command=mostar_seleccion)
radio4.place(x=20, y=120)

label = Label(pestaña1, text="Selecciona una opcion ")

def calcular_circulo ():
    try:
        radio = float(entry_circulo.get())
        area = pi*radio**2
        resultado_circulo.config(text=f" El area es: {area:.2f} ")
    except ValueError:
        resultado_circulo.config(text="Por favor ingresa un numero valido ")

radio_circulo=Label(pestaña1, text="Circulo ")
radio_circulo.place(x=100, y=10)
etiq_radio=Label(pestaña1, text="Radio")
etiq_radio.place(x=100, y=30)
entry_circulo=Entry(pestaña1, width=6)
entry_circulo.place(x=160, y=30)
boton_circulo=Button(pestaña1, text="Calcular", command = calcular_circulo)
boton_circulo.place(x=210, y=30)
resultado_circulo=Label(pestaña1,)
resultado_circulo.place(x=280, y=30)

def calcular_triangulo ():
    try:
        Altura= float(entry_triangulo.get())
        Base=float(entry_base.get())
        area_tr = (Base * Altura)/2
        resultado_triangulo.config(text=f"El area es: {area_tr:.2f} ")
    except ValueError:
        resultado_circulo.config(text="Por favor ingresa un numero valido ")

lado_triangulo=Label(pestaña1, text="Triangulo ")
lado_triangulo.place(x=100, y=60)
etiq_altura=Label(pestaña1, text="Altura")
etiq_altura.place(x=100, y=80)
entry_triangulo=Entry(pestaña1, width=6)
entry_triangulo.place(x=160, y=80)
etiq_base=Label(pestaña1, text="Base ")
etiq_base.place(x=200, y=80)
entry_base=Entry(pestaña1, width=6)
entry_base.place(x=230, y=80)
boton_triangulo=Button(pestaña1, text="Calcular", command = calcular_triangulo)
boton_triangulo.place(x=280, y=80)
resultado_triangulo=Label(pestaña1,)
resultado_triangulo.place(x=340, y=80)

def calcular_cuadrado ():
    try:
        lado = float(entry_cuadrado.get())
        area_cuad = lado ** 2
        resultado_cuadrado.config(text=f"El area es: {area_cuad:.2f} ")
    except ValueError:
        resultado_circulo.config(text="Por favor ingresa un numero valido ")

radio_cuadrado=Label(pestaña1, text="Cuadrado ")
radio_cuadrado.place(x=100, y=100)
etiq_lado=Label(pestaña1, text="Lado")
etiq_lado.place(x=120, y= 120)
entry_cuadrado=Entry(pestaña1, width=6)
entry_cuadrado.place(x=160, y=120)
boton_cuadrado=Button(pestaña1, text="Calcular", command = calcular_cuadrado)
boton_cuadrado.place(x=210, y=120)
resultado_cuadrado=Label(pestaña1,)
resultado_cuadrado.place(x=270, y=120)

def calcular_rectangulo ():
    try:
        base = float(entry_base_rectangulo.get())
        altura = float(entry_altura_rectangulo.get())
        area = base * altura
        resultado_rectangulo.config(text=f"Area del rectangulo {area:.2f} unidades cuadradas ")
    except ValueError:
        resultado_rectangulo.config(text="Por favor ingresa un numero valido ")

base_rectangulo=Label(pestaña1, text="Base ")
base_rectangulo.place(x=120, y=160)
entry_base_rectangulo=Entry(pestaña1, width=6)
entry_base_rectangulo.place(x=160, y=160)
altura_rectangulo=Label(pestaña1, text="Altura ")
altura_rectangulo.place(x=210, y=160)
entry_altura_rectangulo=Entry(pestaña1, width=6)
entry_altura_rectangulo.place(x=260, y=160)
boton_rectangulo=Button(pestaña1, text="Calcular", command = calcular_rectangulo)
boton_rectangulo.place(x=320, y=160)
resultado_rectangulo=Label(pestaña1,)
resultado_rectangulo.place(x=380, y=160)

# PESTAÑA 2

def calcular_resultado():
    try:
        x = int(entry_ecua_x.get())
        Y = int(entry_ecua_y.get())
        z = ((2 * x + 3 * Y) ** 2) / 5
        resultado_z.config(state="normal")  # Habilitar edición temporal
        resultado_z.delete(0, END)      # Borrar el contenido actual
        resultado_z.insert(0, f"{z:.2f}")  # Insertar el resultado formateado
        resultado_z.config(state="readonly")  # Volver a ponerlo como solo lectura
    except ValueError:
        resultado_z.config(state="normal")
        resultado_z.delete(0, END)
        resultado_z.insert(0, "Error")
        resultado_z.config(state="readonly")

ecua_x = Label(pestaña2, text="X = ")
ecua_x.place(x = 40, y= 50)

entry_ecua_x = Entry (pestaña2)
entry_ecua_x.insert(0, "0")
entry_ecua_x.place(x=60, y=50)

ecua_y = Label(pestaña2, text="Y= ")
ecua_y.place(x= 40, y= 70)

entry_ecua_y=Entry(pestaña2)
entry_ecua_y.insert(0, "0")
entry_ecua_y.place(x=60, y=70)

metodo = Label(pestaña2, text="Ecuacion Z = (2X + 3Y)^2 / 5")
metodo.place(x=50, y= 90)

ecua_z = Label(pestaña2, text="Z = ")
ecua_z.place(x=40, y=110)

resultado_z= Entry(pestaña2, state="readonly")
resultado_z.place(x=70, y=110)

botresul = Button(pestaña2, text="Calcular ", command= calcular_resultado)
botresul.place(x=60, y=140)
def aumentar ():
    try:
        x = int(entry_ecua_x.get())
        Y = int(entry_ecua_y.get())
        entry_ecua_x.delete(0, END)
        entry_ecua_x.insert(0, str(x + 1))
        entry_ecua_y.delete(0, END)
        entry_ecua_y.insert(0, str(x + 1))
    except ValueError:
        entry_ecua_x.delete(0, END)
        entry_ecua_x(0, "0")  
        entry_ecua_y.delete(0, END)
        entry_ecua_y(0, "0")     

def disminuir ():
    try:
        x = int(entry_ecua_x.get())
        Y = int(entry_ecua_y.get())
        entry_ecua_x.delete(0, END)
        entry_ecua_x.insert(0, str(x - 1))
        entry_ecua_y.delete(0, END)
        entry_ecua_y.insert(0, str(x - 1))
    except ValueError:
        entry_ecua_x.delete(0, END)
        entry_ecua_x(0, "0")  
        entry_ecua_y.delete(0, END)
        entry_ecua_y(0, "0")

butonaut=Button(pestaña2, width=2, height= 1, text="+ ", command = aumentar)
butonaut.place(x=180, y=50)
butony=Button(pestaña2,width=2, height=1, text= "- ", command= disminuir)
butony.place(x=180, y = 70)

ventana.mainloop()
#agregando un cambio 