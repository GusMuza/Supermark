import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn


def update_usuarios_clave(conn, usuario):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE usuarios
              SET clave = ?
              WHERE usuarioId = ?'''
    cur = conn.cursor()
    cur.execute(sql, usuario)
    conn.commit()
    
def update_usuarios_atributo(conn, atributo ,usuario):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param descuento:
    :return: project id
    """
    sql = f''' UPDATE usuarios 
                SET {atributo} = ?
                WHERE usuarioId = ?'''
    cur = conn.cursor()
    cur.execute(sql, usuario)
    conn.commit()    

def update_table(conn, tabla,atributo,id,tupla):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param descuento:
    :return: project id
    """
    sql = f''' UPDATE {tabla} 
                SET {atributo} = ?
                WHERE {id} = ?'''
    cur = conn.cursor()
    cur.execute(sql, tupla)
    conn.commit() 

def main():
    database = r"Supermark.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        #update_usuarios_clave(conn, ("felipito",1))
        #update_usuarios_atributo(conn,"clave",("superFelipe",1))
        #update_table(conn,"usuarios","clave","usuarioId",("superFelipon",1))
        #update_table(conn,"usuarios","dni","usuarioId",(34331999,1))
        update_table(conn,"productos","stock","productoId",(300,2))

if __name__ == '__main__':
    main()
