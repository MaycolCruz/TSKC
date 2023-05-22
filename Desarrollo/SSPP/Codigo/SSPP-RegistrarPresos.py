from tkinter import *
from PIL import ImageTk, Image

# Crear la ventana principal
ventana = Tk()
ventana.title("SSPP - Regisrtar Presos")
ventana.geometry("1200x720")

# Cargar la imagen de fondo
imagen_fondo = Image.open("imagenes/puertaCelda.jpg")
imagen_fondo = imagen_fondo.resize((1200, 720), Image.ANTIALIAS)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Mostrar la imagen de fondo en un widget Label
fondo = Label(ventana, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Aquí puedes agregar los elementos de la interfaz gráfica y la lógica de tu aplicación

# Ejecutar el bucle principal de la ventana
ventana.mainloop()