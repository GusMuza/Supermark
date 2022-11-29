class Comprobante:
    def __init__(self,comprobanteId,tipo,fecha,total,usuarioId,tarjetaId):
        self.__comprobanteId=comprobanteId
        self.__tipo=tipo
        self.__fecha=fecha
        self.__total=total
        self.__usuarioId=usuarioId
        self.__tarjetaId=tarjetaId
        
    @property
    def comprobanteId(self):
        return self.__comprobanteId
    
    @comprobanteId.setter
    def comprobanteId(self,comprobanteId):
        self.__comprobanteId = comprobanteId
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self,tipo):
        self.__tipo = tipo
    
    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self,fecha):
        self.__fecha = fecha 
        
    @property
    def total(self):
        return self.__total
    
    @total.setter
    def total(self,total):
        self.__total = total 
        
    @property
    def usuarioId(self):
        return self.__usuarioId
    
    @usuarioId.setter
    def usuarioId(self,usuarioId):
        self.__usuarioId = usuarioId
        
    @property
    def tarjetaId(self):
        return self.__tarjetaId
    
    @tarjetaId.setter
    def tarjetaId(self,tarjetaId):
        self.__usuarioId = tarjetaId
