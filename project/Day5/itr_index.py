#kolejka do lekarza, wypisac nr w kolejnce i imie


print('-------while')

u_lekarza = ["Adam Wędzonka", "Anna Szklanka", "Tomasz Pisak", "Jędrzej Myszka"]

licznik =  0

dl_kolejki = len(u_lekarza)

while licznik < dl_kolejki:
     print(f"Na miejscu {licznik+1} w kolejce jest {u_lekarza[licznik]}")
     licznik += 1


print('-------for')

for licznik in range(len(u_lekarza)):
    print(f"Na miejscu {licznik+1} w kolejce jest {u_lekarza[licznik]}")


print('-------enumerate')

for indeks, element in enumerate(u_lekarza):
    print(f"Na miejscu {indeks+1} w kolejce jest {element}")

print('-------enumerateBEZrozpakowania')

for element in enumerate(u_lekarza):
    print(f"Na miejscu {element} w kolejce jest {element}")