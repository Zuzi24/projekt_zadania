def liczba_słów():
    return len(zdanie.split())              #Funkcja split() dzieli tekst (czyli zdanie)
                                            # na listę wyrazów, len liczy słowa

zdanie = input("podaj zdanie: ")            #zdanie = podane zdanie

print(liczba_słów())                        #pokaż ile słów (czyli wynik funkcji def)

