class Usuario:

    def __init__(self, id, perfil, nombre, apellido,username, clave, confirmacion):
        
        self.__id = id
        self.__perfil = perfil
        self.__nombre = nombre
        self.__apellido = apellido
        self.__username = username
        self.__clave = clave
        self.__confirmacion = confirmacion

    def __str__(self):
        return f'ID [ {self.__id} ] PERFIL [ {self.__perfil} ] NOMBRE [ {self.__nombre} ] APELLIDO [ {self.__apellido} ] CLAVE [ {self.__clave} ] CONFIRMACION [ {self.__confirmacion} ]'

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def perfil(self):
        return self.__perfil
    @perfil.setter
    def perfil(self, perfil):
        self.__perfil = perfil

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def clave(self):
        return self.__clave
    @clave.setter
    def clave(self, clave):
        self.__clave = clave

    @property
    def confirmacion(self):
        return self.__confirmacion
    @confirmacion.setter
    def confirmacion(self, confirmacion):
        self.__confirmacion = confirmacion
