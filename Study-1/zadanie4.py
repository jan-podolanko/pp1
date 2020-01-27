class Zbiory():
    @staticmethod
    def iloczyn(x,y):
        z = []
        for i in x:
            if i in y:
                if i not in z:
                    z.append(i)
        return z
    @staticmethod
    def suma(x,y):
        z = []
        for i in x:
            if i not in z:
                z.append(i)
        for i in y:
            if i not in z:
                z.append(i)
        return z
    @staticmethod
    def roznica(x,y):
        z = []
        for i in x:
            if i not in y:
                if i not in z:
                    z.append(i)
        return z
    
    
g = [1,2,3,4,5]
h = [4,5,6,7,8]
p = Zbiory()
print(p.suma(g,h))
print(p.roznica(g,h))
print(p.iloczyn(g,h))
            