from clientes import*
import json
from json import*

class ClientesList:    
    dataJson = {}
    dataJson['clients'] = []   
    
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
        
    
    def buscarCliente(self, dpi):    
        for cliente in self.dataJson['clients']:
            if(cliente['_Cliente__dpi']==dpi):
                return cliente
        return None
    
    def agregarDict(self, dict):        
        self.dataJson['clients'].append(dict)
        self.guardar()
        
    
    #crea un objeto Cliente, lo agrega al array y por ultimo actualiza el json    
    def crearCliente(self, id, dpi, nombre, apellido, direccion, telefono, ciudad, fechaNac, fechaIng):
        if(self.buscarCliente(dpi)!=None): 
            print("Este cliente ya existe")
        else:
            cliente= Cliente(id, dpi, nombre, apellido, direccion, telefono, ciudad, fechaNac, fechaIng)
            clienteDict = vars(cliente)
            self.agregarDict(clienteDict)
    
    def editarCliente(self, dpi, nombre, apellido, direccion, telefono, ciudad, fechaNac, fechaIng):
        cliTemp=self.buscarCliente(dpi)
        if(cliTemp!=None):
            cliTemp['_Cliente__nombre'] = nombre
            cliTemp['_Cliente__apellido'] = apellido
            cliTemp['_Cliente__direccion'] = direccion
            cliTemp['_Cliente__telefono'] = telefono
            cliTemp['_Cliente__ciudad'] = ciudad
            cliTemp['_Cliente__fechaNac'] = fechaNac
            cliTemp['_Cliente__fechaIng'] = fechaIng
            self.guardar()
        else:
            print("Este cliente no existe")
    
    def borrarCliente(self, dpi):
        cliTemp = self.buscarCliente(dpi)
        if(cliTemp!=None):
            self.dataJson['clients'].remove(cliTemp)
            self.guardar()
        else:
            print("Este cliente no existe")        


clienteL=ClientesList()
clienteL.crearCliente(12,"8965","Juan","Lopez","zona 2","4587966","xela","24/04/2003","12/08/2023")
#clienteL.borrarCliente(8965)
