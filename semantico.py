
palabras = ['Proceso','Escribir','Leer','Definir','Como', 'Caracter', 'Entero','Real','Logico','FinProceso']

estructura = []


def traductor(lista):

    lista = lista.split()
    print(lista)

    if palabras[0] in lista:
        posicion = lista.index(palabras[0])
        lista.pop(posicion)
        lista.insert(posicion,'def')

    if palabras[1] in lista:
        posicion = lista.index(palabras[1])
        lista.pop(posicion)
        lista.insert(posicion,'print')
    
    if palabras[2] in lista:
        posicion = lista.index(palabras[2])
        lista.pop(posicion)
        lista.insert(posicion+1,'= input()')
    
    if palabras[3] in lista:
        posicion = lista.index(palabras[3])
        lista.pop(posicion)

        if palabras[4] in lista:
            posicion = lista.index(palabras[4])
            lista.pop(posicion)
            lista.insert(posicion,'= null')

            if palabras[5] in lista:
                posicion = lista.index(palabras[5])
                lista.pop(posicion)
            elif palabras[6] in lista:
                posicion = lista.index(palabras[6])
                lista.pop(posicion)
            elif palabras[7] in lista:
                posicion = lista.index(posicion)
                lista.pop(posicion)
            elif palabras[8] in lista:
                posicion = lista.index(palabras[8])
                lista.pop(posicion)
    
    if palabras[9] in lista:
        posicion = lista.index(palabras[9])
        lista.pop(posicion)
    
    return lista

def traductor2(lista):
    lista = lista.split()

    if palabras[0] in lista:
        posicion = lista.index(palabras[0])
        lista.pop(posicion)
        lista.insert(posicion,'public class')
        lista.insert(posicion+2,'{')
        lista.insert(posicion+3,'public static void main(String[] args) {')
        lista.insert(posicion+4,'Scanner leer = new Scanner (System.in);')

    if palabras[1] in lista:
        posicion = lista.index(palabras[1])
        lista.pop(posicion)
        lista.insert(posicion,'System.out.println(')
        lista.insert(posicion+4,');')
    
    if palabras[2] in lista:
        posicion = lista.index(palabras[2])
        lista.pop(posicion)
        if palabras[5] in lista:
            lista.insert(posicion+1,'= leer.nextLine();')
        elif palabras[6] in lista:
            lista.insert(posicion+1,'= leer.nextInt();')
            
    
    if palabras[3] in lista:
        posicion1 = lista.index(palabras[3])
        lista.pop(posicion1)

        if palabras[4] in lista:
            posicion = lista.index(palabras[4])
            lista.pop(posicion)
            lista.insert(posicion,'= null;')

            if palabras[5] in lista:
                posicion = lista.index(palabras[5])
                lista.pop(posicion)
                lista.insert(posicion1, 'String')
            elif palabras[6] in lista:
                posicion = lista.index(palabras[6])
                lista.pop(posicion)
                lista.insert(posicion1, 'int')
            elif palabras[7] in lista:
                posicion = lista.index(posicion)
                lista.pop(posicion)
                lista.insert(posicion1, 'float')
            elif palabras[8] in lista:
                posicion = lista.index(palabras[8])
                lista.pop(posicion)
                lista.insert(posicion1, 'boolean')
    
    if palabras[9] in lista:
        posicion = lista.index(palabras[9])
        lista.pop(posicion)
        lista.insert(posicion,'}  }')
                
    return lista
