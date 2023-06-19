import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image, ImageFilter

def cerrar_ventana():
    ventana.destroy()

def agregar_perfil():
    # Obtener el preso seleccionado del combobox
    preso_seleccionado = combobox_presos.get()

    if preso_seleccionado == "Seleccione un preso":
        messagebox.showerror("Error", "Por favor, seleccione un preso.")
    else:
        ventana_visualizar_perfiles.place_forget()
        # Obtener los nombres y apellidos del preso seleccionado
        apellidos, nombres = preso_seleccionado.split(", ")

        # Actualizar el texto del label con el nombre y apellido del preso
        label_preso.config(text=f"{nombres} {apellidos}")

        # Conectar a la base de datos "PP.db"
        conn_pp = sqlite3.connect("PP.db")
        cursor_pp = conn_pp.cursor()

        # Obtener el contenido de PP y peligrosidad del preso
        cursor_pp.execute("SELECT PP, peligrosidad FROM presos WHERE apellidos=? AND nombres=?",
                          (apellidos, nombres))
        row = cursor_pp.fetchone()
        pp = row[0]
        peligrosidad = row[1]

        # Cerrar la conexión a la base de datos
        conn_pp.close()

        # Actualizar los cuadros de texto con el contenido de PP y peligrosidad
        cuadro_pp.delete("1.0", END)
        cuadro_pp.insert(END, pp)

        cuadro_nivel_peligrosidad.delete(0, END)
        cuadro_nivel_peligrosidad.insert(END, peligrosidad)

        # Obtener la pena y el tiempo de condena del preso seleccionado
        conn_presos = sqlite3.connect("presos.db")
        cursor_presos = conn_presos.cursor()
        cursor_presos.execute("SELECT pena, tiempo_condena FROM presos WHERE apellidos=? AND nombres=?",
                              (apellidos, nombres))
        row = cursor_presos.fetchone()
        pena = row[0]
        tiempo_condena = row[1]
        conn_presos.close()

        # Actualizar el texto del label con la pena y el tiempo de condena
        label_pena_condena.config(text=f"Pena: {pena}\nCondena: {tiempo_condena} años")

        # Mostrar ventana de agregar perfil
        ventana_agregar_perfil.place(x=0, y=0, width=940, height=590)

def guardar_perfil():
    # Obtener el preso seleccionado del combobox
    preso_seleccionado = combobox_presos.get()

    # Obtener el contenido de PP y peligrosidad ingresado en los cuadros de texto
    pp = cuadro_pp.get("1.0", END).strip()
    peligrosidad = cuadro_nivel_peligrosidad.get()

    # Verificar si se ingresó un valor válido para la peligrosidad (un entero entre 1 y 100)
    if not peligrosidad.isdigit() or not 1 <= int(peligrosidad) <= 100:
        messagebox.showerror("Error", "Ingrese un valor válido para la peligrosidad (entre 1 y 100).")
        return

    # Obtener los nombres y apellidos del preso seleccionado
    apellidos, nombres = preso_seleccionado.split(", ")

    # Conectar a la base de datos "PP.db"
    conn_pp = sqlite3.connect("PP.db")
    cursor_pp = conn_pp.cursor()

    # Actualizar la información de PP y peligrosidad del preso en la base de datos
    cursor_pp.execute("UPDATE presos SET PP=?, peligrosidad=? WHERE apellidos=? AND nombres=?",
                      (pp, peligrosidad, apellidos, nombres))
    conn_pp.commit()

    # Cerrar la conexión a la base de datos
    conn_pp.close()

    messagebox.showinfo("Éxito", "Se actualizó la información con éxito.")

def cancelar_perfil():
    ventana_agregar_perfil.place_forget()

