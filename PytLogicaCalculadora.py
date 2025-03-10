'''
Created on 3 mar 2025

@author: Yo tambien
'''
from lib2to3.pgen2.token import OP
from tkinter import Tk
from tkinter import messagebox
class Calculadora:
    
    def __init__(self, primerNum=0, operacion="", segundoNum=0):
        self.primerNum = primerNum
        self.segundoNum = segundoNum
        self.operacion = operacion
        
    def sumar(self):
        return float(self.primerNum)    +float(self.segundoNum)
    def masMenos(self):
        return float(self.primerNum) *-1
    def porciento(self):
        return float(self.primerNum) /100
    def dividir(self):
        try:
            return float(self.primerNum)  /float(self.segundoNum)
        except  ZeroDivisionError:
            messagebox.showinfo("ERROR", "You cannot divide a value with zero")
            print("You cannot divide a value with zero")
    def multiplicar(self):
        return float(self.primerNum)  *float(self.segundoNum)
    def restarr(self):
        return float(self.primerNum)  -float(self.segundoNum)
    def Punto(self):
        contador=0
        for caracter in self.primerNum:
            if(caracter=="."):
                #print("yA HAY UN PUNTO")
                contador=1
            elif(caracter!="."):
                print("NOO HAY UN PUNTO")
            print(caracter)
            
        if(contador==0):
            return (self.primerNum+".") 
        elif(contador>=1):
            return (self.primerNum) 
            
    def indicarOperacionConNumero(self,n1, op):
        self.primerNum=n1
        self.operacion=op 
    
    
    def indicarSegundoNumero(self,n2):
        self.segundoNum=n2
        
    def realizarOperacion (self):
        if(self.operacion=="+"):
            return self.sumar()
        elif(self.operacion=="+/-"):
            return self.masMenos()
        elif(self.operacion=="%"):
            return self.porciento()
        elif(self.operacion=="/"):
            return self.dividir()
        elif(self.operacion=="*"):
            return self.multiplicar()
        elif(self.operacion=="-"):
            return self.restarr()
        elif(self.operacion=="."):
            return self.Punto()










