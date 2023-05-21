import sqlite3

# Conectarse a la base de datos (se creará si no existe)
conn = sqlite3.connect('SSPP-BD.db')

# Crear un objeto cursor
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT,
                   apellido TEXT,
                   edad INTEGER)''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()