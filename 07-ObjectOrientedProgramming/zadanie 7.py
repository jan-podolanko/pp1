#zadanie 7

class Student():
    uczelnia = 'UEK'
    nr_albumu = 100000
    def __init__(self,imie,nazwisko,kierunek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kierunek = kierunek
        self.nr_albumu = Student.nr_albumu
        Student.nr_albumu += 1 
    def __str__(self):
        return f'{self.imie} {self.nazwisko} ({Student.nr_albumu}), {self.kierunek}, {Student.uczelnia}'


print(Student('Jan','Podolanko','Informatyka stosowana'))
print(Student('Jan2','Podolanko','Informatyka stosowana'))
print(Student('Jan3','Podolanko','Informatyka stosowana'))
