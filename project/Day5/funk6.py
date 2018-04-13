# podaj imie oraz ewentualnie liste , do ktorj imie ma byc dodne
# jak nie podam listy, to ma byc zwrocona nowa lista z wpisanym imieniem
#j ak podam liste to imie ma byc dopisane do listy
#

print("------pierwsz sposob")
#buduje sie lista poniewaz kod wykonuje sie jeden po drugim i dopisujemy do listy
def dodaj_imie2(imie, lista=[]):
    lista.append(imie)
    return lista

anglicy = dodaj_imie2("John")
print(anglicy)

anglicy = dodaj_imie2("adami", anglicy)
print(anglicy)

rosjanie = dodaj_imie2('Sergiej')
print(rosjanie)


polacy = dodaj_imie2("Arek")
print(polacy)



print("------drugi sposob")

def dodaj_imie(imie, lista=None):
    if lista == None:
        lista = []
    lista.append(imie)
    return lista

anglicy = dodaj_imie("John")
print(anglicy)

anglicy = dodaj_imie("adami", anglicy)
print(anglicy)

# frnacuzi = ['pier']
# francuzi + dodaj_imie('francois', francuzi)

rosjanie = dodaj_imie('Sergiej')
print(rosjanie)


polacy = dodaj_imie("Arek")
print(polacy)