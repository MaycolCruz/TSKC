import tkinter as tk
from PIL import ImageTk, Image
import sqlite3

def registrar_preso():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    dni = int(entry_dni.get())
    edad = int(entry_edad.get())
    otros = entry_otros.get()
    
    conn = sqlite3.connect('Presos.db')
    cursor = conn.cursor()
    
    # Insertar datos en la tabla
    cursor.execute('''INSERT INTO Presos (nombre, apellido, dni, edad, otros)
                      VALUES (?, ?, ?, ?, ?)''', (nombre, apellido, dni, edad, otros))
    
    conn.commit()
    conn.close()
    
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_dni.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_otros.delete(0, tk.END)
    
    label_status.config(text="Preso registrado exitosamente.", fg="green")

def ver_registros():
    conn = sqlite3.connect('Presos.db')
    cursor = conn.cursor()
    
    # Obtener todos los registros de la tabla
    cursor.execute("SELECT * FROM Presos")
    registros = cursor.fetchall()
    
    # Crear una nueva ventana para mostrar los registros
    ventana_registros = tk.Toplevel(root)
    ventana_registros.title("Registros")
    
    # Crear un widget Canvas en la nueva ventana
    canvas_registros = tk.Canvas(ventana_registros, width=800, height=600)
    canvas_registros.pack(fill="both", expand=True)
    
    # Mostrar los registros en el Canvas
    y_pos = 100
    for registro in registros:
        registro_texto = f"ID: {registro[0]}, Nombre: {registro[1]}, Apellido: {registro[2]}, DNI: {registro[3]}, Edad: {registro[4]}, Otros: {registro[5]}"
        canvas_registros.create_text(400, y_pos, text=registro_texto, font=("Arial", 12), fill="white")
        y_pos += 30
    
    # Cambiar el fondo de la ventana de registros
    image_registros = ImageTk.PhotoImage(Image.open("imagenes\puertaCelda.jpg").resize((800, 600), Image.ANTIALIAS))
    background_item_registros = canvas_registros.create_image(0, 0, image=image_registros, anchor="nw")
    canvas_registros.lower(background_item_registros)  # Colocar el fondo detrás de los elementos de texto

root = tk.Tk()
root.title("Sistema de Registro de Presos")

# Cargar imagen de fondo
image = Image.open("imagenes\puertaCelda.jpg")
image = image.resize((800, 600), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image)

# Crear un widget Canvas y mostrar la imagen de fondo
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
background_item = canvas.create_image(0, 0, image=background_image, anchor="nw")



label_nombre = tk.Label(root, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

label_apellido = tk.Label(root, text="Apellido:")
label_apellido.pack()
entry_apellido = tk.Entry(root)
entry_apellido.pack()

label_dni = tk.Label(root, text="DNI:")
label_dni.pack()
entry_dni = tk.Entry(root)
entry_dni.pack()

label_edad = tk.Label(root, text="Edad:")
label_edad.pack()
entry_edad = tk.Entry(root)
entry_edad.pack()

label_otros = tk.Label(root, text="Otros:")
label_otros.pack()
entry_otros = tk.Entry(root)
entry_otros.pack()

button_registrar = tk.Button(root, text="Registrar", command=registrar_preso)
button_registrar.pack()

canvas.create_window(350, 250, window=label_nombre)
canvas.create_window(450, 250, window=entry_nombre)
canvas.create_window(350, 290, window=label_apellido)
canvas.create_window(450, 290, window=entry_apellido)
canvas.create_window(350, 330, window=label_dni)
canvas.create_window(450, 330, window=entry_dni)
canvas.create_window(350, 370, window=label_edad)
canvas.create_window(450, 370, window=entry_edad)
canvas.create_window(350, 410, window=label_otros)
canvas.create_window(450, 410, window=entry_otros)

label_status = tk.Label(root, text="")
label_status.pack()

button_ver_registros = tk.Button(root, text="Ver Registros", command=ver_registros)
canvas.create_window(400, 450, window=button_ver_registros)

root.mainloop()