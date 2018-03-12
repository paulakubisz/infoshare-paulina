# 9. inupt - miesiąc oraz dzien,
#   okreslic pore roku

dzien = int(input("Wprowadz dzień: "))

miesiac = input("Wprowadz miesiac: ")

wiosna = ['marzec', 'kwiecien', 'maj']
lato = ['czerwiec', 'lipiec', 'sierpien']
jesien = ['wrzesien', 'październik', 'listopad']
zima = ['grudzien', 'styczeń', 'luty']

# pory_roku = [wiosna, lato, jesień, zima]

if dzien > 32:
        print(f"Nie znam miesiąca który miałby {dzien} dni")
        exit()

if dzien > 1 and dzien < 32 and miesiac in wiosna:
    print(f"{dzien} {miesiac} to Wiosna")

if dzien > 1 and dzien < 32 and miesiac in lato:
    print(f"{dzien} {miesiac} to Lato")

if dzien > 1 and dzien < 32 and miesiac in jesien:
    print(f"{dzien} {miesiac} to Jesień")

if dzien > 1 and dzien < 32 and miesiac in zima:
    print(f"{dzien} {miesiac} to Zima")