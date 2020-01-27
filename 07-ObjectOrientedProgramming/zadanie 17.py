import math
class Figury():
    @staticmethod
    def oblicz_pole_kola(r):
        p_kola = math.pi*r**2
        return p_kola
    @staticmethod
    def oblicz_pole_prostokata(bok1,bok2):
        p_prostokata = bok1 * bok2
        return p_prostokata
    @staticmethod
    def oblicz_pole_trojkata(pod,wys):
        p_trojkata = (1/2)*pod*wys
        return p_trojkata

print(Figury.oblicz_pole_kola(3))
print(Figury.oblicz_pole_prostokata(4,7))
print(Figury.oblicz_pole_trojkata(6,2))