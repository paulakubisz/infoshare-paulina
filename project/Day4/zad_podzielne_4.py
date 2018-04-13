#wszystkie liczby od 0-20 podzielne przez 4

zakres = range(0,21)

for liczba in zakres:
    if liczba % 4 != 0:
        print(liczba)


#drugi sposob

for liczba in zakres:
    if liczba % 4 == 0:
        continue
    else:
        print(liczba)