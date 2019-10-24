c = float(input('Podaj poziom temperatury w skali Celsjusza: '))

#konwersja na skalę fahrenheita
f = c * 1.8 + 32
#konwersja na skalę kelvina
k = c + 273.15

print('Temperatura w skali Fahrenheita wynosi {} stopni.'.format(f))
print('Temperatura w skali Kelvina wynosi {} stopni.'.format(k))
