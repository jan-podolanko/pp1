class Miasto():
    def __init__(self,x,y):
        if type(x) != str:
            raise TypeError('Nazwa musi byc typu str')
        if type(y) != int:
            if type(y) != float:
                raise TypeError('Populacja musi byc int albo float')
        self.nazwa = x
        self.populacja = y
    def print_name(self):
        print(f'Nazwa miasta: {self.nazwa} \nPopulacja: {self.populacja}')
