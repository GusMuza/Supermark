class Usuario:
    def __init__(self,usuarioId,nombre,apellido,email,dni,fechaNac,clave,direccion,tipo):
        self.__usuarioId=usuarioId
        self.__nombre=nombre
        self.__apellido=apellido
        self.__email=email
        self.__dni=dni
        self.__fechaNac=fechaNac
        self.__clave=clave
        self.__direccion=direccion
        self.__tipo=tipo
        
    @property
    def usuarioId(self):
        return self.__usuarioId
    
    @usuarioId.setter
    def usuarioId(self,usuarioId):
        self.__usuarioId = usuarioId
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,email):
        self.__email = email 
        
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self,dni):
        self.__dni = dni 
        
    @property
    def fechaNac(self):
        return self.__fechaNac
    
    @fechaNac.setter
    def fechaNac(self,fechaNac):
        self.__fechaNac = fechaNac
        
    @property
    def clave(self):
        return self.__clave
    
    @clave.setter
    def clave(self,clave):
        self.__clave = clave
        
    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self,direccion):
        self.__direccion = direccion
        
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self,tipo):
        self.__tipo = tipo              
        
              