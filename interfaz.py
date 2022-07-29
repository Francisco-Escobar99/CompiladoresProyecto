import tkinter as tk

from logica import busqueda_Delimitadores, busqueda_Digito, busqueda_parentesis, busqueda_Reservadas, busqueda_Variables
from sintactico import *
from semantico import *

class interfaz():

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Compiladores e Interpretes")
        self.ventana.geometry("1200x700")
        self.ventana.config(background="#D5E6DD")
        self.ventana.resizable(0,0)
     
        self.labelTitulo=tk.Label(self.ventana, text="Analizador de pseudocodigo", width=78, height=2, background="#4C5CA6" ,foreground="#FCF9F9", font=("Tahoma", 22,)).place(x=0,y=45)
        self.labelSubTitulo=tk.Label(self.ventana, text="Pseudocodigo a evaluar:", background="#D5E6DD", foreground="#596186", font=("Arial", 17)).place(x=125,y=221)

        self.CajaTexto=tk.Text(self.ventana, highlightbackground="#4C5CA6", foreground="#596186", highlightthickness = 2, bd=0, font=("Arial", 17))
        self.CajaTexto.place(x=60,y=259,width=375, height=286)

        self.btn=tk.Button(self.ventana, text="Verificar", background="#4C5CA6", foreground="#FCF9F9", font=("Arial", 14, ), command= lambda:sintaxis(self.CajaTexto.get('1.0','end')))
        self.btn.place(x=83,y=569, width=150, height=35)

        self.btntraducir=tk.Button(self.ventana, text="Traducir",  background="#4C5CA6", foreground="#FCF9F9", font=("Arial", 14,),command=lambda:imprimir1())
        self.btntraducir.place(x=268,y=569, width=150, height=35)

        self.btnLexico=tk.Button(self.ventana, text="Tokens",  background="#4C5CA6", foreground="#FCF9F9", font=("Arial", 14,),command=lambda:self.VentanaResultado(self.CajaTexto.get('1.0','end')))
        self.btnLexico.place(x=83,y=615, width=150, height=35)

        #Python
        self.fondoPy=tk.Label(self.ventana, background="white", highlightbackground="#4C5CA6", foreground="#596186", highlightthickness = 2, bd=0,).place( x=450, y= 221, width=365, height=400)
        self.tituloPython=tk.Label(self.ventana, text="Python", background="#D5E6DD", foreground="#596186", font=("Arial", 17)).place(x=612,y=175)

        #Java
        self.fondoJava=tk.Label(self.ventana, background="white", highlightbackground="#4C5CA6", foreground="#596186", highlightthickness = 2, bd=0,).place( x=815, y= 221, width=365, height=400)
        self.tituloJava=tk.Label(self.ventana, text="Java", background="#D5E6DD", foreground="#596186", font=("Arial", 17)).place(x=972,y=175)

        def imprimir1():
    
            listas = traductor(self.CajaTexto.get('1.0','end'))
            listas2 = traductor2(self.CajaTexto.get('1.0','end'))

            print(listas)
            print(listas2)
            print(len(listas2))

            palabra1 = listas[0] +'  ' + listas[1] + '()' +':'
            palabra2 = listas[2] + listas[3]
            palabra3 = listas[4] + '(' + listas[5] + listas[6] + listas[7] + ')'
            palabra4 = listas[8] + listas[9]

            palabra5 = listas2[0] + '  ' + listas2[1] + ' ' + listas2[2]
            palabra6 = listas2[3]
            palabra7 = listas2[4]
            palabra8 = listas2[5] +' ' + listas2[6] +' ' + listas2[7]
            palabra9 = listas2[8] + listas2[9] + listas2[10] + listas2[11] + listas2[12]
            palabra10 =listas2[13] + ' ' + listas2[14]
            palabra11 = listas2[15]

            # python 
            label1 = tk.Label(self.ventana, background="white", text=palabra1, font=('Arial',14)).place(x=480, y=240)
            label2 = tk.Label(self.ventana, background='white', text=palabra2, font=('Arial',14)).place(x=480, y=300)
            label3 = tk.Label(self.ventana, background='white', text=palabra3, font=('Arial',14)).place(x=480, y=400)
            label4 = tk.Label(self.ventana, background='white', text=palabra4, font=('Arial',14)).place(x=480, y=500)

            #Java
            label5 = tk.Label(self.ventana, background="white", text=palabra5, font=('Arial',14)).place(x=830, y=240)
            label6 = tk.Label(self.ventana, background='white', text=palabra6, font=('Arial',14)).place(x=830, y=280)
            label7 = tk.Label(self.ventana, background='white', text=palabra7, font=('Arial',14)).place(x=830, y=340)
            label8 = tk.Label(self.ventana, background='white', text=palabra8, font=('Arial',14)).place(x=830, y=380)
            label9 = tk.Label(self.ventana, background="white", text=palabra9, font=('Arial',14)).place(x=830, y=450)
            label10 = tk.Label(self.ventana, background='white', text=palabra10, font=('Arial',14)).place(x=830, y=480)
            label11 = tk.Label(self.ventana, background='white', text=palabra11, font=('Arial',14)).place(x=830, y=540)


        self.ventana.mainloop()


    def VentanaResultado(self, texto_Codigo):
        self.ventanaNueva = tk.Tk()
        self.ventanaNueva.title("Resultado")
        self.ventanaNueva.geometry("1000x640")
        self.ventanaNueva.resizable(0,0)
        self.ventanaNueva.config(background="#D5E6DD")

        self.labelTitulo2=tk.Label(self.ventanaNueva, text="Resultados Obtenidos", width=65, height=1, background="#4C5CA6", foreground="#FCF9F9", font=("Tahoma", 22,)).place(x=0,y=25)
        
        cant_reservadas, reservadas, newTexto = busqueda_Reservadas(texto_Codigo)
        cant_delimitador, delimitador, newTexto2 = busqueda_Delimitadores(newTexto)
        cant_parentesis, parentesis, newTexto3  = busqueda_parentesis(newTexto2)
        cant_Digitos, Digitos, newTexto4 = busqueda_Digito(newTexto3)
        cant_Variable, Variables, Errores = busqueda_Variables(newTexto4)

        print('----------------')
        print('Reservadas: ', cant_reservadas ,' = ',reservadas)
        print('Delimitador: ', cant_delimitador, ' = ' ,delimitador)
        print('Parentesis', cant_parentesis, ' =  ', parentesis)
        print('Variables: ', cant_Variable, '= ', Variables)
        print('Digitos: ', cant_Digitos, ' = ', Digitos)
        print('Errores: ', len(Errores), ' = ', Errores)


        self.labelTituloMetodo=tk.Label(self.ventanaNueva, text="Token", width=64, height=1,  background="#4C5CA6", foreground="#FCF9F9", font=("Arial", 15,)).place(x=100,y=100, width=800)
        self.cuadro2=tk.Label(self.ventanaNueva, background="#9AA8A8", highlightbackground="#4C5CA6",highlightthickness =1, bd=0).place(x=100,y=129, width=800, height=480)
        self.labelError=tk.Label(self.ventanaNueva, text="Error", width=64, height=1,  background="#4C5CA6", foreground="#FCF9F9", font=("Arial", 15,)).place(x=100,y=440, width=800)
        self.labelReservada=tk.Label(self.ventanaNueva, background="#9AA8A8",text="Palabras Reservadas:", font=("Arial", 20)).place(x=143,y=165, width=270)
        self.labelDelimitadores=tk.Label(self.ventanaNueva, background="#9AA8A8",text="Delimitadores:", font=("Arial", 20)).place(x=139,y=205, width=190)
        self.labelParentesis=tk.Label(self.ventanaNueva, background="#9AA8A8",text="Parentesis:", font=("Arial", 20)).place(x=142,y=240, width=150)
        self.labelPalabras=tk.Label(self.ventanaNueva, background="#9AA8A8",text="Palabras:", font=("Arial", 20)).place(x=135,y=278, width=130)
        self.labelEntero=tk.Label(self.ventanaNueva, background="#9AA8A8",text="Enteros:", font=("Arial", 20)).place(x=135,y=320, width=130)

        tk.Label(self.ventanaNueva, background="#9AA8A8",text=cant_reservadas, font=("Arial", 20)).place(x=420,y=165)
        tk.Label(self.ventanaNueva, background="#9AA8A8",text=cant_delimitador, font=("Arial", 20)).place(x=360,y=205)
        tk.Label(self.ventanaNueva, background="#9AA8A8",text=cant_parentesis, font=("Arial", 20)).place(x=360,y=240)
        tk.Label(self.ventanaNueva, background="#9AA8A8",text=cant_Variable, font=("Arial", 20)).place(x=300,y=278)
        tk.Label(self.ventanaNueva, background="#9AA8A8",text=cant_Digitos, font=("Arial", 20)).place(x=300,y=320)


        tk.Label(self.ventanaNueva, background="#9AA8A8",text=reservadas, font=("Arial", 14)).place(x=470,y=165)
        tk.Label(self.ventanaNueva, background="#9AA8A8",text=delimitador, font=("Arial", 14)).place(x=430,y=205)
        tk.Label(self.ventanaNueva, background="#9AA8A8",text=parentesis, font=("Arial", 14)).place(x=400,y=240)
        tk.Label(self.ventanaNueva, background="#9AA8A8",text=Variables, font=("Arial", 14)).place(x=400,y=278)
        tk.Label(self.ventanaNueva, background="#9AA8A8",text=Digitos, font=("Arial", 14)).place(x=400,y=320)
        tk.Label(self.ventanaNueva, background="#9AA8A8",text= Errores, font=("Arial", 14)).place(x=200,y=500)

      

        
    
    

PrincipalVentana = interfaz()



