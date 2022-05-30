import tkinter as tk
from logica import *

class interfaz():

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Compiladores e Interpretes")
        self.ventana.geometry("1000x600")
        self.ventana.config(background="#D5E6DD")
     
        self.labelTitulo=tk.Label(self.ventana, text="Analizador de pseudocodigo", width=65, height=2, background="#4C5CA6" ,foreground="#FCF9F9", font=("Tahoma", 22,)).place(x=0,y=45)
        image=tk.PhotoImage(file="Logo.png")
        image= image.subsample(3,3)
        label =tk.Label(image=image, background="#4C5CA6")
        label.place(x=76,y=45, width=158, height=75)

        self.labelSubTitulo=tk.Label(self.ventana, text="Pseudocodigo a evaluar:", background="#D5E6DD", foreground="#596186", font=("Arial", 24)).place(x=355,y=150)

        self.CajaTexto=tk.Text(self.ventana, highlightbackground="#4C5CA6", foreground="#596186", highlightthickness = 2, bd=0, font=("Arial", 17))
        self.CajaTexto.place(x=340,y=201,width=375, height=286)

        self.btn=tk.Button(self.ventana, text="Verificar", background="#4C5CA6", foreground="#FCF9F9", font=("Arial", 14, ), command= lambda:self.VentanaResultado(self.CajaTexto.get('1.0','end')))
        self.btn.place(x=453,y=511, width=150, height=35)

        self.ventana.mainloop()


    def VentanaResultado(self, texto_Codigo):
        self.ventanaNueva = tk.Tk()
        self.ventanaNueva.title("Resultado")
        self.ventanaNueva.geometry("700x550")
        self.ventanaNueva.config(background="#D5E6DD")

        self.labelTitulo2=tk.Label(self.ventanaNueva, text="Resultados Obtenidos", width=45, height=1, background="#4C5CA6", foreground="#FCF9F9", font=("Tahoma", 22,)).place(x=0,y=25)
        

        reservadas = busqueda_Reservadas(texto_Codigo)
        delimitador = busqueda_Delimitadores(texto_Codigo)

        print('----------------')
        print('Reservadas: ', reservadas)
        print('delimitador: ', delimitador)


        self.labelTituloMetodo=tk.Label(self.ventanaNueva, text="Resultado", width=64, height=1,  background="#4C5CA6", foreground="#FCF9F9", font=("Arial", 15,)).place(x=133,y=100, width=450)
        self.cuadro2=tk.Label(self.ventanaNueva, background="#9AA8A8", highlightbackground="#4C5CA6",highlightthickness =1, bd=0).place(x=133,y=129, width=450, height=340)


PrincipalVentana = interfaz()
