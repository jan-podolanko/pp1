#zadanie 5

class Utwor():
    def __init__(self, wykonawca, utwor, album, rok):
        self.wykonawca = wykonawca
        self.utwor = utwor
        self.album = album
        self.rok = rok
    def __str__(self):
        return 'Wykonawca: ' + self.wykonawca + '\n' + 'Utwor: ' + self.utwor + '\n' + 'Album: ' + self.album + '\n' + 'Rok: ' + self.rok

print(Utwor('wykonawca', 'utwor', 'album', 'rok'))