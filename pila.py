
class Pila:
    def __init__(self):
        self.pila = []
    
    def AgregarPila(self):
        self.pila.append()

    def eliminarPila(self):
        if len(self.pila) == 0:
            return None
        else:
            return self.pila.pop()
    
    def cabeceraPila(self):
        if len(self.pila) == 0:
            print('Borrado')
            return None
        else:
            return self.pila[-1]
    
    
    def mostrarPila(self):
        print("Pila: ", self.pila)
        return self.pila

    def proceso(self):
        self.MostrarPila()
        self.Agregar()
        self.MostrarPila()
        return self.eliminarPila()