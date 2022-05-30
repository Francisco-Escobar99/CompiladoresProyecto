import re

palabras_Reservadas = ['Proceso','Definir','Como', 'Caracter', 'Entrero','Real','Logico','Verdadero','Falso',
                        'Ecribir','Leer','FinProceso']
delimitadores = ['"',',','<','-','.']
letras = '^[A-Z|a-z]+$'
enteros = '^[0-9]+$'