def visualizar_perfiles():
    # Verificar si se ha seleccionado un preso
    preso_seleccionado = combobox_presos.get()
    if preso_seleccionado == "Seleccione un preso":
        messagebox.showerror("Error", "Por favor, seleccione un preso")
        return

    ventana_agregar_perfil.place_forget()
    # Obtener los nombres y apellidos del preso seleccionado
    apellidos, nombres = preso_seleccionado.split(", ")

    # Conectar a la base de datos "PP.db"
    conn_pp = sqlite3.connect("PP.db")
    cursor_pp = conn_pp.cursor()

    # Obtener el contenido de PP y peligrosidad del preso seleccionado
    cursor_pp.execute("SELECT PP, peligrosidad FROM presos WHERE apellidos=? AND nombres=?",
                      (apellidos, nombres))
    row = cursor_pp.fetchone()
    pp = row[0]
    peligrosidad = row[1]

    # Cerrar la conexión a la base de datos
    conn_pp.close()

    # Obtener la pena y el tiempo de condena del preso seleccionado
    conn_presos = sqlite3.connect("presos.db")
    cursor_presos = conn_presos.cursor()
    cursor_presos.execute("SELECT pena, tiempo_condena FROM presos WHERE apellidos=? AND nombres=?",
                          (apellidos, nombres))
    row = cursor_presos.fetchone()
    pena = row[0]
    tiempo_condena = row[1]
    conn_presos.close()


     # Asigna la etiqueta y el fondo en función del rango de peligrosidad
    if peligrosidad >= 1 and peligrosidad <= 20:
        etiqueta = "Aceptable"
        fondo = "pale green"
    elif peligrosidad >= 21 and peligrosidad <= 40:
        etiqueta = "Bajo"
        fondo = "dark green"
    elif peligrosidad >= 41 and peligrosidad <= 60:
        etiqueta = "Medio"
        fondo = "yellow"
    elif peligrosidad >= 61 and peligrosidad <= 80:
        etiqueta = "Alto"
        fondo = "light coral"
    elif peligrosidad >= 81 and peligrosidad <= 100:
        etiqueta = "Muy Alto"
        fondo = "red"
    else:
        etiqueta = "Desconocido"
        fondo = "gray"

    # Actualizar los labels con los datos obtenidos
    label_nombre_preso.config(text=f"Nombre del preso: {nombres} {apellidos}")
    label_pp.config(text=f"Perfil Psicologico: {pp}")
    label_peligrosidad.config(text=f"Nivel de Peligrosidad: {etiqueta}", bg=fondo)
    label_pena.config(text=f"Pena: {pena}")
    label_condena.config(text=f"Condena: {tiempo_condena} años")

    # Mostrar ventana de visualizar perfiles
    ventana_visualizar_perfiles.place(x=0, y=0, width=940, height=590)

# Crear la base de datos "PP.db"
conn_pp = sqlite3.connect("PP.db")
cursor_pp = conn_pp.cursor()

# Crear la tabla "presos" en "PP.db" si no existe
cursor_pp.execute("CREATE TABLE IF NOT EXISTS presos (nombres TEXT, apellidos TEXT, PP TEXT, peligrosidad INTEGER, comentarios TEXT)")

# Copiar valores desde "presos.db" a "PP.db" solo si no existen previamente
conn_presos = sqlite3.connect("presos.db")
cursor_presos = conn_presos.cursor()
cursor_presos.execute("SELECT nombres, apellidos FROM presos")
rows = cursor_presos.fetchall()
for row in rows:
    nombres = row[0]
    apellidos = row[1]
    # Verificar si el preso ya existe en la base de datos "PP.db"
    cursor_pp.execute("SELECT COUNT(*) FROM presos WHERE nombres=? AND apellidos=?", (nombres, apellidos))
    count = cursor_pp.fetchone()[0]
    if count == 0:
        cursor_pp.execute("INSERT INTO presos (nombres, apellidos, PP, peligrosidad) VALUES (?, ?, ?, ?)",
                          (nombres, apellidos, "falta llenar", 0))

# Guardar los cambios y cerrar las conexiones
conn_pp.commit()
conn_pp.close()
conn_presos.close()

# Obtener los apellidos y nombres de la base de datos "PP.db"
conn_pp = sqlite3.connect("PP.db")
cursor_pp = conn_pp.cursor()
cursor_pp.execute("SELECT apellidos, nombres FROM presos")
rows = cursor_pp.fetchall()
presos = ["Seleccione un preso"]
for row in rows:
    apellidos = row[0]
    nombres = row[1]
    presos.append(f"{apellidos}, {nombres}")

# Guardar los cambios y cerrar la conexión
conn_pp.commit()
conn_pp.close()

# Crear la ventana principal
ventana = Tk()
ventana.title("SSPP - Perfil Psicológico")
ventana.geometry("1200x720")

