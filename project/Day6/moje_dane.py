osoby = ['jan kowalski', 'anna nowak', 'antoni pawlak']

# with open('osoby.txt', 'w', encoding='utf-8') as plik:
#     plik.write("Ola ma tez psa\n")
#     plik.write("Pies reksio ma wakacja\n")



# with open('osoby.txt', 'a', encoding='utf-8') as plik:
#     plik.write("To jest dopisana linijka w trybie a\n")


with open("moje_osoby.txt", 'w', encoding='utf-8') as plik:

    for indkes, osoba in enumerate(osoby):
        osoby[indkes] = osoba + "\n"
    print(osoby)
    plik.writelines(osoby)


