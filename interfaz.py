import tkinter as tk
from logica import *

class interfaz():

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Compiladores e Interpretes")
        self.ventana.geometry("1000x600")
        self.ventana.config(background="#D5E6DD")
        self.ventana.resizable(0,0)
     
        self.labelTitulo=tk.Label(self.ventana, text="Analizador de pseudocodigo", width=65, height=2, background="#4C5CA6" ,foreground="#FCF9F9", font=("Tahoma", 22,)).place(x=0,y=45)
        #image=tk.PhotoImage(file="Logo.png")
        #image= image.subsample(3,3)
        #label =tk.Label(image=image, background="#4C5CA6")
       # label.place(x=76,y=45, width=158, height=75)

        self.labelSubTitulo=tk.Label(self.ventana, text="Pseudocodigo a evaluar:", background="#D5E6DD", foreground="#596186", font=("Arial", 24)).place(x=355,y=150)

        self.CajaTexto=tk.Text(self.ventana, highlightbackground="#4C5CA6", foreground="#596186", highlightthickness = 2, bd=0, font=("Arial", 17))
        self.CajaTexto.place(x=340,y=201,width=375, height=286)

        self.btn=tk.Button(self.ventana, text="Verificar", background="#4C5CA6", foreground="#FCF9F9", font=("Arial", 14, ), command= lambda:self.VentanaResultado(self.CajaTexto.get('1.0','end')))
        self.btn.place(x=453,y=511, width=150, height=35)

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
