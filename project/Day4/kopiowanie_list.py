elementy = [1, 3 ,'ala', '45']
print(elementy)
#kopiowanie listy

elementy1 = elementy.copy()
print(elementy1)


elementy2 = list(elementy)
print(elementy2)


elementy3 = elementy[:]
print(elementy3)


elementy[2] = 'Ala'
print(elementy)

print(elementy1)

print(elementy2)

print(elementy3)