#zadanie3

class Prostokat():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.pole = a*b
    def __add__(self,o):
        return self.pole + o.pole
