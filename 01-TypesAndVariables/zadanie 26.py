masa = float(input('Podaj swoją masę (w kg): '))
wzrost = float(input('Podaj swój wzrost (w metrach): '))

bmi = masa / (wzrost ** 2)

print('Twój wskaźnik BMI wynosi {}.'.format(bmi))

if bmi >= 18.5 and bmi < 25.0:
    print('Twoja waga jest prawidłowa.')
else:
    print('Twoja waga jest nieprawidłowa.')
