import  copy

elementy = [1, 3 ,[ 8, 9,'ala'], '45']

elementy1 = copy.deepcopy(elementy)

print(elementy1)
elementy[2][2] = 'OLA' # PRZEZ ZASTOSOWANIE COPY.DEEPCOPY - DANA PODMIENI SIE TYLKO W TEJ NOWEJ LISCIE A NIE W PIERWOTNEJ

print(elementy)
print(elementy1) #TYLKO TUTAJ SIE PODMIENI POPRZEZMETODE Z IMPORTU,

#LISTY SA TYPAMI REFERENCYJNYMI

