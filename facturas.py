class Factura:

    def __init__(self, id, fecha, cliente, productos, total):
        self.__id = id
        self.__fecha = fecha
        self.__cliente = cliente
        self.__productos = productos
        self.__total = total

    def __str__(self):
        return f'ID [ {self.__id} ] fecha [ {self.__fecha} ] cliente [ {self.__cliente} ] productos [ {self.__productos} ] total [ {self.__total} ] '
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha   

    @property
    def cliente(self):
        return self.__cliente
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente   

    @property
    def productos(self):
        return self.__productos
    @productos.setter
    def productos(self, productos):
        self.__productos = productos
        
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total):
        self.__total = total
