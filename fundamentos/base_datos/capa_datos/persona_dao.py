from fundamentos.base_datos.capa_datos.persona import Persona
from fundamentos.base_datos.capa_datos.conexion import Conexion
from fundamentos.base_datos.capa_datos.logger_base import logger


class PersonaDao:
    """DAO (Data Access Object) CRUD: Create-Read-Update-Delete entidad Persona"""
    __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
    __ACTUALIZAR = 'update PERSONA SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    __ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def seleccionar(cls):
        cursor = Conexion.obtenerCursor()
        logger.debug(cursor.mogrify(cls.__SELECCIONAR))
        cursor.execute(cls.__SELECCIONAR)
        registros = cursor.fetchall()
        personas = []
        for registro in registros:
            persona = Persona(registro[0], registro[1], registro[2], registro[3])
            personas.append(persona)
        Conexion.cerrar()
        return personas

    @classmethod
    def insertar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {persona}')
            values = (persona.get_nombre(), persona.get_apellido(), persona.get_email())
            cursor.execute(cls.__INSERTAR, values)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepción al insertar persona: {e}')
        finally:
            Conexion.cerrar()

    @classmethod
    def actualizar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {persona}')
            values = (persona.get_nombre(), persona.get_apellido(), persona.get_email(), persona.get_id_persona())
            cursor.execute(cls.__ACTUALIZAR, values)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepción al actualizar persona: {e}')
        finally:
            Conexion.cerrar()

    @classmethod
    def eliminar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            values = (persona.get_id_persona())
            cursor.execute(cls.__ELIMINAR, values)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepción al eliminar persona: {e}')
        finally:
            Conexion.cerrar()


if __name__ == '__main__':
    # personas = PersonaDao.seleccionar()
    # for persona in personas:
    #     logger.debug(persona)

    # Insertamos un nuevo registro
    # persona = Persona(nombre='Pedro', apellido='Najera', email='pnajera@email.com')
    # personas_insertadas = PersonaDao.insertar(persona)
    # logger.debug(f'Personas insertadas: {personas_insertadas}')

    # Actualizar un registro existente
    # persona = Persona(1, 'Juan', 'Pérez2', 'jperez3@mail.com')
    # persona_actualizada = PersonaDao.actualizar(persona)
    # logger.debug(f'Personas actualizadas: {persona_actualizada}')

    # Eliminar un registro existente
    persona = Persona('9')
    personas_eliminadas = PersonaDao.eliminar(persona)
    logger.debug(f'Personas elimiadas: {personas_eliminadas}')