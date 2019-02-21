'''
Prueba de clase tiempo

@author: Jose Notario Millan
'''
from Ejercicio_Tiempo.Tiempo import Tiempo

reloj = Tiempo(12,20,30)

contador = 0
while contador!=3:
    reloj.menu()
    contador = int(input())
    
    if contador == 1:
        h = int(input("Horas a sumar:"))
        mun = int(input("Minutos a sumar: "))
        seg = int(input("segundos a sumar: "))
        reloj.sumar(h, mun, seg)
        
    if contador == 2:
        h = int(input("Horas a restar:"))
        mun = int(input("Minutos a restar: "))
        seg = int(input("segundos a restar: "))
        reloj.restar(-h, -mun, -seg)
        
    
    if contador == 3:
        print("----Adios ;)----.")
        
    if contador <=0 and contador >3:
        print("No existe esa funcion.")