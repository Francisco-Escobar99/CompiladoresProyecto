import re

palabras_Reservadas = ['Proceso','Definir','Como', 'Caracter', 'Entero','Real','Logico','Verdadero','Falso',
                        'Escribir','Leer','FinProceso']
delimitadores = ['"',',','<','-','.','*','+']
parentesis = ["(",")"]
palabras = '^[A-Z|a-z]+$'
enteros = '^[0-9]+$'

def busqueda_Reservadas(texto):
    texto = texto.split()
    newReservadas = []

    if palabras_Reservadas[0] in texto:
        contador = texto.count(palabras_Reservadas[0])
        posicion = texto.index(palabras_Reservadas[0])
        print('-Proceso: ', contador, 'Posicion: ', posicion)
        newReservadas.append(palabras_Reservadas[0])
        texto.pop(posicion)
    else:
        contador = 0
    
    if palabras_Reservadas[1] in texto:
        contador2 = texto.count(palabras_Reservadas[1])
        posicion2 = texto.index(palabras_Reservadas[1])
        print('-Definir: ', contador2)
        newReservadas.append(palabras_Reservadas[1])
        texto.pop(posicion2)
    else:
        contador2 = 0
    
    if palabras_Reservadas[2] in texto:
        contador3 = texto.count(palabras_Reservadas[2])
        posicion3 = texto.index(palabras_Reservadas[2])
        print('-Como: ', contador3)
        newReservadas.append(palabras_Reservadas[2])
        texto.pop(posicion3)
    else:
        contador3 = 0
    
    if palabras_Reservadas[3] in texto:
        contador4 = texto.count(palabras_Reservadas[3])
        posicion4 = texto.index(palabras_Reservadas[3])
        print('-Caracter: ', contador4)
        newReservadas.append(palabras_Reservadas[3])
        texto.pop(posicion4)
    else:
        contador4 = 0
    
    if palabras_Reservadas[4] in texto:
        contador5 = texto.count(palabras_Reservadas[4])
        posicion5 = texto.index(palabras_Reservadas[4])
        print('-Entero: ', contador5)
        newReservadas.append(palabras_Reservadas[4])
        texto.pop(posicion5)
    else:
        contador5 = 0
    
    if palabras_Reservadas[5] in texto:
        contador6 = texto.count(palabras_Reservadas[5])
        posicion6 = texto.index(palabras_Reservadas[5])
        print('-Real: ', contador6)
        newReservadas.append(palabras_Reservadas[5])
        texto.pop(posicion6)
    else:
        contador6 = 0
    
    if palabras_Reservadas[6] in texto:
        contador7 = texto.count(palabras_Reservadas[6])
        posicion7 = texto.index(palabras_Reservadas[6])
        print('-Logico: ', contador7)
        newReservadas.append(palabras_Reservadas[6])
        texto.pop(posicion7)
    else:
        contador7 = 0
    
    if palabras_Reservadas[7] in texto:
        contador8 = texto.count(palabras_Reservadas[7])
        posicion8 = texto.index(palabras_Reservadas[7])
        print('-Verdadero: ', contador8)
        newReservadas.append(palabras_Reservadas[7])
        texto.pop(posicion8)
    else:
        contador8 = 0
    
    if palabras_Reservadas[8] in texto:
        contador9 = texto.count(palabras_Reservadas[8])
        posicion9 = texto.index(palabras_Reservadas[8])
        print('-Falso: ', contador9)
        newReservadas.append(palabras_Reservadas[8])
        texto.pop(posicion9)
    else:
        contador9 = 0
    
    if palabras_Reservadas[9] in texto:
        contador10 = texto.count(palabras_Reservadas[9])
        posicion10 = texto.index(palabras_Reservadas[9])
        print('-Escribir: ', contador10)
        newReservadas.append(palabras_Reservadas[9])
        texto.pop(posicion10)
    else:
        contador10 = 0
    
    if palabras_Reservadas[10] in texto:
        contador11 = texto.count(palabras_Reservadas[10])
        posicion11 = texto.index(palabras_Reservadas[10])
        print('-Leer: ', contador11)
        newReservadas.append(palabras_Reservadas[10])
        texto.pop(posicion11)
    else:
        contador11 = 0
    
    if palabras_Reservadas[11] in texto:
        contador12 = texto.count(palabras_Reservadas[11])
        posicion12 = texto.index(palabras_Reservadas[11])
        print('-FinProceso: ', contador12)
        newReservadas.append(palabras_Reservadas[11])
        texto.pop(posicion12)
    else:
        contador12 = 0

    total = contador + contador2 + contador3 + contador4 + contador5 + contador6 + contador6 + contador7 + contador8 + contador9 + contador10 + contador11 + contador12

    return total, newReservadas, texto

