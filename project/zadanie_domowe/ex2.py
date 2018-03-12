# 2. obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

rok = int(input("Wprowadź roku który chcesz sprawdzić: "))

if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
    print(f"Tak, rok {rok} jest rokiem przestępnym! ")

else:
    print(f"Nie, rok {rok} nie jest rokiem przestępnym! ")