# Cargar la imagen de fondo
imagen_fondo = Image.open("imagenes/puertaCelda.jpg")
imagen_fondo = imagen_fondo.resize((1200, 720), Image.LANCZOS)
imagen_fondo = imagen_fondo.filter(ImageFilter.BLUR)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Mostrar la imagen de fondo en un widget Label
fondo = Label(ventana, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Botón "Atrás"
boton_atras = Button(ventana, text="Atrás", font=("Arial", 16), command=cerrar_ventana)
boton_atras.place(x=1050, y=20, width=100, height=40)

# Crear el contenedor para las ventanas
contenedor_ventanas = Frame(ventana, bg="white")
contenedor_ventanas.place(x=200, y=100, width=950, height=600)

# Ventana de Agregar Perfil
ventana_agregar_perfil = Frame(contenedor_ventanas, bg="white")

# Label con el nombre y apellido del preso
label_preso = Label(ventana_agregar_perfil, text="Preso:", font=("Arial", 16), bg="white")
label_preso.pack(pady=10)

# Cuadro grande editable con el contenido de PP
cuadro_pp = Text(ventana_agregar_perfil, font=("Arial", 12), width=80, height=20)
cuadro_pp.pack()

# Cuadro editable pequeño para el nivel de peligrosidad
label_peligrosidad = Label(ventana_agregar_perfil, text="Nivel de peligrosidad:", font=("Arial", 12), bg="white")
label_peligrosidad.pack(pady=10)

cuadro_nivel_peligrosidad = Entry(ventana_agregar_perfil, font=("Arial", 12), width=10)
cuadro_nivel_peligrosidad.pack()

# Etiqueta para indicar el rango del nivel de peligrosidad
label_rango_peligrosidad = Label(ventana_agregar_perfil, text="Colocar del 1 al 100", font=("Arial", 10), bg="white")
label_rango_peligrosidad.pack()

boton_guardar = Button(ventana_agregar_perfil, text="Guardar", font=("Arial", 16), command=guardar_perfil)
boton_guardar.place(x=350, y=520)

boton_cancelar = Button(ventana_agregar_perfil, text="Cancelar", font=("Arial", 16), command=cancelar_perfil)
boton_cancelar.place(x=500, y=520)

# Crear el label para mostrar la pena y el tiempo de condena
label_pena_condena = Label(ventana_agregar_perfil, text="", font=("Arial", 12), bg="white")
label_pena_condena.place(x=10, y=570, anchor="sw")

# Ventana de Visualizar Perfiles
ventana_visualizar_perfiles = Frame(contenedor_ventanas, bg="white")

# Label para mostrar el nombre del preso
label_nombre_preso = Label(ventana_visualizar_perfiles, text="Nombre del preso:", font=("Arial", 16), bg="white")
label_nombre_preso.pack(pady=10)

# Label para mostrar el contenido de PP
label_pp = Label(ventana_visualizar_perfiles, text="Perfil Psicologico:", font=("Arial", 12), bg="white")
label_pp.pack(pady=10)

# Label para mostrar la peligrosidad
label_peligrosidad = Label(ventana_visualizar_perfiles, text="Nivel de Peligrosidad:", font=("Arial", 12), bg="white")
label_peligrosidad.pack(pady=10)

# Label para mostrar la pena y la condena
label_pena = Label(ventana_visualizar_perfiles, text="Pena:", font=("Arial", 12), bg="white")
label_pena.pack(pady=10)

label_condena = Label(ventana_visualizar_perfiles, text="Condena:", font=("Arial", 12), bg="white")
label_condena.pack(pady=10)

# Ocultar las ventanas iniciales
ventana_agregar_perfil.place_forget()
ventana_visualizar_perfiles.place_forget()

# Combobox para seleccionar el perfil
combobox_presos = ttk.Combobox(ventana, values=presos, font=("Arial", 12), state="readonly")
combobox_presos.current(0)  # Establecer la primera opción como seleccionada
combobox_presos.place(x=10, y=100, width=180)

# Botón "Agregar"
boton_agregar = Button(ventana, text="Agregar o \nModificar", font=("Arial", 16), command=agregar_perfil)
boton_agregar.place(x=10, y=200, width=180, height=60)

# Botón "Visualizar"
boton_visualizar = Button(ventana, text="Visualizar\nPerfil", font=("Arial", 16), command=visualizar_perfiles)
boton_visualizar.place(x=10, y=300, width=180, height=60)

# Mostrar la ventana principal
ventana.mainloop()