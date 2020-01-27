class Macierz():
    def __init__(self,x,y):
        import random
        self.sety = []
        for j in range(y):
            self.setx = []
            for i in range(x):
                self.setx.append(random.randrange(9+1))
            self.sety.append(self.setx)
    def __add__(self,o):
        self.result = []
        for i in range(len(self.sety)):
            self.result.append([])
        if len(self.sety) == len(o.sety):
            if len(self.sety[0]) == len(o.sety[0]):
                for i in range(len(self.sety)):
                    for j in range(len(self.sety[0])):
                        self.result[i].append(self.sety[i][j] + o.sety[i][j])
        else:
            self.result = []
        return self.result                         
    def view(self):
        for i in self.sety:
            print(i)
                
