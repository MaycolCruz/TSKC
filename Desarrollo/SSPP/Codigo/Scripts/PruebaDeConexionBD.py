import pyodbc

try:
    server = 'MSI\SQLEXPRESS'
    bd = 'SSPP'
    usuario = 'sa'
    contrasena = '72792766'
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' + server + ' ;DATABASE=' + bd + ';UID=' + usuario + ';PWD=' + contrasena)
    print("conexion exitosa")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Recluso")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)