'''
Ejercicio del terminal.

@author: Jose Notario Millan
'''

class Terminal():
    
    def __init__(self, numero):
        
        self.Numero = numero
        self.TiempoDeConversacion =0
        
        
    def llama (self, t, Tiempo):
        
        self.TiempoDeConversacion += Tiempo
        t.TiempoDeConversacion += Tiempo
        
    def __str__(self):
        print("nº",self.Numero,"-",self.TiempoDeConversacion,"segs en contestar")