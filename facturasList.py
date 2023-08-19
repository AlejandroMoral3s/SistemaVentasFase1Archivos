from facturas import*
from productosList import*
import json
from json import*

class FacturasList:  
    objProd = ProductosList()
    dataJson = {}
    productos = []   
    total = 0
    
    #carga la info contenida en el .json, si no hay info se omite
    def __init__(self):
        with open('info.json', 'r') as f:   
            try:
                dataJson = json.load(f)
                self.dataJson = dataJson
            except EOFError:
                pass
            finally:
                del f
    
    def guardar(self):        
        with open('info.json','w') as file:
            json.dump(self.dataJson,file,indent=4)
        
    
    def buscarFactura(self, id):    
        for Factura in self.dataJson['facturas']:
            if(Factura['_Factura__id']==id):
                return Factura
        return None
    
    def agregarDictFac(self, dict):        
        self.dataJson['facturas'].append(dict)
        self.guardar()
    
    def agregarProductos(self, nombre, cant):
        prod = self.objProd.buscarProducto(nombre)
        self.productos.append(prod)
        self.total += prod['_Producto__precio']*cant
    
#PENDIENTE------------------------------------------------------
#    def eliminarProducto(self, parametro):
#        prod = self.objProd.buscarProducto(parametro)
#        self.productos.remove(prod)
        
    def limpiarFactura(self):
        self.productos.clear()
        self.total=0
    
    #crea un objeto Factura, lo agrega al array y por ultimo actualiza el json    
    def crearFactura(self, id, fecha, cliente, productos, total):
        if(self.buscarFactura(id)!=None): 
            print("Este Factura ya existe")
        else:
            factura= Factura(id, fecha, cliente, productos, total)
            FacturaDict = vars(factura)
            self.agregarDictFac(FacturaDict)  
            self.productos.clear()    
            self.total = 0

facturaL = FacturasList()
facturaL.agregarProductos("tomate",9)
facturaL.agregarProductos("cebolla",4)
facturaL.limpiarFactura()
productos = facturaL.productos
total = facturaL.total
facturaL.crearFactura(21,"10/08/2023","pancho",productos,total)
