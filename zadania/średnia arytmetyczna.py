#średnia algebraiczna

def srednia():

    liczby = list(range(0,10))                      #liczby z listy liczb od 1 do 10

    suma = sum(liczby)                              #wywołanie sumy

    srednia_arytmetyczna =suma / len(liczby)        #suma z wyżej podzielona na liczbe liczb w ciągu

    print(srednia_arytmetyczna)                     #pokaż wynik działania

    srednia()                                           #zakończ program