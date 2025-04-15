from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:  # Se crea el objeto pool
            try:
                pool_config = {
                    'pool_name': cls.POOL_NAME,
                    'pool_size': cls.POOL_SIZE,
                    'host': cls.HOST,
                    'user': cls.USERNAME,
                    'password': cls.PASSWORD,
                    'port': cls.DB_PORT,
                    'database': cls.DATABASE
                }
                cls.pool = pooling.MySQLConnectionPool(**pool_config)
                return cls.pool
            except Error as e:
                print(f'Error al crear el pool de conexiones: {e}')
                return None
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().get_connection()
        return conexion

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()
