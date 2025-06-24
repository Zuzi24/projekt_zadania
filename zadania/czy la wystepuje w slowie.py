#napisz funkcje która będzie sprawdzała czy sylaba la znajduje sie w słowie podanym przez uzytkownika

def sylaba():                                         #definicja zmiennej
    return True if 'la' in slowo else False           #warunek True -> la , else=w innym wypadku -> False
                                                        #slowo = input podany na dole
slowo = input("podaj słowo: ")                          #podanie słowa

print(sylaba())                                        #pokaż wynik działania funkcji