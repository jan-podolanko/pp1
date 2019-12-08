import random
class termometr():
    def __init__(self):
        self.temperatura = 36.0
    def zmierz_temperature(self):
        self.temperatura = round(random.uniform(34.0,42.0),1)
    def wyswietl_temperature(self):
        if self.temperatura >= 37.0 and self.temperatura < 41.0:
            print(f'Zmierzona temperatura: {self.temperatura}C (goraczka)')
        elif self.temperatura >= 41.0:
            print(f'Zmierzona temperatura: {self.temperatura}C (stan zagrozenia zycia)')
        else:
            print(f'Zmierzona temperatura: {self.temperatura}C')

x = termometr()
x.zmierz_temperature()
x.wyswietl_temperature()
x.zmierz_temperature()
x.wyswietl_temperature()