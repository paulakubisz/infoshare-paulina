# 12. sprawdź czy podany znak jest samogłoską, spółgłoską, cyfrą czy znakiem specjalnym
#     wypisz odpowiedź


SAMOGLOSKI = "aeiouyAEIOUY"
znak = input("Podaj znak: ")

#sprawdzamy czy dostalismy jeden znak
if len(znak) == 1:
    print("Twoj znak to: {}".format(znak)) #jezeli tak

else: #jezeli nie to koniec
    print("Moze byc tylko jeden znak!")
    exit()

if znak in SAMOGLOSKI: #sprawdzamy czy wprowadzony znak jest samogloska
    print(f"Twoj znak {znak} jest samogłoską!")

elif znak.isdigit(): #sprawdzamy czy jest cyfrą
    print(f"Twoj znak {znak} jest cyfrą!")

#wartosci <65 w tabeli ASCII
elif ord(znak) < 65 or (ord(znak) > 90 and ord(znak) < 97):
    print("Twoj znak to znak specjalny!")

else:
    print("Twoj znak to spółgłoska!")