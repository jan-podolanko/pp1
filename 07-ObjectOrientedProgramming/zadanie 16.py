class Student():
    str1 = 'Imię: '
    str2 = 'Nazwisko: '
    str3 = 'Numer albumu: '
    n = '\n'
    def __init__(self,imie,nazwisko,nr_albumu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_albumu = nr_albumu
    def display(self):
        print(f'{Student.str1:>15}{self.imie}{Student.n}{Student.str2:>15}{self.nazwisko}{Student.n}{Student.str3:>15}{self.nr_albumu}')
    def __eq__(self,other):
        self.nr_albumu == other.nr_albumu
    def __lt__(self,other):
        self.nr_albumu < other.nr_albumu

students = [
Student('Anna','Tomaszewska',141820),
Student('Wojciech','Zbych',201003),
Student('Maja','Kowalska',153202),
Student('Marek','Migiel',138600)
]

for i in students:
    i.display()
    print()
students2 = sorted(students,key=lambda student: student.nr_albumu)
for j in students2:
    j.display()
    print()