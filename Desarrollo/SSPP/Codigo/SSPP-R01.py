# -*- coding: utf-8 -*-
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import subprocess

def iniciar_sesion():
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()

    if not usuario or not contrasena:
        messagebox.showerror("Error", "Por favor, ingresa un usuario y una contraseña.")
    else:
        # Verificar si los datos están en la base de datos
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND contrasena=?", (usuario, contrasena))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso.")
            abrir_archivo()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

def guardar_registro():
    usuario = entrada_usuario_registro.get()
    contrasena = entrada_contrasena_registro.get()

    if not usuario or not contrasena:
        messagebox.showerror("Error", "Por favor, ingresa un usuario y una contraseña.")
    else:
        # Guardar usuario y contraseña en la base de datos
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", (usuario, contrasena))
        conn.commit()
        conn.close()
        messagebox.showinfo("Registro exitoso", "El usuario se registró correctamente.")
        ventana_registro.destroy()

def regresar():
    ventana_registro.destroy()

def registrar():
    global ventana_registro, entrada_usuario_registro, entrada_contrasena_registro
    ventana_registro = Toplevel(ventana)
    ventana_registro.title("SSPP - Registrar usuario")
    ventana_registro.geometry("800x600")

    imagen_fondo_registro = Image.open("Desarrollo/SSPP/Codigo/imagenes/puertaCelda.jpg")
    imagen_fondo_registro = imagen_fondo_registro.resize((800, 600), Image.ANTIALIAS)
    fondo_registro = ImageTk.PhotoImage(imagen_fondo_registro)

    label_fondo_registro = Label(ventana_registro, image=fondo_registro)
    label_fondo_registro.place(x=0, y=0, relwidth=1, relheight=1)

    label_usuario_registro = Label(ventana_registro, text="Usuario:")
    label_usuario_registro.place(x=50, y=50)

    entrada_usuario_registro = Entry(ventana_registro)
    entrada_usuario_registro.place(x=120, y=50)

    label_contrasena_registro = Label(ventana_registro, text="Contraseña:")
    label_contrasena_registro.place(x=30, y=80)

    entrada_contrasena_registro = Entry(ventana_registro, show="*")
    entrada_contrasena_registro.place(x=120, y=80)

    boton_guardar_registro = Button(ventana_registro, text="Guardar", command=guardar_registro)
    boton_guardar_registro.place(x=180, y=120)

    boton_atras = Button(ventana_registro, text="Atrás", command=regresar)
    boton_atras.place(x=250, y=120)

def abrir_archivo():
    ventana.withdraw()  # Oculta la ventana actual
    subprocess.call(["python", "SSPP-Inicio.py"])
    ventana.deiconify()  # Muestra la ventana principal nuevamente

# Crear la ventana principal
ventana = Tk()
ventana.title("SSPP - Login")
ventana.geometry("1200x720")

# Cargar la imagen de fondo
imagen_fondo = Image.open("Desarrollo/SSPP/Codigo/imagenes/puertaCelda.jpg")
imagen_fondo = imagen_fondo.resize((1200, 720), Image.ANTIALIAS)
fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear un widget de lienzo para la imagen de fondo
canvas = Canvas(ventana, width=1200, height=720)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=fondo, anchor="nw")

# Etiqueta de usuario
label_usuario = Label(ventana, text="Usuario:")
label_usuario.place(x=500, y=300)

# Campo de entrada de usuario
entrada_usuario = Entry(ventana)
entrada_usuario.place(x=570, y=300)

# Etiqueta de contraseña
label_contrasena = Label(ventana, text="Contraseña:")
label_contrasena.place(x=480, y=330)

# Campo de entrada de contraseña
entrada_contrasena = Entry(ventana, show="*")
entrada_contrasena.place(x=570, y=330)

# Botón de inicio de sesión
boton_iniciar_sesion = Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)
boton_iniciar_sesion.place(x=500, y=400)

# Botón de registrar
boton_registrar = Button(ventana, text="Registrar", command=registrar)
boton_registrar.place(x=600, y=400)

# Crear la base de datos si no existe
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (usuario TEXT, contrasena TEXT)")
conn.commit()
conn.close()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()