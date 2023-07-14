# Capa de acceso a datos (data_access_layer/user_repository.py)
import pyodbc

# Establecer la cadena de conexión
server = 'TU_SERVIDOR'
database = 'TU_BASE_DE_DATOS'
username = 'TU_USUARIO'
password = 'TU_CONTRASEÑA'
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

# Establecer la conexión
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()


class UserRepository:
    def __init__(self):
        # Configurar la conexión a la base de datos
        self.connection_string = ...

    def insert_user(self, user_data):
        # Abrir la conexión a la base de datos
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()

        # Ejecutar el comando SQL para insertar el usuario
        insert_query = "INSERT INTO users (name, email) VALUES (?, ?)"
        values = (user_data['name'], user_data['email'])
        cursor.execute(insert_query, values)
        conn.commit()

        # Cerrar la conexión
        cursor.close()
        conn.close()
