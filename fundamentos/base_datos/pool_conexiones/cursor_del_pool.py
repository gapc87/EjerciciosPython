from fundamentos.base_datos.pool_conexiones.conexion import Conexion
from fundamentos.base_datos.pool_conexiones.logger_base import logger


class CursorDelPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None

    # Inicio de with
    def __enter__(self):
        logger.debug('Inicio de with método __enter__')
        self.__conn = Conexion.obtenerConexion()
        self.__cursor = self.__conn.cursor()
        return self.__cursor

    # fin del bloque with
    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.debug(f'Se ejecuta método __exit__')
        if exc_val:
            self.__conn.rollback()
            logger.debug(f'Ocurrió una excepción: {exc_val}')
        else:
            self.__conn.commit()
            logger.debug('Commit de la transacción')
        # Cerramos el cursor
        self.__cursor.close()
        # Regresar la conexion al pool
        Conexion.liberarConexion(self.__conn)


if __name__ == '__main__':
    # Obtener un cursor a partir de la conexion del pool
    # with se ejecuta __enter_ y termina con __exit__
    with CursorDelPool() as cursor:
        cursor.execute('SELECT * FROM persona')
        logger.debug('Listado de Personas')
        logger.debug(cursor.fetchall())
