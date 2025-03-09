'''
Created on 3 mar 2025

@author: Yo tambien
'''
from lib2to3.pgen2.token import OP
from tkinter import Tk
class Calculadora:
    
    def __init__(self, primerNum=0, operacion="", segundoNum=0):
        self.primerNum = primerNum
        self.segundoNum = segundoNum
        self.operacion = operacion
        
    def sumar(self):
        return float(self.primerNum)    +float(self.segundoNum)
    
    def indicarOperacionConNumero(self,n1, op):
        self.primerNum=n1
        self.operacion=op 
        
    def indicarSegundoNumero(self,n2):
        self.segundoNum=n2
        
    def realizarOperacion (self):
        if(self.operacion=="+"):
            return self.sumar()
        










