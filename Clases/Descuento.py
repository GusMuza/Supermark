class Descuento:
    def __init__(self,descuentoId,porcentaje):
        self.__descuentoId=descuentoId
        self.__porcentaje=porcentaje
               
    @property
    def descuentoId(self):
        return self.__descuentoId
    
    @descuentoId.setter
    def descuentoId(self,descuentoId):
        self.__descuentoId = descuentoId
    
    @property
    def porcentaje(self):
        return self.__porcentaje
    
    @porcentaje.setter
    def porcentaje(self,porcentaje):
        self.__porcentaje = porcentaje
    
    