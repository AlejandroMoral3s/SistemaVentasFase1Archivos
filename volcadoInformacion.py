import pickle

def almacenarInformacion(nombreArchivo, listaObjetos):
    with open(nombreArchivo, 'w') as f:
        pickle.dump(listaObjetos, f)
        return

def recuperarInformacion(nombreArchivo):
    with open(nombreArchivo, 'r') as f:
        listaAlmacen = pickle.load(f)
        for x in listaAlmacen:
            print(x)