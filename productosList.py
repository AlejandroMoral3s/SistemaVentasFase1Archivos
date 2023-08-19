from productos import*
import json
from json import*

class ProductosList:    
    dataJson = {}
    dataJson['products'] = []   
    
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
        
    
    def buscarProducto(self, parametro):    
        for Producto in self.dataJson['products']:
            if(Producto['_Producto__id']==parametro):
                return Producto
            elif(Producto['_Producto__descripcion']==parametro):
                return Producto
        return None
    
    def agregarDict(self, dict):        
        self.dataJson['products'].append(dict)
        self.guardar()
        
    
    #crea un objeto Producto, lo agrega al array y por ultimo actualiza el json    
    def crearProducto(self, id, descripcion, precio, iva, nota):
        if(self.buscarProducto(id)!=None): 
            print("Este producto ya existe")
        else:
            producto= Producto(id, descripcion, precio, iva, nota)
            ProductoDict = vars(producto)
            self.agregarDict(ProductoDict)
    
    def editarProducto(self, id, descripcion, precio, iva, nota):
        prodTemp=self.buscarProducto(id)
        if(prodTemp!=None):
            prodTemp['_Producto__descripcion'] = descripcion
            prodTemp['_Producto__precio'] = precio
            prodTemp['_Producto__iva'] = iva
            prodTemp['_Producto__nota'] = nota
            self.guardar()
        else:
            print("Este Producto no existe")
    
    def borrarProducto(self, id):
        prodTemp = self.buscarProducto(id)
        if(prodTemp!=None):
            self.dataJson['products'].remove(prodTemp)
            self.guardar()
        else:
            print("Este producto no existe")        

