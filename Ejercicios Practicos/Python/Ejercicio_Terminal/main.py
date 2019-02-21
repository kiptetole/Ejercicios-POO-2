'''
Prueba de Terminal.

@author: Jose Notario Millan
'''
from Ejercicio_Terminal.Terminal import Terminal
from Ejercicio_Terminal.Movil import Movil

t1 = Terminal("678 11 22 33")
t2 = Terminal("678 12 44 53")
t3 = Terminal("622 32 89 09")
t4 = Terminal("664 73 98 18")
t1.llama(t2, 350)
t1.llama(t3, 500)
t1.__str__()
t2.__str__()
t3.__str__()
t4.__str__()

'''
Esta parte es la prueba de movil (Subclase de Terminal)
'''

m1 = Movil("678 11 22 33", "rata")
m2 = Movil("644 74 44 69", "mono")
m3 = Movil("622 32 89 09", "bisonte")
m1.llama(m2, 50)
m2.llama(m3, 30)
m1.__str__()
m2.__str__()
m3.__str__()