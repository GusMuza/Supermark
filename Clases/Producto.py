class Producto:
    def __init__(self,productoId,codigo,nombre,precio,stock,tipoId,marca):
        self.__productoId=productoId
        self.__codigo=codigo
        self.__nombre=nombre
        self.__precio=precio
        self.__stock=stock
        self.__tipoId=tipoId
        self.__marca=marca
        
        
    @property
    def productoId(self):
        return self.__productoId
    
    @productoId.setter
    def productoId(self,productoId):
        self.__productoId = productoId
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self,precio):
        self.__precio = precio
        
    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self,stock):
        self.__stock = stock    
        
    @property
    def tipoId(self):
        return self.__tipoId
    
    @tipoId.setter
    def tipoId(self,tipoId):
        self.__tipoId = tipoId    
        
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,marca):
        self.__marca = marca 