#średnia algebraiczna ze wpisaniem przedziału

def srednia():
    y = int (input("liczba z przedziału od: "))         #int=że dane to będa liczby , input=podaj
    x = int(input("do: "))                              #x i y definiują podane liczby przez użytkownika

    liczby = list(range(y,x))                       #liczby z listy liczb od x do y

    suma = sum(liczby)                              #suma

    srednia_arytmetyczna =suma / len(liczby)        #suma z wyżej podzielona na liczbe liczb w ciągu

    print(srednia_arytmetyczna)                     #pokaż wynik działania

srednia()                                           #zakończ program