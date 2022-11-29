class Tarjeta:
    def __init__(self,tipoId,descripcion,descuentoId):
        self.__tipoId=tipoId
        self.__descripcion=descripcion
        self.__descuentoId=descuentoId
       
    @property
    def tipoId(self):
        return self.__tipoId
    
    @tipoId.setter
    def tipoId(self,tipoId):
        self.__tipoId = tipoId
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self,descripcion):
        self.__descripcion = descripcion
    
    @property
    def descuentoId(self):
        return self.__descuentoId
    
    @descuentoId.setter
    def descuentoId(self,descuentoId):
        self.__descuentoId = descuentoId