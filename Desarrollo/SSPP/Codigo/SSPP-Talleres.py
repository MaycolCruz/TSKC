from tkinter import *
from PIL import ImageTk, Image
import sqlite3

def cerrar_ventana():
    ventana.destroy()

# Función para mostrar los talleres seleccionados
def mostrar_talleres_seleccionados():
    talleres_seleccionados = []
    if mecanica_var.get():
        talleres_seleccionados.append("Mecánica")
    if orfebreria_var.get():
        talleres_seleccionados.append("Orfebrería")
    if cocina_var.get():
        talleres_seleccionados.append("Cocina")
    if otros_var.get():
        talleres_seleccionados.append("Otros")

    talleres_seleccionados_label.config(text="Talleres seleccionados: " + ", ".join(talleres_seleccionados))

def guardar_talleres():
    preso = preso_seleccionado.get()
    talleres_seleccionados = []
    if mecanica_var.get():
        talleres_seleccionados.append("Mecánica")
    if orfebreria_var.get():
        talleres_seleccionados.append("Orfebrería")
    if cocina_var.get():
        talleres_seleccionados.append("Cocina")
    if otros_var.get():
        talleres_seleccionados.append("Otros")

    conn = sqlite3.connect("presos.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE presos SET talleres = ? WHERE apellidos || ', ' || nombres = ?", (", ".join(talleres_seleccionados), preso))
    conn.commit()
    conn.close()

# Función para actualizar la visibilidad de los checkboxes
def actualizar_visibilidad_checkboxes(*args):
    if preso_seleccionado.get() == "Seleccione preso":
        mecanica_checkbox.place_forget()
        orfebreria_checkbox.place_forget()
        cocina_checkbox.place_forget()
        otros_checkbox.place_forget()
        guardar_button.place_forget()
    else:
        mecanica_checkbox.place(x=500, y=150)
        orfebreria_checkbox.place(x=500, y=200)
        cocina_checkbox.place(x=500, y=250)
        otros_checkbox.place(x=500, y=300)
        guardar_button.place(x=500, y=400, width=200, height=50)
        
        conn = sqlite3.connect("presos.db")
        cursor = conn.cursor()
        cursor.execute("SELECT talleres FROM presos WHERE apellidos || ', ' || nombres = ?", (preso_seleccionado.get(),))
        talleres = cursor.fetchone()[0]
        conn.close()

        talleres_seleccionados = talleres.split(", ") if talleres else []
        mecanica_var.set("Mecánica" in talleres_seleccionados)
        orfebreria_var.set("Orfebrería" in talleres_seleccionados)
        cocina_var.set("Cocina" in talleres_seleccionados)
        otros_var.set("Otros" in talleres_seleccionados)

# Crear la ventana principal
ventana = Tk()
ventana.title("SSPP - Modificar Presos")
ventana.geometry("1360x760")

# Cargar la imagen de fondo
imagen_fondo = Image.open("Desarrollo/SSPP/Codigo/imagenes/puertaCelda.jpg")
imagen_fondo = imagen_fondo.resize((1200, 720), Image.LANCZOS)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Mostrar la imagen de fondo en un widget Label
fondo = Label(ventana, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Botón "Atrás"
boton_atras = Button(ventana, text="Atrás", font=("Arial", 16), command=cerrar_ventana)
boton_atras.place(x=1050, y=20, width=100, height=40)

# Lista desplegable de selección de preso
preso_seleccionado = StringVar(ventana)
preso_seleccionado.set("Seleccione preso")

conn = sqlite3.connect("presos.db")
cursor = conn.cursor()
cursor.execute("SELECT apellidos, nombres FROM presos ORDER BY apellidos")
rows = cursor.fetchall()
presos = ["Seleccione preso"] + [f"{apellido}, {nombre}" for apellido, nombre in rows]
conn.close()

preso_dropdown = OptionMenu(ventana, preso_seleccionado, *presos)
preso_dropdown.config(font=("Arial", 16))
preso_dropdown.place(x=300, y=100, width=300, height=40)

# Variables para almacenar los valores de los checkboxes
mecanica_var = IntVar()
orfebreria_var = IntVar()
cocina_var = IntVar()
otros_var = IntVar()

# Checkboxes de los talleres
mecanica_checkbox = Checkbutton(ventana, text="Mecanica", variable=mecanica_var, font=("Arial", 16))
orfebreria_checkbox = Checkbutton(ventana, text="Orfebrería", variable=orfebreria_var, font=("Arial", 16))
cocina_checkbox = Checkbutton(ventana, text="Cocina", variable=cocina_var, font=("Arial", 16))
otros_checkbox = Checkbutton(ventana, text="Otros", variable=otros_var, font=("Arial", 16))

# Registrar función para actualizar la visibilidad de los checkboxes cuando se selecciona un preso
preso_seleccionado.trace("w", actualizar_visibilidad_checkboxes)

# Label para mostrar los talleres seleccionados
talleres_seleccionados_label = Label(ventana, text="Talleres seleccionados:", font=("Arial", 16))
talleres_seleccionados_label.place(x=500, y=350)

# Botón para mostrar los talleres seleccionados
mostrar_talleres_button = Button(ventana, text="Mostrar Talleres", font=("Arial", 16), command=mostrar_talleres_seleccionados)
mostrar_talleres_button.place(x=500, y=400, width=200, height=50)

# Botón para guardar los talleres seleccionados
guardar_button = Button(ventana, text="Guardar", font=("Arial", 16), command=guardar_talleres)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()