from tkinter import *
from PIL import ImageTk, Image
import sqlite3

def guardar_datos():
    # Obtener los valores ingresados en los campos de texto
    nombres = entry_nombres.get()
    apellidos = entry_apellidos.get()
    tipo_documento = entry_tipo_documento.get()
    documento = entry_documento.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    edad = entry_edad.get()
    tiempo_condena = entry_tiempo_condena.get()
    pena = entry_pena.get()
    conducta = entry_conducta.get()

    # Guardar los datos en la base de datos
    conn = sqlite3.connect("presos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO presos (nombres, apellidos, tipo_documento, documento, fecha_nacimiento, edad, tiempo_condena, pena, conducta) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (nombres, apellidos, tipo_documento, documento, fecha_nacimiento, edad, tiempo_condena, pena, conducta))
    conn.commit()
    conn.close()

    # Limpiar los campos de texto después de guardar los datos
    entry_nombres.delete(0, END)
    entry_apellidos.delete(0, END)
    entry_tipo_documento.delete(0, END)
    entry_documento.delete(0, END)
    entry_fecha_nacimiento.delete(0, END)
    entry_edad.delete(0, END)
    entry_tiempo_condena.delete(0, END)
    entry_pena.delete(0, END)
    entry_conducta.delete(0, END)

# Crear la ventana principal
ventana = Tk()
ventana.title("SSPP - Registrar Presos")
ventana.geometry("1200x720")

# Cargar la imagen de fondo
imagen_fondo = Image.open("imagenes/puertaCelda.jpg")
imagen_fondo = imagen_fondo.resize((1200, 720), Image.ANTIALIAS)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Mostrar la imagen de fondo en un widget Label
fondo = Label(ventana, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Campos de texto
label_nombres = Label(ventana, text="Nombres:", font=("Arial", 16))
label_nombres.place(x=100, y=100)
entry_nombres = Entry(ventana, font=("Arial", 16))
entry_nombres.place(x=250, y=100)

label_apellidos = Label(ventana, text="Apellidos:", font=("Arial", 16))
label_apellidos.place(x=100, y=150)
entry_apellidos = Entry(ventana, font=("Arial", 16))
entry_apellidos.place(x=250, y=150)

label_tipo_documento = Label(ventana, text="Tipo de Documento:", font=("Arial", 16))
label_tipo_documento.place(x=100, y=200)
entry_tipo_documento = Entry(ventana, font=("Arial", 16))
entry_tipo_documento.place(x=250, y=200)

label_documento = Label(ventana, text="Documento:", font=("Arial", 16))
label_documento.place(x=100, y=250)
entry_documento = Entry(ventana, font=("Arial", 16))
entry_documento.place(x=250, y=250)

label_fecha_nacimiento = Label(ventana, text="Fecha de Nacimiento:", font=("Arial", 16))
label_fecha_nacimiento.place(x=100, y=300)
entry_fecha_nacimiento = Entry(ventana, font=("Arial", 16))
entry_fecha_nacimiento.place(x=250, y=300)

label_edad = Label(ventana, text="Edad:", font=("Arial", 16))
label_edad.place(x=100, y=350)
entry_edad = Entry(ventana, font=("Arial", 16))
entry_edad.place(x=250, y=350)

label_tiempo_condena = Label(ventana, text="Tiempo de Condena:", font=("Arial", 16))
label_tiempo_condena.place(x=100, y=400)
entry_tiempo_condena = Entry(ventana, font=("Arial", 16))
entry_tiempo_condena.place(x=250, y=400)

label_pena = Label(ventana, text="Pena:", font=("Arial", 16))
label_pena.place(x=100, y=450)
entry_pena = Entry(ventana, font=("Arial", 16))
entry_pena.place(x=250, y=450)

label_conducta = Label(ventana, text="Conducta:", font=("Arial", 16))
label_conducta.place(x=100, y=500)
entry_conducta = Entry(ventana, font=("Arial", 16))
entry_conducta.place(x=250, y=500)

# Botón Guardar
boton_guardar = Button(ventana, text="Guardar", font=("Arial", 16), command=guardar_datos)
boton_guardar.place(x=100, y=600, width=250, height=60)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()