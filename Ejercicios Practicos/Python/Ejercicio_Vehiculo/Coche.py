'''
Subclase Coche

@author: Jose Notario Millan.
'''
## Importa la superclase Vehiculo. ##
from Ejercicio_Vehiculo.Vehiculo import Vehiculo

class Coche(Vehiculo):
    
    def quemarRueda(self):
        return "Quemando rueda........"