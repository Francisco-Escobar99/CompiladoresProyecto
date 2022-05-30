import re

palabras_Reservadas = ['Proceso','Definir','Como', 'Caracter', 'Entrero','Real','Logico','Verdadero','Falso',
                        'Escribir','Leer','FinProceso']
delimitadores = ['"',',','<','-','.']
letras = '^[A-Z|a-z]+$'
enteros = '^[0-9]+$'

def busqueda_General(codigo):
  texto = codigo.split()

  reservadas = busqueda_Reservadas(texto)
  print('Reservadas: ', reservadas)

def busqueda_Reservadas(texto):

    if palabras_Reservadas[0] in texto:
        contador = texto.count(palabras_Reservadas[0])
        print('Proceso: ', contador)
    else:
        contador = 0
    
    if palabras_Reservadas[1] in texto:
        contador2 = texto.count(palabras_Reservadas[1])
        print('Definir: ', contador2)
    else:
        contador2 = 0
    
    if palabras_Reservadas[2] in texto:
        contador3 = texto.count(palabras_Reservadas[2])
        print('Como: ', contador3)
    else:
        contador3 = 0
    
    if palabras_Reservadas[3] in texto:
        contador4 = texto.count(palabras_Reservadas[3])
        print('Caracter: ', contador4)
    else:
        contador4 = 0
    
    if palabras_Reservadas[4] in texto:
        contador5 = texto.count(palabras_Reservadas[4])
        print('Entero: ', contador5)
    else:
        contador5 = 0
    
    if palabras_Reservadas[5] in texto:
        contador6 = texto.count(palabras_Reservadas[5])
        print('Real: ', contador6)
    else:
        contador6 = 0
    
    if palabras_Reservadas[6] in texto:
        contador7 = texto.count(palabras_Reservadas[6])
        print('Logico: ', contador7)
    else:
        contador7 = 0
    
    if palabras_Reservadas[7] in texto:
        contador8 = texto.count(palabras_Reservadas[7])
        print('Verdadero: ', contador8)
    else:
        contador8 = 0
    
    if palabras_Reservadas[8] in texto:
        contador9 = texto.count(palabras_Reservadas[8])
        print('Falso: ', contador9)
    else:
        contador9 = 0
    
    if palabras_Reservadas[9] in texto:
        contador10 = texto.count(palabras_Reservadas[9])
        print('Escribir: ', contador10)
    else:
        contador10 = 0
    
    if palabras_Reservadas[10] in texto:
        contador11 = texto.count(palabras_Reservadas[10])
        print('Leer: ', contador11)
    else:
        contador11 = 0
    
    if palabras_Reservadas[11] in texto:
        contador12 = texto.count(palabras_Reservadas[11])
        print('FinProceso: ', contador12)
    else:
        contador12 = 0

    total = contador + contador2 + contador3 + contador4 + contador5 + contador6 + contador6 + contador7 + contador8 + contador9 + contador10 + contador11 + contador12

    return total

