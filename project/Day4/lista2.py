lista = ['kwiatek', '234', 'ala', '4353,676']

print(lista[2])
print(lista[2: :2])

lista[2] = 'Ola'

#del lista[3] #usuwa element

x = lista.pop(3)  #pop wzial element z listy i zapisal pod zmienna i mozna to dalej uzyc, jak nie podamy elementu usunie ostatni element
print(lista)

zdanie = "Ala ma kota, czarno-burego"
lista_zdanie = list(zdanie)
print(lista_zdanie)

lista_zdanie[12] = "X" # do 13 elementu przypisuje X
lista_zdanie.pop(7)

sklejone_zdanie = ''.join(lista_zdanie) #jak z listy zroic jeden strin  - dodajemy pustego strina, jak dodamy w "x" to bedzie z x w srodku kazdego
print(sklejone_zdanie)