from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image, ImageFilter
import sqlite3

def cerrar_ventana():
    ventana.destroy()

def agregar_comentario():
    preso_seleccionado = combo_presos.get()
    if preso_seleccionado == "Seleccionar preso":
        messagebox.showerror("Error", "Por favor, seleccione un preso.")
    else:
        ventana_ver_comentario.place_forget()
        ventana_agregar_comentario.place(x=0, y=0, width=940, height=590)

def guardar_comentario():
    comentario = texto_comentario.get("1.0", END).strip()
    autor = texto_autor.get().strip()

    if not autor:
        autor = "Anónimo"

    if comentario:
        preso_seleccionado = combo_presos.get().split(", ")
        apellidos = preso_seleccionado[0]
        nombres = preso_seleccionado[1]

        # Actualizar la columna de comentarios en la base de datos
        conn = sqlite3.connect("PP.db")
        cursor = conn.cursor()
        cursor.execute("SELECT comentarios FROM presos WHERE apellidos=? AND nombres=?", (apellidos, nombres))
        comentarios_actuales = cursor.fetchone()[0]

        if comentarios_actuales:
            comentarios_nuevos = f"{comentarios_actuales}\n{autor} dijo: {comentario}"
        else:
            comentarios_nuevos = f"{autor} dijo: {comentario}"

        cursor.execute("UPDATE presos SET comentarios=? WHERE apellidos=? AND nombres=?", (comentarios_nuevos, apellidos, nombres))
        conn.commit()
        conn.close()

        # Limpiar los cuadros de texto
        texto_comentario.delete("1.0", END)
        texto_autor.delete(0, END)
        messagebox.showinfo("Éxito", "Comentario guardado exitosamente.")
    else:
        messagebox.showerror("Error", "Por favor, ingrese un comentario.")

def ver_comentarios():
    preso_seleccionado = combo_presos.get()
    if preso_seleccionado == "Seleccionar preso":
        messagebox.showerror("Error", "Por favor, seleccione un preso.")
    else:
        ventana_agregar_comentario.place_forget()
        ventana_ver_comentario.place(x=0, y=0, width=940, height=590)
        mostrar_comentarios(preso_seleccionado)

def mostrar_comentarios(preso):
    # Consultar la base de datos para obtener los comentarios del preso seleccionado
    conn = sqlite3.connect("PP.db")
    cursor = conn.cursor()
    cursor.execute("SELECT comentarios FROM presos WHERE apellidos || ', ' || nombres = ?", (preso,))
    comentarios = cursor.fetchone()
    conn.close()

    # Limpiar cualquier contenido previo en la ventana de Ver Comentario
    for widget in ventana_ver_comentario.winfo_children():
        widget.destroy()

    # Mostrar los comentarios en la ventana
    if comentarios:
        comentarios_texto = comentarios[0]
        etiqueta_comentarios = Label(ventana_ver_comentario, text="Comentarios:", font=("Arial", 16), bg="white")
        etiqueta_comentarios.pack(pady=10)

        # Verificar si hay múltiples comentarios
        if "\n" in comentarios_texto:
            comentarios_lista = comentarios_texto.split("\n")
            scrollbar = Scrollbar(ventana_ver_comentario)
            scrollbar.pack(side=RIGHT, fill=Y)

            comentarios_texto_scroll = Text(ventana_ver_comentario, font=("Arial", 12), yscrollcommand=scrollbar.set)
            comentarios_texto_scroll.pack(expand=True, fill=BOTH)

            scrollbar.config(command=comentarios_texto_scroll.yview)

            for i, comentario in enumerate(comentarios_lista, start=1):
                comentarios_texto_scroll.insert(END, f"{i}. {comentario}\n\n")
        else:
            # Solo hay un comentario
            etiqueta_comentario = Label(ventana_ver_comentario, text=comentarios_texto, font=("Arial", 12), bg="white")
            etiqueta_comentario.pack(pady=10)
    else:
        etiqueta_sin_comentarios = Label(ventana_ver_comentario, text="No hay comentarios.", font=("Arial", 12), bg="white")
        etiqueta_sin_comentarios.pack(pady=10)

