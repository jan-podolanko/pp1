#zadanie 5
import statistics
wynagrodzenia = [21600, 4350, 3920, 5590, 3250, 4010]
srednia = statistics.mean(wynagrodzenia)
mediana = statistics.median(wynagrodzenia)
odchstand = statistics.pstdev(wynagrodzenia)
print(f'srednia = {srednia}, mediana = {mediana}, odchylenie s. = {odchstand}')