#kopiowanie listy

elementy = [1, 3 ,[ 8, 9,'ala'], '45']
print(elementy)

elementy1 = elementy.copy()
print(elementy1)

elementy2 = list(elementy)
print(elementy2)

elementy3 = elementy[:]
print(elementy3)

elementy[2][2] = 'Ola'


print(elementy)

print(elementy1)

print(elementy2)

print(elementy3)

print(elementy)