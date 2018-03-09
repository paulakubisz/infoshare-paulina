#dostajemy liczbe od useram, chcemy sprawdzic czy jest podzielna przez 3 i podzielna przez 5


#liczba = int(input("Podaj liczbę: ")) # jezeli chcemy zamienic string w inny typ, w tym wypadku w calkowtie

liczba = (input("Podaj liczbę: ")) # jezeli chcemy zamienic string w inny typ, w tym wypadku w calkowtie inny sposob:

#liczba_int = int(liczba) #nadpisujemy stara liczbe nowa, tworzymy nowa zmienna

if liczba.isdigit():
    liczba = int(liczba)

    # jesli liczba podzielna jest przez 3 i 5
    if liczba % 3 == 0 and  liczba % 5 == 0: #na koncu :
        print(f"Liczba {liczba} jest podzielna przez 3 i 5")   # potwierdz

    # w przeciwnym razie:
    else:
        print(f"Liczba {liczba} nie jest podzielna przez 3 i 5.")  # napisz, ze nie jest podzielna przez 3 i 5

else:
    print("Podaj tylko cyfry!")

#print(liczba)
#print(type(liczba)) #typ liczby



