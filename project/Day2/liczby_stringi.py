#liczba_a = int(input("Podaj liczbę a: "))
#liczba_b = (input("Podaj liczbę b: "))
#liczba_b =  int(liczba_b)
#print(liczba_a + liczba_b)  #jak zamienic zeby liczby sie doday a nie zsumowalu - nalezy dodanc int - jako int przed inputem,
# drugim sposobem jest przypisanie do zmienniej int - zawsze pierwsza jest wykonana prawa strona a pozniej lewa strona


x = 0.1
y = 3 * 0.1

print(x == y)

#to nie jest to samo jak np. 0,33333333

print(f"x: {x: .19f} y: {y: .19f}") # 19 miejsc po przecinku

zaokr_x = round(x, 6)  #skrocone do 6 miejsc po przecinku
zaokr_y = round(y, 6) #skrocone do 6 miejsc do przecinku
print(zaokr_x,zaokr_y) #print ucina 0 na koncu wyrazenia
print(zaokr_x,zaokr_y) #print ucina 0 na koncu wyrazenia


print(f"{zaokr_x: .9f} == round{zaokr_y: .9f}") #pozwala  wstawic wyrazenie - zmienna, albo wyrazenie do obliczenia

zdanie= "Ala ma kota"

formatowanie = f"Moje zdanie to {zdanie}"  #formatowanie stringa - mozemy uzyc {} jak chcemy wpisywac jakies zmieniajace zmienne
print(formatowanie)