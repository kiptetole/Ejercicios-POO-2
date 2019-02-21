'''
Clase Tiempo

    tres variables locales Horas Minutos Segundos
    
    Metodos:
    - Suma minutos segundos.
    - Resta minutos segundos.
    
@author: Jose Notario Millan.
'''

class Tiempo():
    ## Constructor de la clase Tiempo ##
    def __init__(self,h,mun,seg):
        
        contador = 0
        while seg>59:
            contador = contador + 1
            seg = seg - 60
        self.minutos = contador
        mun = mun + contador
        contador = 0
        while mun > 59:
            contador = contador + 1
            seg = seg - 60
        h = h + contador
        while h > 23:
            h = h - 24
            
        self.segundos = seg
        self.minutos = mun 
        self.horas = h
    ## Menu de seleccion ##  
    def menu(self):
        print("----Menu Tiempo-----")
        self.__str__()
        print("1. Sumar.")
        print("2. Restar.")
        print("3. Salir menu.")
    
    ## Muestra el estado del objeto ##
    def __str__(self):
        print('Hora:',self.horas,'h -',self.minutos,'min -',self.segundos,'segs')
    
    ## Suma una hora a la guardada por medio de parametro ##
    def sumar(self, h,mun,seg):
        
        contador = 0
        seg = self.segundos + seg 
        while seg>59:
            contador = contador + 1
            seg = seg - 60
        mun = mun + contador + self.minutos
        contador = 0
        while mun > 59:
            contador = contador + 1
            mun = mun - 60
        h = h + contador + self.horas
        while h > 23:
            h = h - 24

        self.segundos = seg 
        self.minutos = mun
        self.horas = h 
        
    ## Resta una hora a la guardada por medio de parametro ##
    def restar(self, h, mun, seg):
        
        contador = 0
        seg = self.segundos + seg
        while seg<0:
            contador = contador - 1
            seg = seg + 60
        mun = self.minutos + mun + contador
        while mun<0:
            contador = contador - 1
            mun = mun + 60
        contador = 0
        h = self.horas + h + contador
        while h<0:
            h = h + 24
            
        self.segundos = seg 
        self.minutos = mun
        self.horas = h 