# Crear la base de datos "PP" y la tabla "presos"
conn = sqlite3.connect("PP.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS presos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombres TEXT,
                    apellidos TEXT,
                    PP TEXT,
                    peligrosidad INTEGER,
                    comentarios TEXT
                )''')
conn.commit()
conn.close()

# Crear la ventana principal
ventana = Tk()
ventana.title("SSPP - Comentarios")
ventana.geometry("1360x760")

# Cargar la imagen de fondo
imagen_fondo = Image.open("imagenes\puertaCelda.jpg")
imagen_fondo = imagen_fondo.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()), Image.LANCZOS)
imagen_fondo = imagen_fondo.filter(ImageFilter.BLUR)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Mostrar la imagen de fondo en un widget Label
fondo = Label(ventana, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Obtener apellidos y nombres de la base de datos
conn = sqlite3.connect("PP.db")
cursor = conn.cursor()
cursor.execute("SELECT apellidos, nombres FROM presos")
presos = cursor.fetchall()
conn.close()

# Crear una lista de opciones para el ComboBox
opciones = ["Seleccionar preso"] + [f"{apellidos}, {nombres}" for apellidos, nombres in presos]

# ComboBox de presos
combo_presos = ttk.Combobox(ventana, values=opciones)
combo_presos.place(x=20, y=20, width=200, height=30)
combo_presos.current(0)  # Establecer la primera opción como seleccionada por defecto

# Botón "Atrás"
boton_atras = Button(ventana, text="Atrás", font=("Arial", 16), command=cerrar_ventana)
boton_atras.place(x=1050, y=20, width=100, height=40)

# Botón "Agregar comentario"
boton_agregar = Button(ventana, text="Agregar comentario", font=("Arial", 16), command=agregar_comentario)
boton_agregar.place(x=20, y=70, width=200, height=40)

# Botón "Ver comentarios"
boton_ver = Button(ventana, text="Ver comentarios", font=("Arial", 16), command=ver_comentarios)
boton_ver.place(x=20, y=120, width=200, height=40)

# Crear el contenedor para las ventanas
contenedor_ventanas = Frame(ventana, bg="white")
contenedor_ventanas.place(x=250, y=100, width=900, height=600)

# Ventana de Agregar Comentario
ventana_agregar_comentario = Frame(contenedor_ventanas, bg="white")

# Etiqueta "Inserte comentario"
etiqueta_comentario = Label(ventana_agregar_comentario, text="Inserte comentario", font=("Arial", 16), bg="white")
etiqueta_comentario.place(x=20, y=20)

# Cuadro de texto para el comentario
texto_comentario = Text(ventana_agregar_comentario, font=("Arial", 12), height=10, width=80)
texto_comentario.place(x=20, y=60)

# Etiqueta "Autor"
etiqueta_autor = Label(ventana_agregar_comentario, text="Autor", font=("Arial", 16), bg="white")
etiqueta_autor.place(x=20, y=300)

# Cuadro de texto para el autor
texto_autor = Entry(ventana_agregar_comentario, font=("Arial", 12), width=30)
texto_autor.place(x=20, y=340)

# Botón "Guardar"
boton_guardar = Button(ventana_agregar_comentario, text="Guardar", font=("Arial", 16), command=guardar_comentario)
boton_guardar.place(x=20, y=400, width=120, height=40)

# Botón "Cancelar"
boton_cancelar = Button(ventana_agregar_comentario, text="Cancelar", font=("Arial", 16), command=lambda: ventana_agregar_comentario.place_forget())
boton_cancelar.place(x=150, y=400, width=120, height=40)

# Ventana de Ver Comentario
ventana_ver_comentario = Frame(contenedor_ventanas, bg="white")

# Ocultar las ventanas iniciales
ventana_agregar_comentario.place_forget()
ventana_ver_comentario.place_forget()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()