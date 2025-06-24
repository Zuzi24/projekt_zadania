#liczba podzielna przez

def liczba():                #definiujemy liczbe
    for i in range(1, 100):   #wybieramy dla jakiego i definiujemy , range=z jakiego przedziału
        if i % 2 == 0:         # %=dzieli sie przez, if = jeśli coś, reszta 0 bo wtedy sie dzieli
            print(i)           #pokaż wartość i
liczba()                       #zakończ definiowanie