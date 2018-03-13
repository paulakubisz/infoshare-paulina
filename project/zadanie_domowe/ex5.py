
# 5. ruletka: otrzymawszy liczbę, sprawdź czy jest ona:
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

ruletka = int(input("Wprowadz wylosowaną liczbę: "))
czerwone = (1,3,5,7,9,12,14,16,19,21,23,25,27,30,32,34,36)
czarne = (2,4,6,8,10,11,13,17,20,22,24,26,28,29,31,33,35)

if ruletka in czerwone and ruletka % 2 == 0:
    print("Czerwone, parzyste")

elif ruletka in czerwone and ruletka % 2 > 0:
    print("Czerwone, nieparzyste")

elif ruletka in czarne and ruletka % 2 == 0:
    print("Czarne, parzyste")

elif ruletka in czarne and ruletka % 2 > 0:
    print("Czarne, nieparzyste")

else:
    print(f"Wskzana liczba: {ruletka} - nie jest zgodna z zasadami gry! Podaj liczbę mniejszą niż 36!. ")
