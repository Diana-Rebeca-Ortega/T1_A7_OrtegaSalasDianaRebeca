'''
Created on 3 mar 2025

@author: Yo
'''
from tkinter import *
from tkinter import  messagebox as msg
from PytLogicaCalculadora import Calculadora
import tkinter as tk
from pip._vendor.rich.table import Column

calcu = Calculadora()

ventana_inicio =  Tk()
ventana_inicio.title("Calculadora Sencilla")
ventana_inicio.geometry("450x500")

numeros = StringVar()
caja_operaciones = Entry(ventana_inicio, bg='#C2FFC7', 
                        fg='#526E48', font=("roboto", 20, "bold"),
                        width=30, 
                        justify=tk.RIGHT,
                        textvariable=numeros)

caja_operaciones.grid(row=0, columnspan=4)

#def formatoBoton (Button, comando, fila=0, columna=0, texto=""):
    #boton= Button(ventana_inicio, text=texto, width=8, height=3, bg="#9EDF9C", fg="#62825D",font=("roboto", 15, "bold"),
        #           command=comando )
   # boton.grid(row=fila, column=columna)
def formatoBotonNumeros (Button, fila=0, columna=0, texto=""):
    boton= Button(ventana_inicio, text=texto, width=8, height=3, bg="#9EDF9C", fg="#62825D",font=("roboto", 15, "bold"),
                  command=lambda:mostrarNumero(texto))
    boton.grid(row=fila, column=columna)   
    
##Declaracion de variables     
btn_ac, btnMas_Menos, btn_Porciento, btn_Entre,btn_Por, btn_Menos,btn_Mas=Button,Button,Button,Button,Button,Button,Button
btn_7,btn8,btn9,btn_4,btn5,btn6,btn_1,btn2,btn3, btnPunto, btn0=Button,Button,Button,Button,Button,Button,Button,Button,Button,Button,Button
##Metodo de POO PRIMERA FILA

#formatoBoton(btn_ac,1,0, "AC")
#formatoBoton(btnMas_Menos, 1, 1, "+/-")
#formatoBoton(btn_Porciento, 1, 2, "%")
#formatoBoton(btn_Entre, 1, 3, "/")
def indicarAC():
    numeros.set("")
btn_ac = Button(ventana_inicio, text="AC",width=8, height=3, bg="#9EDF9C", fg="#62825D",font=("roboto", 15, "bold") , command=indicarAC)
btn_ac.grid(row=1, column=0)

def indicarMasMenos():
    calcu.indicarOperacionConNumero(numeros.get(), "+/-")
    numeros.set(calcu.realizarOperacion())
btnMas_Menos = Button(ventana_inicio, text="+/-",width=8, height=3, bg="#9EDF9C", fg="#62825D",font=("roboto", 15, "bold") , command=indicarMasMenos)
btnMas_Menos.grid(row=1, column=1)

def indicarPorciento():
    calcu.indicarOperacionConNumero(numeros.get(), "%")
    numeros.set(calcu.realizarOperacion())
btn_Porciento = Button(ventana_inicio, text="%",width=8, height=3, bg="#9EDF9C", fg="#62825D",font=("roboto", 15, "bold") , command=indicarPorciento)
btn_Porciento.grid(row=1, column=2)

def indicarDivision():
    calcu.indicarOperacionConNumero(numeros.get(), "/")
    numeros.set("")
btn_Entre = Button(ventana_inicio, text="/",width=8, height=3, bg="#9EDF9C", fg="#62825D",font=("roboto", 15, "bold") , command=indicarDivision)
btn_Entre.grid(row=1, column=3)

def mostrarNumero(num):
    
    #msg.showinfo("title", "7")
    numeros.set(numeros.get()+ num)

##segunda fila
formatoBotonNumeros(btn_7, 2, 0, "7")
formatoBotonNumeros(btn8, 2, 1, "8")
formatoBotonNumeros(btn9, 2, 2,"9")
#formatoBoton(btn_Por, 2, 3, "x")
def indicarMultiplicacion():
    calcu.indicarOperacionConNumero(numeros.get(), "*")
    numeros.set("")
btn_Por = Button(ventana_inicio, text="*",width=8, height=3, bg="#9EDF9C", fg="#62825D",font=("roboto", 15, "bold") , command=indicarMultiplicacion)
btn_Por.grid(row=2, column=3)


##TERCERA fila
formatoBotonNumeros(btn_4, 3,0 , "4")
formatoBotonNumeros(btn5,3,1,"5")
formatoBotonNumeros(btn6,3,2,"6")
#formatoBoton(btn_Menos,3,3,"-")
def indicarResta():
    calcu.indicarOperacionConNumero(numeros.get(), "-")
    numeros.set("")
btn_Menos = Button(ventana_inicio, text="-",width=8, height=3, bg="#9EDF9C", fg="#62825D",font=("roboto", 15, "bold") , command=indicarResta)
btn_Menos.grid(row=3, column=3)

##CUARTA fila
formatoBotonNumeros(btn_1,4,0,"1")
formatoBotonNumeros(btn2,4,1,"2")
formatoBotonNumeros(btn3,4,2,"3")

def indicarSuma():
    calcu.indicarOperacionConNumero(numeros.get(), "+")
    numeros.set("")

#formatoBoton(btn_Mas, comando_indicarSuma(),4,3,"+")

btn_Mas = Button(ventana_inicio, text="+",width=8, height=3, bg="#9EDF9C", fg="#62825D",font=("roboto", 15, "bold") ,
                 command=indicarSuma)
btn_Mas.grid(row=4, column=3)


btn_z = Button(ventana_inicio, text="Mood", width=8, height=3, bg="#9EDF9C", fg="#62825D",font=("roboto", 15, "bold"))         
btn_z.grid(row=5, column=0)

formatoBotonNumeros( btn0,5,1,"0" )
def indicarPunto():
    calcu.indicarOperacionConNumero(numeros.get(), ".")
    numeros.set(calcu.realizarOperacion())
    
btnPunto = Button(ventana_inicio, text=".",width=8, height=3, bg="#9EDF9C", fg="#62825D",font=("roboto", 15, "bold") ,
                 command=indicarPunto)
btnPunto.grid(row=5, column=2)



def calcularResultado():
    calcu.indicarSegundoNumero(numeros.get())
    numeros.set(calcu.realizarOperacion())

btn_Igual = Button(ventana_inicio, text="=", width=8, height=3, bg="#9EDF9C", fg="#62825D",font=("roboto", 15, "bold") ,
                   command=calcularResultado
                   )
btn_Igual.grid(row=5, column=3)



ventana_inicio.mainloop()


