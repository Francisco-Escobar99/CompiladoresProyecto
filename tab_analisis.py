
class tabla:

    G = {'Proceso' : 'G -> BLOQUE1 BLOQUE2 BLOQUE3 BLOQUE4'}
    BLOQUE1 = {'Proceso' : 'BLOQUE1 -> Proceso L'}
    L = {'a...z' : 'R -> Letra RL', 'A...Z': 'L -> Letra RL'}
    RL = {'"' : 'RL -> ∈', 'A...Z' : 'RL -> Letra RL', 'a...z' : 'RL -> Letra RL', ',' : 'RL -> ∈', '<-' : 'RL -> ∈', 'Definir' : 'RL -> ∈', 'Escribir': 'RL -> ∈'}
    Letra = {'a...z' : 'Letra -> a..z', 'A...Z' : 'Letra -> A...Z'}
    BLOQUE2 = {'Definir' : 'BLOQUE2 -> Definir L VP C TD'}
    VP = {',' : 'VP -> , L VP', 'Como': 'VP -> ∈'}
    C = {'Como' : 'C -> Como'}
    TP = {'Caracter' : 'TD -> Carácter', 'Entero' : 'TD -> Entero', 'Logico' : 'TD -> Logico', 'Real' : 'TD -> Real'}
    BLOQUE3 = {'a...z' : 'BLOQUE3 -> L <- Valor', 'A...Z' : 'BLOQUE3 -> L <- Valor', 'Escribir' : 'BLOQUE3 -> Contenido2 RC'}
    Valor = {'0...9' : 'Valor -> D | D .  RD ', '"' : 'Valor -> "L', 'Verdadero' : 'Valor ->  Verdadero', 'Falso' : 'Valor ->  Falso'}
    D = {'0...9' : 'D -> 0...9'}
    RD = {'0...9' : 'RD -> D RD'}
    Contenido2 = {'Escribir': 'Contenido2 -> Escribir “ L “ Leer L'}
    RC = {'Escribir': 'RC -> Contenido2 RC', 'FinProceso' : 'RC->∈'}
    BLOQUE4 = {'FinProceso':'BLOQUE4 -> FinProceso'}


#    diccionario = {
#      'BLOQUE1': {'Proceso', 'L'},
#      'L': {'Letra RL'},
#      'RL' : {'Letra RL'},
#      'Letra' : {'a...z','A...Z'},
#      'BLOQUE2' : {'Definir L VP C TD'},
#      'VP' : {' L VP'},
#      'C' : {'Como'},
#      'TP':{'Carcter', 'Entero', 'Lógico', 'Real'},
#      'BLOQUE3':{'L <- Valor'},
#    }

    