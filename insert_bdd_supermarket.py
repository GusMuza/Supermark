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
    sql = ''' INSERT INTO tarjetas(numero, banco, titular, fechaCaducidad, usuarioId)
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
        ['Conservas',5],
        ['Harinas',3],
        ['Pastas y Salsas',2],
        ['Snacks',1],
        ['Arroz y Legumbres',3],
        ['Bebidas',1],
        ['Lácteos',2]
    ]  
    
    descuentos = [
        [0.00],
        [5.00],
        [10.00],
        [15.00],
        [25.00],
        [30.00],
        [40.00],
        [45.00],
        [50.00]
    ]      

    usuarios = [
        ['BELEN', 'SORIA', 'abelu89@gmail.com','36087450', '2000-04-29',  '123456abcd#', 'ALBERDI 789','admin'],
        ['JULIAN', 'ALVAREZ', 'july_alvarez@gmail.com','11122233', '1998-01-01',  'juli_alvarez', 'Alberdi 791','admin'],
        ['JORGE RAUL', 'AGUILERA', 'jorgeraul@gmail.com','24504036', '1972-06-10',  'qwert123', '20 DE FEBRERO 941','cliente'],
        ['GRISELDA BEATRIZ', 'ALBORNOZ', 'gbeatriz@gmail.com','34041751', '1988-03-29',  'asdfg321', 'GUEMES 662','cliente'],
        ['HECTOR JOSE', 'ALTAMIRANO', 'josealtamirano@gmail.com','32934724', '1986-07-01',  'zxcvb135', 'BOLIVIA 134','cliente'],
        ['CRISTIAN EMANUEL', 'BRITO', 'emanuel_brito@gmail.com','35928858', '1990-12-10',  'uiop789', 'AV SAN MARTIN 209','cliente'],
        ['ENRIQUE', 'CARDOZO', 'ecardozo@gmail.com','29948427', '1980-01-20',  'hjkl987', 'B° EL PROGRESO MZA 3 CA 3','cliente'],
        ['LAURA', 'DIAZ', 'lau_diaz@gmail.com','32684283', '1986-08-14',  'vbnm3456', 'CORNEJO 1208-B°SAN ROQUE','cliente'],
        ['FERNANDA', 'GUZMAN', 'f_guzman@gmail.com','33567822', '1988-08-08',  'qqaazz345', 'ALBERDI 789','cliente'],
        ['YAMILA', 'LEDESMA', 'yamilaledesma@gmail.com','32013892', '1987-03-22',  'yamila123', '12 DE OCTUBRE 140','cliente'],
        ['SILVIA SUSANA', 'PADILLA', 'silpadilla@gmail.com','37961022', '2001-09-07',  'susana567', 'CORDOBA 173 B° CENTRO','cliente'],
        ['ANGEL', 'RESTON', 'angelreston@gmail.com','36677915', '2000-02-28',  'angelito11', 'RIVADAVIA 989','cliente']
    ]
    
    productos = [
        ['11621310003', 'Lentejas Arcor 300g', 'ARCOR', 153.30, 60, 1],
        ['11650101001', 'Picadillo De Carne Swift 90 Gr', 'SWIFT', 125.00, 20, 1],
        ['11620302017', 'Choclo Amarillo Arcor 300 Gr', 'ARCOR', 140.00, 18, 1],
        ['11410138007', 'Harina Ca¤uelas 0000 X1kg', 'CAnUELAS', 132.00, 35, 2],
        ['11410413001', 'Harina Ca¤uelas Integral X1kg', 'CAnUELAS', 138.00, 35, 2],
        ['11410142005', 'Harina Pureza Ultra Refinada 000 1 Kg', 'PUREZA', 112.00, 35, 2],
        ['11430501017', 'Almidon De Maiz Maizena Clasica Sin Tacc 520 G', 'MAIZENA', 348.00, 35, 2],
        ['11430301030', 'Avena Quaker Instantanea 380g', 'QUAKER', 430.00, 35, 2],
        ['11460701040', 'Fideos Rina Matarazzo Fusilli X 500 Gr', 'MATARAZZO', 287.00, 20, 3],
        ['11460214002', 'Tallarin La Campagnola Pastas Secas 500 Gr', 'LA CAMPAGNOLA', 171.00, 20, 3],
        ['11460104019', 'Fideos Spaghetti Lucchetti X500 Gr', 'LUCHETTI', 165.00, 20, 3],
        ['11460701032', 'Fideos Tirabuzon Matarazzo X500 Gr', 'MATARAZZO', 194.00, 20, 3],
        ['11460701031', 'Fideos Mostachol Matarazzo X500 Gr', 'MATARAZZO', 194.00, 20, 3],
        ['11610101006', 'Tomate Perita En Lata Arcor 400 Gr', 'ARCOR', 126.00, 20, 3],
        ['11610707009', 'Pure Tomate Arcor 1050g', 'ARCOR', 276.00, 20, 3],
        ['11131154039', 'Doritos Queso 220 Gr', 'DORITOS', 909.00, 18, 4],
        ['11130101200', 'Papas Fritas Lays Clasicas 379g', 'LAYS', 1042.00, 18, 4],
        ['11130101198', 'Papas Fritas Lays Clasicas 145g', 'LAYS', 525.00, 18, 4],
        ['11130709005', 'Palitos Salados Krachitos 120 Gr', 'KRACH-ITOS', 152.00, 18, 4],
        ['11130702017', 'Palitos Salados Pehuamar 190g', 'PEHUAMAR', 224.00, 18, 4],
        ['11131708006', 'Nachos Tostitos X220g', 'Tostitos', 848.00, 18, 4],
        ['11130118050', 'Papas Fritas Americano Krachitos 60g', 'KRACH-ITOS', 167.00, 18, 4],
        ['11131229003', 'Gallo 4 Chips Queso 100 Gr.', 'GALLO', 291.00, 18, 4],
        ['11130902035', 'Maní Japonés Pehuamar 110 Gr', 'PEHUAMAR', 324.00, 18, 4],
        ['11131202009', 'Saladix Cross Queso X67g', 'SALADIX', 141.00, 18, 4],
        ['11131229007', 'Galletitas Snack Gallo De Arroz Jamon X50g', 'GALLO', 163.00, 18, 4],
        ['11450507012', 'Arroz Molinos Ala Grano Largo Fino 1kg', 'Molinos Ala', 203.00, 100, 5],
        ['11450502015', 'Arroz Oro Estuche Gallo X1 Kg', 'GALLO', 282.00, 100, 5],
        ['11450507014', 'Arroz Molinos Ala Parboil 1kg', 'Molinos Ala', 233.00, 100, 5],
        ['11450302013', 'Arroz Doble Carolina Gallo X1 Kg', 'GALLO', 463.00, 100, 5],
        ['11480111001', 'Lentejas La Espanola Gourmet 400 Gr', 'LA ESPAnOLA GOURMET', 177.00, 100, 5],
        ['11470310014', 'Risotto 4 Quesos Gallo X240 Gr', 'GALLO', 454.00, 100, 5],
        ['11480908002', 'Garbanzos Egran X400g', 'EGRAN', 304.00, 100, 5],
        ['12120107001', 'Agua Mineral Eco De Los Andes Sin Gas 2 L', 'ECO DE LOS ANDES', 191.00, 44, 6],
        ['12120104025', 'Agua Villa Del Sur Pet Sin Gas 2250 Ml', 'Levite', 199.00, 44, 6],
        ['12120103003', 'Agua Villavicencio Pet Sin Gas 2 L', 'VILLAVICENCIO', 185.00, 44, 6],
        ['12110101009', 'Gaseosa Coca-cola Sabor Original 2.25 L', 'COCA COLA', 405.00, 44, 6],
        ['12110301030', 'Gaseosa Sprite Sin Azúcar Lima-limón 1.5 Lt', 'SPRITE', 268.82, 44, 6],
        ['12110901005', 'Gaseosa Fanta Naranja 500 Ml', 'FANTA', 171.59, 44, 6],
        ['12130501113', 'Ades Soja + Jugo De Manzana 1 L', 'ADES', 277.36, 44, 6],
        ['21130106046', 'Jugo Naranja Citric 1l', 'CITRIC', 460.00, 44, 6],
        ['12130106140', 'Jugo En Polvo Clight Manzana Verde D 7 5gr', 'CLIGHT', 57.00, 44, 6],
        ['12320303001', 'Aperitivo Gancia 950 Ml', 'GANCIA', 1114.00, 44, 6],
        ['12320501017', 'Fernet Branca Botella 750 Cc', 'BRANCA', 1700.00, 44, 6],
        ['12320710002', 'Aperitivo Livenza Spritz Soda 310ml Sin Tac', 'GANCIA', 256.00, 44, 6],
        ['12520514001', 'Gin Bombay 750 Ml', 'BOMBAY', 6260.00, 44, 6],
        ['12520540001', 'Gin Bombay Bramble 700', 'BOMBAY', 6909.00, 44, 6],
        ['12521364001', 'Vodka Smirnoff Bc Grapef.lime', 'SMIRNOFF', 1816.00, 44, 6],
        ['12440137035', 'Cerveza Patagonia Hoppy Lager 730 Cc No Retornable', 'PATAGONIA', 543.00, 44, 6],
        ['12440106063', 'Cerveza Rubia Quilmes Clásica 1 L Botella Retornable', 'QUILMES', 365.00, 44, 6],
        ['12440504032', 'Cerveza Heineken Retornable 1lt', 'HEINEKEN', 529.00, 44, 6],
        ['12440137003', 'Cerveza Roja Patagonia Amber Lager 730 Ml Botella Descartable', 'PATAGONIA', 543.00, 44, 6],
        ['12410901001', 'Espumante Baron B Extra Brut 750 Cc', 'BARON B', 4108.00, 44, 6],
        ['12410548002', 'Espumante Chandon Brut Nature Rose', 'CHANDON', 2476.00, 44, 6],
        ['12521501004', 'Whisky Jack Daniels 750 Ml.', 'JACK DANIELS', 11510.00, 44, 6],
        ['12521597002', 'Whisky Johnnie Walker Red Label 1 L', 'JOHNNIE WALKER', 7065.00, 44, 6],
        ['21210112009', 'Crema De Leche Doble Milkaut X 205 Gr', 'MILKAUT', 244.00, 60, 7],
        ['21210307009', 'Crema De Leche Culinaria La Serenisima U.a.t. 200 Ml', 'LA SERENISIMA', 198.00, 60, 7],
        ['21210112011', 'Crema Milkaut 325g', 'MILKAUT', 375, 60, 7],
        ['21280104012', 'Dulce De Leche Ls Colonial 400g', 'LA SERENISIMA', 299, 60, 7],
        ['21280138009', 'Dulce De Leche Familiar Milkaut X 405 Gr', 'MILKAUT', 249, 60, 7],
        ['21280138011', 'Dulce De Leche De Campo Milkaut 400g', 'MILKAUT', 327.00, 60, 7],
        ['21140105002', 'Silk Almendra Sin Azúcar 946 Cm3', 'Silk', 592.00, 60, 7],
        ['21140106001', 'Bebida A Base De Almendras Ades Almendras 1lt', 'ADES', 437.34, 60, 7],
        ['21110102029', 'Leche Entera Clasica La Serenisima Sachet 1 L', 'LA SERENISIMA', 221.00, 60, 7],
        ['21270104010', 'Manteca Multivitaminas La Serenísima 200gr', 'LA SERENISIMA', 533.00, 60, 7],
        ['21270102015', 'Manteca Sancor Multivitaminas 200 Gr', 'SANCOR', 379.00, 60, 7],
        ['21270119002', 'Manteca Milkaut Paquete X 100 Gr', 'MILKAUT', 262.00, 60, 7]
    ]

    tarjetas = [
        ['4508 1234 5678 9010','MACRO','JORGE RAUL AGUILERA','24-12-01',3],
        ['4000 1234 5678 9010','GALICIA','GRISELDA BEATRIZ ALBORNOZ','24-01-01',4],
        ['5226 8400 1925 7458','NACION','HECTOR JOSE ALTAMIRANO','25-05-01',5],
        ['4720 3900 0000 0000','HSBC','MARIA JULIA LOIS','22-01-01',6],
        ['4365 0100 8754 8974','MACRO','ENRIQUE CARDOZO','23-07-01',7],
    ] 
    
    comprobantes = [
        ['00001-00000001', 'B', '2022-11-04', 5487, 3, 1 ],
        ['00001-00000002', 'B', '2022-11-04', 8954, 4, 2 ],
        ['00001-00000003', 'B', '2022-11-04', 12548, 5, 3 ],
        ['00001-00000004', 'B', '2022-11-05', 87451, 6, 4 ],
        ['00001-00000005', 'B', '2022-11-05', 97854, 7, 5 ]
    ]  

    detalles = [
        [4, 153.30, 1, 1],
        [1, 125.00, 2, 1],
        [2, 140.00, 3, 1],
        [6, 132.00, 4, 1],
        [2, 304.00, 10, 1],
        [1, 460.00, 16, 2],
        [1, 1700.00, 17, 2],
        [1, 6909.00, 19, 2],
        [2, 153.30, 1, 3],
        [2, 125.00, 2, 3],
        [3, 140.00, 3, 4],
        [1, 132.00, 4, 4],
        [3, 304.00, 10, 5],
        [4, 460.00, 16, 5],
        [1, 1700.00, 17, 5],
        [1, 6909.00, 19, 5]
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
        
        #create a new tarjeta_credito
        for tarjeta in tarjetas:
            create_tarjetas(conn, tarjeta)
        
        # create a new comprobante
        for comprobante in comprobantes:
            create_comprobantes(conn, comprobante)
        
        # create a new detalle_compra
        for detalle in detalles:
            create_detalles_compra(conn, detalle)
        
        # create a new producto
        for producto in productos: 
            create_productos(conn, producto)
        
        print("Valores insertados")
        


if __name__ == '__main__':
    insert_data("Supermark.db")
    pass
