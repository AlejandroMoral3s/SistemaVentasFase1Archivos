from usuarios import*
import json
from json import*

class UsuariosList:    
    dataJson = {} 
    
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
        
    
    def buscarUser(self, username):    
        for usuario in self.dataJson['users']:
            if(usuario['_Usuario__nombreUsuario']==username):
                return usuario
        return None
    
    def agregarDict(self, dict):        
        self.dataJson['users'].append(dict)
        self.guardar()
        
    
    #crea un objeto usuario, lo agrega al array y por ultimo actualiza el json    
    def crearUsuario(self, id, perfil, nombre, apellido,username, clave, confirmacion):
        if(self.buscarUser(username)!=None): 
            print("Este usuario ya existe")
        else:
            usuario= Usuario(id, perfil, nombre, apellido,username, clave, confirmacion)
            usuarioDict = vars(usuario)
            self.agregarDict(usuarioDict)
    
    def editarUsuario(self, usernameAnt, perfil, nombre, apellido, usernameNuevo, clave, confirmacion):
        usTemp=self.buscarUser(usernameAnt)
        if(usTemp!=None):
            usTemp['_Usuario__perfil'] = perfil
            usTemp['_Usuario__nombre'] = nombre
            usTemp['_Usuario__apellido'] = apellido            
            usTemp['_Usuario__nombreUsuario'] = usernameNuevo
            usTemp['_Usuario__clave'] = clave
            usTemp['_Usuario__confirmacion'] = confirmacion
            self.guardar()
        else:
            print("Este usuario no existe")
    
    def borrarUsuario(self, username):
        usTemp = self.buscarUser(username)
        if(usTemp!=None):
            self.dataJson['users'].remove(usTemp)
            self.guardar()
        else:
            print("Este user no existe")        