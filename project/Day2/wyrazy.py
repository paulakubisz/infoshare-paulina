#zdanie = "Dzisiaj jest wtorek 6 marca"
#literka = "b"


#interaktywny program
zdanie = input("Podaj zdanie: ")
literka = input("Podaj literke do policzenia: ")



ilosc = zdanie.count(literka)

print("W Twoim zdaniu znak", literka, "wystepuje", ilosc, "razy.")

print(f"W Twoim zdaniu znak '{literka}' wystepuje {ilosc} razy") # specjalne formatowanie stringa poprzed dodanie f przed ", w nowym pythonie od 3,6

print("W Twoim zdaniu znak '{}' wystepuje {} razy".format(literka,ilosc)) # w starym pythonie
