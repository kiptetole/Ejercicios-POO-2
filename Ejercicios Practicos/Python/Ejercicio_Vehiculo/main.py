'''
Clase de prueba de todas las clases.

@author: Jose Notario Millan.
'''
from Ejercicio_Vehiculo.Coche import Coche
from Ejercicio_Vehiculo.Bicicleta import Bicicleta

bicicleta = Bicicleta(10,3)
coche = Coche(20)

contador=0
while contador != 8:
    bicicleta.menu()
    contador = int(input())
    
    if contador == 1:
        km = int(input("Introduce los km a avanzar: "))
        bicicleta.avanza(km)
        print("La bicicleta avanza",km,"km y en total ha recorrido",bicicleta.kmRecorridos)
    
    if contador == 2:
        print(bicicleta.hazCaballito())
        
    if contador == 3:
        km = int(input("Introduce los km a avanzar: "))
        coche.avanza(km)
        print("El Coche avanza",km,"km y en total ha recorrido",coche.kmRecorridos)
    
    if contador == 4:
        print(coche.quemarRueda())
        
    if contador == 5:
        print("Los km recorridos por la bicicleta son :", bicicleta.kmRecorridos)
        
    if contador == 6:
        print("Los km recorridos por el coche son:", coche.kmRecorridos)
    
    if contador == 7:
        print("Los km totales entre ambos vehiculos son:", bicicleta.kmRecorridos+coche.kmRecorridos)
    
    if contador == 8:
        print("    Hasta Luego ;)      ")
        
    if contador<=0 and contador>8:
        print("Introduzca esto de nuevo")