#ilosc parzystych i nieparzystych w zakresie


zakres = range(34,45678)

parzyste = 0 #licznik po ktorym znamy ilosc cyfr
nieparzyste = 0

for liczba in zakres:
    if liczba % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

print(f"Parzystych: {parzyste}, nieparzystych: {nieparzyste}.")