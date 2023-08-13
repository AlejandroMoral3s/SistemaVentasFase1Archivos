from clientes import*
import json
from json import*

#retorna objeto Cliente serializado 
class ClientEncoder(json.JSONEncoder):
    def default(self,cli):
        return {"id":cli.id,"dpi": cli.dpi,"nombre": cli.nombre,"apellido": cli.apellido,"direccion": cli.direccion, "telefono":cli.telefono,"ciudad": cli.ciudad,"fechaNac": cli.fechaNac,"fechaIng": cli.fechaIng }

class ClientesList:    
    data = {}
    data['clients'] = []   
    
    #carga la info contenida en el .json, si no hay info se omite
    def __init__(self):
        with open('clients.json', 'r') as file:                    
            try:
                self.data = json.load(file)
            except EOFError:
                pass
    
    #crea un objeto Cliente, lo agrega al array y por ultimo actualiza el json    
    def crearCliente(self, id, dpi, nombre, apellido, direccion, telefono, ciudad, fechaNac, fechaIng):    
        cliente= Cliente(id, dpi, nombre, apellido, direccion, telefono, ciudad, fechaNac, fechaIng)
        self.data['clients'].append(cliente)
        with open('clients.json','w') as file:
            json.dump(self.data,file,cls=ClientEncoder,indent=4)

clienteL=ClientesList()
clienteL.crearCliente(1,1478965,"maria","pineda","zona 2","4587966","xela","24/04/2003","12/08/2023")
