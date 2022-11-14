import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"Supermark.db"

    sql_create_usuarios_table = """ CREATE TABLE IF NOT EXISTS usuarios (
                                        usuarioId integer PRIMARY KEY AUTOINCREMENT,
                                        nombre text NOT NULL,
                                        apellido text NOT NULL,
                                        email text NOT NULL,
                                        dni integer NOT NULL,
                                        clave text NOT NULL
                                    ); """
    
    sql_create_domicilios_table = """ CREATE TABLE IF NOT EXISTS domicilios (
                                        domicilioId integer PRIMARY KEY AUTOINCREMENT,
                                        direccion text NOT NULL,
                                        numero integer,
                                        piso integer,
                                        dpto text,
                                        localidadId integer, 
                                        usuarioId integer, 
                                        FOREIGN KEY(localidadId) REFERENCES localidades(localidadId) 
                                        FOREIGN KEY(usuarioId) REFERENCES usuarios(usuarioId)                                    
                                    ); """

    sql_create_localidades_table = """ CREATE TABLE IF NOT EXISTS localidades (
                                        localidadId integer PRIMARY KEY AUTOINCREMENT,
                                        provincia text NOT NULL,
                                        departamento text NOT NULL,
                                        ciudad text,
                                        codpostal integer
                                    ); """

    sql_create_tarjetas_table = """ CREATE TABLE IF NOT EXISTS tarjetas (
                                        tarjetaId integer PRIMARY KEY AUTOINCREMENT,
                                        numero integer NOT NULL,
                                        banco text NOT NULL,
                                        titular text NOT NULL,
                                        fechaCaducidad text NOT NULL,
                                        usuarioId integer, 
                                        FOREIGN KEY(usuarioId) REFERENCES usuarios(usuarioId)
                                    ); """

    sql_create_productos_table = """ CREATE TABLE IF NOT EXISTS productos (
                                        productoId integer PRIMARY KEY AUTOINCREMENT,
                                        codigo text NOT NULL,
                                        nombre text NOT NULL,
                                        marca text NOT NULL,
                                        precio real NOT NULL,
                                        stock integer NOT NULL,
                                        tipoId integer, 
                                        FOREIGN KEY(tipoId) REFERENCES tipos(tipoId)
                                    ); """

    sql_create_tipos_table = """ CREATE TABLE IF NOT EXISTS tipos (
                                        tipoId integer PRIMARY KEY AUTOINCREMENT,
                                        descripcion text NOT NULL,
                                        descuentoId integer NOT NULL, 
                                        FOREIGN KEY(descuentoId) REFERENCES descuentos(descuentoId)
                                    ); """

    sql_create_descuentos_table = """ CREATE TABLE IF NOT EXISTS descuentos (
                                        descuentoId integer PRIMARY KEY AUTOINCREMENT,
                                        porcentaje real NOT NULL
                                    ); """

    sql_create_comprobantes_table = """ CREATE TABLE IF NOT EXISTS comprobantes (
                                        comprobanteId integer PRIMARY KEY AUTOINCREMENT,
                                        numero integer NOT NULL,
                                        tipo text NOT NULL,
                                        fecha text NOT NULL,
                                        total real NOT NULL,
                                        usuarioId integer, 
                                        tarjetaId integer,
                                        FOREIGN KEY(usuarioId) REFERENCES usuarios(usuarioId),
                                        FOREIGN KEY(tarjetaId) REFERENCES tarjetas(tarjetaId)
                                    ); """

    sql_create_detalles_table = """ CREATE TABLE IF NOT EXISTS detalles (
                                        detalleId integer PRIMARY KEY AUTOINCREMENT,
                                        cantidad integer NOT NULL,
                                        precio real NOT NULL,
                                        productoId integer, 
                                        comprobanteId integer, 
                                        FOREIGN KEY(productoId) REFERENCES productos(productoId),
                                        FOREIGN KEY(comprobanteId) REFERENCES comprobantes(comprobanteId)
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_usuarios_table)
        create_table(conn, sql_create_domicilios_table)
        create_table(conn, sql_create_localidades_table)
        create_table(conn, sql_create_tarjetas_table)
        create_table(conn, sql_create_productos_table)
        create_table(conn, sql_create_tipos_table)
        create_table(conn, sql_create_descuentos_table)
        create_table(conn, sql_create_comprobantes_table)
        create_table(conn, sql_create_detalles_table)

        # create tasks table
        # create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
