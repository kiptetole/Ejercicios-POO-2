'''
Clase Vehiculo
Subclases Coche y bicicleta

@author: Jose Notario Millan
'''

class Vehiculo():  
    
    def __init__(self, km):
        self.kmRecorridos = km
        self.arrancar = False 
    
        
    def menu(self):
        print("---------Vehiculos---------"
              ,"\n1. Anda con la Bicicleta. "
              ,"\n2. Haz el caballito con la bicicleta."
              ,"\n3. Anda con el coche."
              ,"\n4. Quema rueda con el coche."
              ,"\n5. Ver Kilometraje de la bicicleta"
              ,"\n6. Ver Kilometraje del coche."
              ,"\n7. Ver Kilometraje total"
              ,"\n8. Salir"
              ,"\n---Elija alguna opcion (Entre 1-8)---")
        
    def avanza(self, km):
        self.kmRecorridos = self.kmRecorridos + km
        kmtotales = km