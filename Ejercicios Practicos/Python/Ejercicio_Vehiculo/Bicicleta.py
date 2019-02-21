'''
Clase Bicicleta

@author: Jose Notario Millan.
'''
from Ejercicio_Vehiculo.Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    
    def __init__(self, km, p):
        Vehiculo.__init__(self, km)
        self.pinones = p 
    
    def hazCaballito(self):
        return "Estoy haciendo el caballito"
    