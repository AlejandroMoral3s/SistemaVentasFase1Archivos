import pickle

def almacenarInformacion(nombreArchivo, listaObjetos):
    with open(nombreArchivo, 'wb+') as f:
        pickle.dump(listaObjetos, f)
        return

def recuperarInformacion(nombreArchivo):
    with open(nombreArchivo, 'rb+') as f:
        listaAlmacen = pickle.load(f)
        for x in listaAlmacen:
            print(x)