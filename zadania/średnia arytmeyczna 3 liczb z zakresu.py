#średnia algebraiczna 3 liczby z zakresu

def srednia_z_zakresu():

 input("podaj trzy liczby podzielone spacją: ")

dane = input("Wpisz liczby oddzielone spacją: ")

liczby = [int(x) for x in dane.split()]

liczby_z_zakresu = [x for x in liczby if 0 <= x <= 200]

if liczby_z_zakresu:
    srednia = sum(liczby_z_zakresu)/len(liczby_z_zakresu)
    print(f"Średnia liczb z zakresu 0-200 wynosi: {srednia}")
else:
    print("Nie podano żadnych liczb w zakresie 0-200.")

srednia_z_zakresu()

