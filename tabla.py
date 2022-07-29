

class tablaAnalisis:
    diccionario = {
       'G' : {'produccion': ['BLOQUE4', 'BLOQUE3', 'BLOQUE2', 'BLOQUE1']},
       'BLOQUE1' : {'produccion': ['L', 'Proceso']},
       'L': {'produccion': ['Letra']},
        'Letra': {'produccion': ['a...z']},
        'BLOQUE2': {'produccion': ['TD', 'C', 'VP', 'L', 'Definir']},
        'VP': {'produccion': ['VP','-','L', ',']},
        'C': {'produccion': ['Como']},
        'TD': {'produccion': ['Caracter']},
        # 'TD2': {'produccion': ['Entero']},
        # 'TD3': {'produccion': ['Logico']},
        # 'TD4': {'produccion': ['Real']},
        'BLOQUE3': {'produccion': ['Contenido2','Valor', '<-', 'L']},
        # 'BLOQUE3': {'produccion': ['Contenido2']},
        'Valor': {'produccion': ['D']},
        # 'Valor2': {'produccion': ['"', 'L', '"']},
        # 'Valor3': {'produccion': ['Verdadero']},
        # 'Valor3': {'produccion': ['Falso']},
        'D': {'produccion': ['0...9']},
        # 'RD': {'produccion': ['RD', 'D']},
        'Contenido2': {'produccion': ['L', 'Leer', '"', 'L', '"', 'Escribir']},
        'BLOQUE4': {'produccion': ['FinProceso']},
    }

class gramatica:
    no_Terminales = [
        'G', 'BLOQUE1', 'L', 'Letra', 'BLOQUE2', 'VP', 
        'C', 'TD', 'BLOQUE3', 'Valor', 'D', 'Contenido2',
        'RC', 'BLOQUE4'
    ]