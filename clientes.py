class Cliente:

    def __init__(self, id, dpi, nombre, apellido, direccion, telefono, ciudad, fechaNac, fechaIng):
        self.__id = id
        self.__dpi = dpi
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__telefono = telefono
        self.__ciudad = ciudad
        self.__fechaNac = fechaNac
        self.__fechaIng = fechaIng

    def __str__(self):
        return f'ID [ {self.__id} ] DPI [ {self.__dpi} ] NOMBRE [ {self.__nombre} ] APELLIDO [ {self.__apellido} ] DIRECCION [ {self.__direccion} ] TELEFONO [ {self.__telefono} ] CIUDAD [ {self.__ciudad} ] FECHA_NAC [ {self.__fechaNac} ] FECHA_ING [ {self.__fechaIng} ]'
    

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def dpi(self):
        return self.__dpi
    @dpi.setter
    def dpi(self, dpi):
        self.__dpi = dpi

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
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono

    @property
    def ciudad(self):
        return self.__ciudad
    @ciudad.setter
    def ciudad(self, ciudad):
        self.__ciudad = ciudad

    @property
    def fechaNac(self):
        return self.__fechaNac
    @fechaNac.setter
    def fechaNac(self, fechaNac):
        self.__fechaNac = fechaNac

    @property
    def fechaIng(self):
        return self.__fechaIng
    @fechaIng.setter
    def fechaIng(self, fechaIng):
        self.__fechaIng = fechaIng