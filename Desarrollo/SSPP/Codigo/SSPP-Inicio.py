# -*- coding: utf-8 -*-
import sqlite3
from tkinter import *
from PIL import ImageTk, Image
import subprocess

def abrir_ventana_registro():
    ventana.withdraw()  # Oculta la ventana actual
    subprocess.call(["python", "SSPP-RegistrarPresos.py"])  # Ejecuta el archivo SSPP-ER01.py
    ventana.deiconify()  # Muestra la ventana principal nuevamente

def abrir_ventana_visualizacion():
    ventana.withdraw()  # Oculta la ventana actual
    subprocess.call(["python", "SSPP-VisualizarPresos.py"])  # Ejecuta el archivo SSPP-ER01.py
    ventana.deiconify()  # Muestra la ventana principal nuevamente

def abrir_ventana_modificacion():
    ventana.withdraw()  # Oculta la ventana actual
    subprocess.call(["python", "SSPP-ModificarPresos.py"])  # Ejecuta el archivo SSPP-ER01.py
    ventana.deiconify()  # Muestra la ventana principal nuevamente

def volver_a_SSPP_R01():
    ventana.destroy()
    
# Crear la ventana principal
ventana = Tk()
ventana.title("Sistema de Seguimiento de Perfil de Presos")
ventana.geometry("1200x720")

# Cargar la imagen de fondo
imagen_fondo = Image.open("imagenes\puertaCelda.jpg")
imagen_fondo = imagen_fondo.resize((1200, 720), Image.ANTIALIAS)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Mostrar la imagen de fondo en un widget Label
fondo = Label(ventana, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Botones
boton_registro = Button(ventana, text="Registro de Presos", font=("Arial", 20), command=abrir_ventana_registro)
boton_registro.place(x=400, y=200, width=400, height=100)

boton_visualizacion = Button(ventana, text="Visualización de Presos", font=("Arial", 20), command=abrir_ventana_visualizacion)
boton_visualizacion.place(x=400, y=350, width=400, height=100)

boton_modificacion = Button(ventana, text="Modificación de Datos", font=("Arial", 20), command=abrir_ventana_modificacion)
boton_modificacion.place(x=400, y=500, width=400, height=100)

boton_cerrar_sesion = Button(ventana, text="Cerrar Sesión", font=("Arial", 14), bg="red", fg="white", command=volver_a_SSPP_R01)
boton_cerrar_sesion.place(x=1050, y=20, width=150, height=40)

# Crear la base de datos si no existe
conn = sqlite3.connect("presos.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS presos (nombres TEXT, apellidos TEXT, dni INTENGER,tipo_documento TEXT, documento INTEGER, fecha_nacimiento TEXT, edad INTEGER, tiempo_condena TEXT, pena TEXT, conducta TEXT, talleres TEXT, peligrosidad TEXT)")
conn.commit()
conn.close()

conn = sqlite3.connect("presos.db")
cursor = conn.cursor()

# Crear la tabla "presos" con las columnas especificadas
cursor.execute("""CREATE TABLE IF NOT EXISTS presos (
                    nombres TEXT,
                    apellidos TEXT,
                    tipo_documento TEXT,
                    documento INTEGER,
                    fecha_nacimiento TEXT,
                    edad INTEGER,
                    tiempo_condena TEXT,
                    pena TEXT,
                    conducta TEXT,
                    talleres TEXT,
                    peligrosidad TEXT
                )""")

# Guardar los cambios y cerrar la conexión a la base de datos
conn.commit()
conn.close()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
