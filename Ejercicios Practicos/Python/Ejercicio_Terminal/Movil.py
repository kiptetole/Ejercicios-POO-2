'''
Subclase movil.

@author: Jose Notario Millan.
'''
from Ejercicio_Terminal.Terminal import Terminal

class Movil(Terminal):
    
    def __init__(self,numero,tarifa):
        Terminal.__init__(self, numero)
        self.tarifa = tarifa
        self.coste = 0
    
    def llama(self,t,Tiempo):
        Terminal.llama(self, t,Tiempo)
        
        if self.tarifa == "rata": 
            self.coste = Tiempo * 0.06
            
        if self.tarifa == "mono":
            self.coste = Tiempo * 0.12
            
        if self.tarifa == "bisonte":
            self.coste = Tiempo * 0.3
            
    def __str__(self):
        Terminal.__str__(self)
        print("El coste de la llamada a sido de: ", "%.2f" % self.coste, "euros")  ## "%.2f" % self.coste Redondeo a dos decimales.