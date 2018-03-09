# 7. po podaniu nazwy miesiaca, program napisze ilosc dni w miesiacu
#sprawdz ze miesiac nie jest liczba -DOM

miesiac = input("Podaj miesiąc: ")

if miesiac.isdigit(): #SPRAWDZ CZY TO LICZBA
    print("Wprowadz nazwę miesiąca słownie np. styczeń!")

if miesiac == "kwiecien" or miesiac == "czerwiec" \
    or miesiac == 'wrzesien' or miesiac == 'listopad':

    print(f"{miesiac.upper()} ma 30 dni!")
elif miesiac == "luty" or "Luty" or "LUTY":
    print("Luty ma 28 lub 29 dni!")
else:
    print(f"{miesiac.upper()} ma 30 dni!")