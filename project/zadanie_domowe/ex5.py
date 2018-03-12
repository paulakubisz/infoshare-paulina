
# 5. ruletka: otrzymawszy liczbę, sprawdź czy jest ona:
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

ruletka = int(input("Wprowadz wylosowaną liczbę: "))
#czerwone = (1,3,5,7,9,12,14,16,19,21,23,25,27,30,32,34,36)
#czarne = (2,4,6,8,10,11,13,17,20,22,24,26,28,29,31,33,35)

if ruletka == 11 or ruletka ==  12 or ruletka ==  17 or ruletka == 29 or ruletka == 31 or ruletka == 33 or ruletka == 35:
    print("Czarne, nieparzyste")

elif ruletka == 12 or ruletka == 14 or ruletka == 16 or ruletka ==30 or ruletka == 32 or ruletka == 34 or ruletka == 36:
    print("Czerwone, parzyste")

elif ruletka > 0 and ruletka < 37 and ruletka % 2 > 0:
    print("Czerwone, nieparzyste")

elif ruletka > 0 and ruletka < 36 and ruletka % 2 == 0:
    print("Czarne, parzyste")


