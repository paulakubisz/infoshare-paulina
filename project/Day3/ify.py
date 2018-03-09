#blok kodu – logiczne oddzielenie kokdu . Wszystkie instrukcje się buduje poprzez zagniezdzenie w poprzednim bloku np.
#Instrukcja:
#	Instrukcja:
#		Instrukcja:
#Indentacja – 4 spacje , inaczej mowiac wciecia


#if  (warunek):
# kod wykonywany gdy warunek prawdziwy

#elif (inny warunek):
# kod wykonywany gdy warunek if był falszywy
#elife musi być prawdziwy aby ten kod się wykonal

#else
#przypadek domyslny, jeżeli wszystko powyzej jest nieprawdziwe
#bedzie wykonany kiedy if i elify były nieprawdziwe
#moze być jeden albo wcale

#kod leci z gory na doł, if sa niezalezne od siebie

a = 44

if a > 2:
    print("Hejka")

elif a == 44:
    print(f'a jest równe {a}')

print("Koniec")