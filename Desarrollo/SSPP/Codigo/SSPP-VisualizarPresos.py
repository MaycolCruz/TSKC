from tkinter import *
from tkinter import ttk
import pyodbc
from ConfigurarConexionBD import DB_DRIVER, DB_SERVER, DB_DATABASE, DB_USERNAME, DB_PASSWORD

# Crear la ventana principal
ventana = Tk()
ventana.title("REPORTE DE PRESOS")
ventana.geometry("1450x720")

# Crear el título del reporte
titulo = Label(ventana, text="REPORTE DE PRESOS", font=("Arial", 16, "bold"))
titulo.pack(pady=(20, 10))

# Crear tabla para mostrar los datos de los presos
tabla_presos = ttk.Treeview(ventana, columns=("Código", "Nombre", "Apellido", "Fecha de Nacimiento", "Crimen",
                                              "Curso", "Conducta", "Celda", "Peligrosidad", "Comentarios"),
                            show="headings")
tabla_presos.heading("Código", text="Código de Recluso", anchor="center")
tabla_presos.heading("Nombre", text="Nombre del Recluso", anchor="center")
tabla_presos.heading("Apellido", text="Apellido del Recluso", anchor="center")
tabla_presos.heading("Fecha de Nacimiento", text="Fecha de Nacimiento", anchor="center")
tabla_presos.heading("Crimen", text="Crimen", anchor="center")
tabla_presos.heading("Curso", text="Curso", anchor="center")
tabla_presos.heading("Conducta", text="Conducta", anchor="center")
tabla_presos.heading("Celda", text="Celda", anchor="center")
tabla_presos.heading("Peligrosidad", text="Peligrosidad", anchor="center")
tabla_presos.heading("Comentarios", text="Comentarios", anchor="center")
tabla_presos.pack(fill="both", padx=10, pady=(0, 10))

# Ajustar el ancho de las columnas en función del contenido
tabla_presos.column("Código", width=90)
tabla_presos.column("Nombre", width=120)
tabla_presos.column("Apellido", width=120)
tabla_presos.column("Fecha de Nacimiento", width=130)
tabla_presos.column("Crimen", width=70)
tabla_presos.column("Curso", width=80)
tabla_presos.column("Conducta", width=80)
tabla_presos.column("Celda", width=20)
tabla_presos.column("Peligrosidad", width=60)
tabla_presos.column("Comentarios", width=200)

# Obtener datos de la base de datos y mostrarlos en la tabla
conn = pyodbc.connect(
    f"Driver={DB_DRIVER};"
    f"Server={DB_SERVER};"
    f"Database={DB_DATABASE};"
    f"UID={DB_USERNAME};"
    f"PWD={DB_PASSWORD};"
)
cursor = conn.cursor()
cursor.execute("""
    SELECT R.Cod_recluso, R.Nombre, R.Apellido, R.Fecha_nacimiento, C.Nombre AS Crimen, CO.Nombre AS Curso,
           COU.Nombre AS Conducta, CE.Numero AS Celda, R.Peligrosidad, R.Comentario
    FROM Recluso R
    LEFT JOIN Crimen C ON R.Cod_crimen = C.Cod_crimen
    LEFT JOIN Curso CO ON R.Cod_curso = CO.Cod_curso
    LEFT JOIN Conducta COU ON R.Cod_conducta = COU.Cod_conducta
    LEFT JOIN Celda CE ON R.Cod_celda = CE.Cod_celda
""")
resultados = cursor.fetchall()
conn.close()

for resultado in resultados:
    codigo = int(resultado[0])
    nombre = resultado[1]
    apellido = resultado[2]
    fecha_nacimiento = str(resultado[3])
    crimen = resultado[4]
    curso = resultado[5]
    conducta = resultado[6]
    celda = resultado[7]
    peligrosidad = resultado[8]
    comentarios = resultado[9]
    
    tabla_presos.insert("", "end", values=(codigo, nombre, apellido, fecha_nacimiento, crimen,
                                           curso, conducta, celda, peligrosidad, comentarios))

# Configurar el anclaje central para todas las columnas
for column in tabla_presos["columns"]:
    tabla_presos.column(column, anchor="center")

# Añadir márgenes alrededor de la tabla
tabla_presos.pack(fill="both", padx=10, pady=(0, 10))

# Ejecutar el bucle principal de la ventana
ventana.mainloop()