def busqueda_Delimitadores(texto):

    print('Delimitadoresss: ', texto)
    newDelimitadores = []

    if delimitadores[0] in texto:
        contador = texto.count(delimitadores[0])
        posicion = texto.index(delimitadores[0])
        print('-Doble Comilla: ', contador)
        newDelimitadores.append(delimitadores[0])
        texto.pop(posicion)
    else:
        contador = 0
    
    if delimitadores[1] in texto:
        contador2 = texto.count(delimitadores[1])
        posicion2 = texto.index(delimitadores[1])
        print('-Coma: ', contador2)
        newDelimitadores.append(delimitadores[1])
        texto.pop(posicion2)
    else:
        contador2 = 0

    if delimitadores[2] in texto:
        contador3 = texto.count(delimitadores[2])
        posicion3 = texto.index(delimitadores[2])
        print('-Signo Mayor: ', contador3)
        newDelimitadores.append(delimitadores[2])
        texto.pop(posicion3)
    else:
        contador3 = 0

    if delimitadores[3] in texto:
        contador4 = texto.count(delimitadores[3])
        posicion4 = texto.index(delimitadores[3])
        print('-Guion: ', contador4)
        newDelimitadores.append(delimitadores[3])
        texto.pop(posicion4)
    else:
        contador4 = 0
    
    if delimitadores[4] in texto:
        contador5 = texto.count(delimitadores[4])
        posicion5 = texto.index(delimitadores[4])
        print('-Puntos: ', contador5)
        newDelimitadores.append(delimitadores[4])
        texto.pop(posicion5)
    else:
        contador5 = 0

    if delimitadores[5] in texto:
        contador6 = texto.count(delimitadores[5])
        posicion6 = texto.index(delimitadores[5])
        print('-Asterisco: ', contador6)
        newDelimitadores.append(delimitadores[5])
        texto.pop(posicion6)
    else:
        contador6 = 0
    
    if delimitadores[6] in texto:
        contador7 = texto.count(delimitadores[6])
        posicion7 = texto.index(delimitadores[6])
        print('-Simibolo Mas: ', contador7)
        newDelimitadores.append(delimitadores[6])
        texto.pop(posicion7)
    else:
        contador7 = 0
    
    total = contador + contador2 + contador3 + contador4 + contador5 + contador6 + contador7

    return total, newDelimitadores, texto

def busqueda_parentesis(texto):
    newParentesis = []

    if parentesis[0] in texto:
        contador = texto.count(parentesis[0])
        posicion = texto.index(parentesis[0])
        print('-Parentesis Apertura:', contador)
        newParentesis.append(parentesis[0])
        texto.pop(posicion)
    else:
        contador = 0
    
    if parentesis[1] in texto:
        contador2 = texto.count(parentesis[1])
        posicion2 = texto.index(parentesis[1])
        print('-Parentesis de Cierre', contador2)
        newParentesis.append(parentesis[1])
        texto.pop(posicion2)
    else:
        contador2 = 0

    total = contador + contador2 

    return total, newParentesis, texto
    
def busqueda_Variables(texto):
    newVariable = []
    evaluar = re.compile(palabras)

    for palabra in texto:
        cont = evaluar.findall(palabra)
        if len(cont) > 0:
            newVariable.append(cont)
            posicion = texto.index(palabra)
            texto.pop(posicion)
    contador = len(newVariable)

    return contador, newVariable, texto

def busqueda_Digito(texto):
    newDigito = []
    evaluar = re.compile(enteros)
    
    for d in texto:
        h = evaluar.findall(d)
        if len(h) > 0:
            newDigito.append(h)
            posicion = texto.index(d)
            texto.pop(posicion)
    contador = len(newDigito)

    return contador, newDigito, texto