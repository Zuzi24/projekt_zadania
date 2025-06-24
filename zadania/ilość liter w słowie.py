#ile liter w słowie

def calculate(slowo):          #definiujemy dla zmiennej
    return len(slowo)           #oddaje liczbe liter

wynik = input("podaj słowo: ")      #wywołuje wpisanie słowa
print(calculate(wynik))             #podaje wynik funkcji liczącej litery