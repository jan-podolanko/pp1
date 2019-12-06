class University():
    #konstruktor:
    def __init__(self):
        self.name = 'UEK'
        self.fullname ='Uniwersytet Ekonomiczny w Krakowie'
    def set_name(self, new_name):
        self.name = new_name
    def set_fullname(self, new_fullname):
        self.fullname = new_fullname
    def print_name(self):
        print(self.name)
    def print_fullname(self):
        print(self.fullname)
        
zmienna = University()
zmienna.set_name('AGH')
zmienna.set_fullname('Akademia Górniczo-Hutnicza')
zmienna.print_name()
zmienna.print_fullname()