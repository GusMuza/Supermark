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

def create_descuentos(conn, descuento):
    """
    Create a new project into the projects table
    :param conn: object of type sqlite3.Connection
    :param descuento:list of values
    :return: descuento id
    """
    sql = ''' INSERT INTO descuentos(porcentaje)
            VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, descuento)
    conn.commit()
    return cur.lastrowid


def create_tipos(conn, tipo):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param tipo: list of values
    :return:
    """
    sql = ''' INSERT INTO tipos(descripcion,descuentoId)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, tipo)
    conn.commit()
    return cur.lastrowid

def create_productos(conn, producto):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param producto: list of values
    :return:
    """
    sql = ''' INSERT INTO productos(codigo, nombre, marca, precio, stock, tipoId)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, producto)
    conn.commit()
    return cur.lastrowid

def create_usuarios(conn, usuario):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param usuario: list of values
    :return:
    """
    sql = ''' INSERT INTO usuarios(nombre, apellido, email, dni, fechaNac, clave, direccion, tipo)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, usuario)
    conn.commit()
    return cur.lastrowid

def create_tarjetas(conn, tarjeta_credito):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param tarjeta_credito: list of values
    :return:
    """
    sql = ''' INSERT INTO tarjetas(numero, banco, titular, fechaCaducidad, id_usuario)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, tarjeta_credito)
    conn.commit()
    return cur.lastrowid

def create_comprobantes(conn, comprobante):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param comprobante: list of values
    :return:
    """
    sql = ''' INSERT INTO comprobantes(numero, tipo, fecha, total, usuarioId, tarjetaId)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, comprobante)
    conn.commit()
    return cur.lastrowid

def create_detalles_compra(conn, detalle_compra):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param detalle_comprobante: list of values
    :return:
    """
    sql = ''' INSERT INTO detalles(cantidad, precio, productoId, comprobanteId)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, detalle_compra)
    conn.commit()
    return cur.lastrowid


def insert_data(database):

    tipos = [
        ['Conservas',1],
        ['Harinas',1],
        ['Pastas y Salsas',1],
        ['Snacks',1],
        ['Arroz y Legumbres',1],
        ['Bebidas',1],
        ['Lácteos',1]
    ]  
    
    descuentos = [
        [10],
        [15],
        [16],
        [24]
    ]      

    usuarios = [
        ['Jose', 'Perez', 'jose_perez@gmail.com',
         '12345678', '2000-01-01',  '123456abcd#', 'Alberdi 789','admin'],
        ['Julian', 'Alvarez', 'july_alvarez@gmail.com',
                   '11122233', '1998-01-01',  'juli_alvarez', 'Alberdi 791','cliente'],
    ]
    
    productos = [
        ['11621310003', 'Lentejas Arcor 300g', 'ARCOR', 153.30, 60, 1],
        ['11650101001', 'Picadillo De Carne Swift 90 Gr', 'SWIFT', 125.00, 20, 1],
        ['11620302017', 'Choclo Amarillo Arcor 300 Gr', 'ARCOR', 140.00, 18, 1],
        ['11410138007', 'Harina Ca¤uelas 0000 X1kg', 'CANUELAS', 132.00, 35, 2],
        ['11410413001', 'Harina Ca¤uelas Integral X1kg', 'CANUELAS', 138.00, 35, 2],
        ['11410142005', 'Harina Pureza Ultra Refinada 000 1 Kg', 'PUREZA', 112.00, 35, 2]

    ]




    # create a database connection
    conn = create_connection(database)
    with conn:
        
        # create a new descuento
        for descuento in descuentos:
            create_descuentos(conn, descuento)
          
        #create a new tipo
        for tipo in tipos:
            create_tipos(conn, tipo)
               
        #create a new usuario
        for usuario in usuarios:
            create_usuarios(conn, usuario)
        
        '''
        # create a new tarjeta_credito
        for tarjeta in tarjetas:
            create_tarjetas(conn, tarjeta_credito)
        
        # create a new comprobante
        for comprobante in comprobantes:
            create_comprobantes(conn, comprobante)
        
        # create a new detalle_compra
        for detalle in detalles:
            create_detalles_compra(conn, detalle_compra)
        '''
        
        # create a new producto
        for producto in productos: 
            create_productos(conn, producto)
        
        print("Valores insertados")
        


if __name__ == '__main__':
    insert_data("Supermark.db")
    pass
