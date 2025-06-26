#napisz funkcje ktora zliczy ile jest liter określonego rodzaju w zdaniu podanym przez użytkownika

zdanie = input("podaj zdanie: ")
x = input("podaj litere: ")

bez_spacji = zdanie.replace(" ", "")

litera = bez_spacji.count(x)


print(litera)