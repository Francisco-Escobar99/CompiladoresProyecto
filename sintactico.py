from tabla import tablaAnalisis as tabla, gramatica as g
from tkinter import messagebox as ms
import re


letras = '^[a-zA-Z][a-zA-Z]+$'
digitos = '^[0-9]+|[0-9]\.[0.9]$'

def sintaxis(palabras):

    palabras = palabras.split()

    pila = ['G']
    indice = 0
    bandera = True

    while True:
        cima = pila.pop()

        if cima in g.no_Terminales:
            print('Cima Pila: ', cima)

            for posicion in tabla.diccionario:
                if cima == posicion:
                    print('Se elimina a: ', cima, 'de la Pila')
                    print('Se agregan reglas de: ', posicion, 'a la Pila')

                    for dato in tabla.diccionario[posicion]['produccion']:
                        pila.append(dato)
                    print('Contenido Pila: ', pila)
        else:

            if cima == 'a...z':
                evaluando_Letra = re.search(letras, palabras[indice])
                if evaluando_Letra: 
                    print('Cumple Expresion')
                    cima = palabras[indice]
                else:
                    print('Error de sintaxis', palabras[indice])
                    ms.showerror('Error', 'Error de Sintaxis')
                    bandera = False
                    break
            
            if cima == '0...9':
                evaluando_Digito = re.search(digitos, palabras[indice])
                if evaluando_Digito:
                    cima = palabras[indice]
                else:
                    print('Error de Sintaxis', palabras[indice])
                    ms.showerror('Error', 'Error de Sintaxis')
                    bandera = False
                    break
            # if(palabras[indice+1] == ","):
            #     pila.append("L")
            #     pila.append(",")

            if(cima=="-"):
                pila.pop()
            
            if cima == palabras[indice]:
                indice += 1
                print('Extrae: ', cima, 'De La Pila')
                print('Pila: ', pila)
            else:
                print('Error de Sintaxis', palabras[indice])
                ms.showerror('Error', 'Error de Sintaxis')
                bandera = False
                break
            
            if len(pila) == 0:
                print('PILA VACIA')
                if indice == len(palabras):
                    print('ENTRADA VACIA')
                    ms.showwarning('Advertencia', 'Entrada y Pila vacias')
                    bandera = False
                else:
                    print('ENTRADA CON DATOS')
                    ms.showwarning("Advertencia","CADENA DE ENTRADA CON DATOS")   
                    bandera = False
                    break
            
            if indice == len(palabras):
                print('ENTRADA VACIA')
                ms.showinfo("Informacion", "Pila con datos, entrada vacia!")
                print('Contenido de Pila: ', pila)
                bandera = False
                break
        
        if bandera == False:
            break

activarboton = 1
   


    