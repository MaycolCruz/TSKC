from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import ttk

def cerrar_ventana():
    ventana.destroy()

def ordenar_por_edad():
    items = [(tree.set(item, "edad"), item) for item in tree.get_children("")]
    items.sort(reverse=True)
    for index, (_, item) in enumerate(items):
        tree.move(item, "", index)

def ordenar_por_condena():
    items = [(tree.set(item, "tiempo_condena"), item) for item in tree.get_children("")]
    items.sort(reverse=True)
    for index, (_, item) in enumerate(items):
        tree.move(item, "", index)

# Crear la ventana principal
ventana = Tk()
ventana.title("SSPP - Visualizar Presos")
ventana.geometry("1200x720")

# Cargar la imagen de fondo
imagen_fondo = Image.open("imagenes/puertaCelda.jpg")
imagen_fondo = imagen_fondo.resize((1200, 720), Image.ANTIALIAS)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Mostrar la imagen de fondo en un widget Label
fondo = Label(ventana, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Crear el Treeview
tree = ttk.Treeview(ventana)
tree["columns"] = ("nombres", "apellidos", "tipo_documento", "documento", "fecha_nacimiento", "edad", "tiempo_condena", "pena", "conducta")

# Configurar las columnas del Treeview
tree.column("#0", width=0, stretch=NO)
tree.column("nombres", anchor=W, width=150)
tree.column("apellidos", anchor=W, width=150)
tree.column("tipo_documento", anchor=W, width=150)
tree.column("documento", anchor=W, width=150)
tree.column("fecha_nacimiento", anchor=W, width=150)
tree.column("edad", anchor=W, width=150)
tree.column("tiempo_condena", anchor=W, width=150)
tree.column("pena", anchor=W, width=150)
tree.column("conducta", anchor=W, width=150)

# Configurar los encabezados de las columnas
tree.heading("#0", text="")
tree.heading("nombres", text="Nombres")
tree.heading("apellidos", text="Apellidos")
tree.heading("tipo_documento", text="Tipo de Documento")
tree.heading("documento", text="Documento")
tree.heading("fecha_nacimiento", text="Fecha de Nacimiento")
tree.heading("edad", text="Edad", command=ordenar_por_edad)  # Agregar comando para ordenar por edad
tree.heading("tiempo_condena", text="Tiempo de Condena", command=ordenar_por_condena)  # Agregar comando para ordenar por tiempo de condena
tree.heading("pena", text="Pena")
tree.heading("conducta", text="Conducta")

# Obtener los datos de la base de datos y mostrarlos en el Treeview
conn = sqlite3.connect("presos.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM presos")
rows = cursor.fetchall()
for row in rows:
    tree.insert("", END, text="", values=row)

conn.close()

# Mostrar el Treeview en la ventana
tree.place(x=100, y=100, width=1000, height=500)

# Botón "Atrás"
boton_atras = Button(ventana, text="Atrás", font=("Arial", 16), command=cerrar_ventana)
boton_atras.place(x=1050, y=20, width=100, height=40)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
 