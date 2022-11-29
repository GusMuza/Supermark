class Tarjeta:
    def __init__(self,tarjetaId,numero,banco,titular,fechaCaducidad,usuarioId):
        self.__tarjetaId=tarjetaId
        self.__numero=numero
        self.__banco=banco
        self.__titular=titular
        self.__fechaCaducidad=fechaCaducidad
        self.__usuarioId=usuarioId
       
    @property
    def tarjetaId(self):
        return self.__tarjetaId
    
    @tarjetaId.setter
    def tarjetaId(self,tarjetaId):
        self.__tarjetaId = tarjetaId
    
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self,numero):
        self.__numero = numero
    
    @property
    def banco(self):
        return self.__banco
    
    @banco.setter
    def banco(self,banco):
        self.__banco = banco
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self,titular):
        self.__titular = titular 
        
    @property
    def fechaCaducidad(self):
        return self.__fechaCaducidad
    
    @fechaCaducidad.setter
    def fechaCaducidad(self,fechaCaducidad):
        self.__fechaCaducidad = fechaCaducidad 
        
    @property
    def usuarioId(self):
        return self.__usuarioId
    
    @usuarioId.setter
    def usuarioId(self,usuarioId):
        self.__usuarioId = usuarioId
        