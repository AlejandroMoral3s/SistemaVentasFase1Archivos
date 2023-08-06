class Producto:

    def __init__(self, id, descripcion, precio, iva, nota):
        self.__id = id
        self.__descripcion = descripcion
        self.__precio = precio
        self.__iva = iva
        self.__nota = nota

    def __str__(self):
        return f'ID [ {self.__id} ] DESCRIPCION [ {self.__descripcion} ] PRECIO [ {self.__precio} ] IVA [ {self.__iva} ] NOTA [{self.__nota}]'
    

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def descripcion(self):
        return self.__descripcion
    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion   

    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, precio):
        self.__precio = precio   

    @property
    def iva(self):
        return self.__iva
    @iva.setter
    def iva(self, iva):
        self.__iva = iva

    @property
    def nota(self):
        return self.__nota
    @nota.setter
    def nota(self, nota):
        self.__nota = nota