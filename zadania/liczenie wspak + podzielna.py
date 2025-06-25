#liczenie liczb podzielnych przez coś wspak

def liczba():                               #definicja zmiennej
    for i in range(100, -1,-1):             #dla i jakiegoś przedziału , -1,-1 = wspak
        if i % 2 ==0:                       #jeśli i %= podzielne , ==0 - reszta 0

            print(i)                        #pokaż i



liczba()                                    #zakończenie programu