
plik = open('lokomotywa.txt', 'r')

zawartosc = plik.read()

print(zawartosc)

plik.close() #zawsze pamietaj zeby zamknac plik


print('-------readline')


with open('lokomotywa.txt', encoding="utf-8") as plik:

    linijka = plik.readline()

    print(linijka, end="")

    print(plik.readline(), end= "")
    print(plik.readline().strip())
    print(plik.readline(), end= "")
    print(plik.readline(), end= "")




print('-------readlines')

with open('lokomotywa.txt', encoding="utf-8", mode="r") as plik:

    linijki = plik.readlines()
    print(linijki)

    gdzie_jestem = plik.tell()
    print(gdzie_jestem)


    plik.seek(0)
    print(plik.readline())
