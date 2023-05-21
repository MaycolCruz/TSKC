import tkinter as tk
from PIL import ImageTk, Image

def login():
    # Aquí puedes agregar la lógica de autenticación
    # para verificar el nombre de usuario y la contraseña
    # ingresados por el usuario
    print("Iniciando sesión...")

root = tk.Tk()
root.title("Login SSPP")

# Cargar imagen de fondo
image = Image.open("imagenes\puertaCelda.jpg")  # Ruta de la imagen de fondo
image = image.resize((800, 600), Image.ANTIALIAS)  # Ajustar el tamaño de la imagen
background_image = ImageTk.PhotoImage(image)

# Crear un widget Canvas y mostrar la imagen de fondo
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Crear etiquetas y campos de entrada
label_username = tk.Label(root, text="Nombre de usuario:")
label_password = tk.Label(root, text="Contraseña:")
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")

# Ubicar las etiquetas y los campos de entrada en el lienzo
canvas.create_window(400, 250, window=label_username)
canvas.create_window(400, 290, window=entry_username)
canvas.create_window(400, 330, window=label_password)
canvas.create_window(400, 370, window=entry_password)

# Crear el botón de inicio de sesión
button_login = tk.Button(root, text="Iniciar sesión", command=login)
canvas.create_window(400, 410, window=button_login)

root.mainloop()