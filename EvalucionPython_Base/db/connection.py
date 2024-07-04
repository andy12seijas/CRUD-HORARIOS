import pyodbc

#Retorna la cadena de conexion
def obtener_cadena_de_conexion(SERVER, DATABASE):
    return f'DRIVER={{ODBC Driver 17 for SQL SERVER}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'

#Funcion que retorna la conexión
def conectar(SERVER, DATABASE):
    cadena = obtener_cadena_de_conexion(SERVER, DATABASE)

    try:
        conexion = pyodbc.connect(cadena)
        print("Conexión exitosa a la base de datos 😊👌")
        return conexion
    except pyodbc.Error as error:
        print(f'Error al conectar: {error}')
        return None

#Función para cerrar la conexión
def cerrar_conexion(conexion):
    if conexion:
        conexion.close()
        print('Conexión cerrada 😁😁😁😁😁😁😁😁😁')

