from tkinter import *
from logica import *


class Table(): 
    def __init__(self,VentanaTokens): 
          
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                self.e = Entry(VentanaTokens, width=30, fg='black', 
                               font=('Arial',13,)) 
                  
                self.e.grid(row=i, column=j) 
                self.e.insert(END, lst[i][j]) 
  
lst = [('Palabras reservadas',2), 
       ('Delimitadores',1), 
       ('Parentesis',20), 
       ('Palabras',21), 
       ('Enteros',21)] 
   
total_rows = len(lst) 
total_columns = len(lst[0]) 
   
VentanaTokens = Tk() 
t = Table(VentanaTokens) 
VentanaTokens.title("Tabla Tokens")
VentanaTokens.mainloop() 