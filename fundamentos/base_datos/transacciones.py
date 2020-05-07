import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db')

try:
    # conexion.autocommit = True

    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) values(%s, %s, %s)'
    valores = ('María', 'Esparza', 'mesparza@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Juan1', 'Pérez2', 'jperez3@mail.com', 1)
    cursor.execute(sentencia, valores)

    # guardamos la informacion en la base de datos
    conexion.commit()
except Exception as e:
    # rollback da marcha atras a todas las operaciones pendientes
    conexion.rollback()
    print(f'Ocurrió in error en la transaccion: {e}')
finally:
    cursor.close()
    conexion.close()
