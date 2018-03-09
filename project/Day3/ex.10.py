# 10. zamiana temperatury
#     wejscie: "35C"
#     wyjście: "Temperatura 35 stopni Celsjusza to 100 stopni Fahrenheitha"
#     wejscie: "100F"
#     wyjście: "Temperatura 100 stopni Fahrenheitha to 35 stopni Celsjusza"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

wejscie = input("Podaj temperature: ")

if wejscie[-1] == "C":
    temp_c = int(wejscie[0:-1]) # zmiana czesci strina na int, zebysmy mobli wykonac polecenie. tworzymy kopie pierwszego stringa
    temp_f = temp_c * (9 / 5) + 32
    print(f"{temp_c} stopni C to {temp_f} stopni F.")


elif wejscie[-1] == "F":
    temp_f = int(wejscie[:-1])
    temp_c = (temp_f - 32) * (5/9)
    print(f"{temp_fs} stopni F to {temp_c: .2f} stopni C.") # .2f mowi wydrukuj mi flouta z dwoma miejscami po przecinku

else:
    print("Żle wprowadziles dane")