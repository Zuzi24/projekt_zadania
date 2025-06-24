#ile liter x w danym słowie

word = input("podaj słowo: ")           #podanie słowa
x = input("podaj litere: ")             #określenie litery

liczba_liter = word.lower().count(x)    #liczba_liter to nazwa zmiennej, word.lower = małe litery
                                        #.count(x) = ile x znajduje sie w danym słowie

print("występuje: ", liczba_liter)      # tekst występuje + pokazanie wyniku