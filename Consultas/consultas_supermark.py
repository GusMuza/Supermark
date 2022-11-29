import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_all_descuentos(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM descuentos")

    rows = cur.fetchall()
    # print(rows)

    return rows


def select_descuento_porcentaje(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM descuento WHERE porcentaje = 25")

    rows = cur.fetchone()
    # print(rows)

    return rows


def update_descuento(conn, descuento):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE descuentos
              SET porcentaje = ?
              WHERE descuentoId = ?'''
    cur = conn.cursor()
    cur.execute(sql, descuento)
    conn.commit()
    print("Valor actualizado correctamente")


def main():
    database = r"Supermark.db"

    # create a database connection
    conn = create_connection(database)
    
    with conn:

        print("Mostrar descuentos")
        print(select_all_descuentos(conn))

        
if __name__ == '__main__':
    main()
